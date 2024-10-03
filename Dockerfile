FROM python:3.10

# Install system prereq packages
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        # these are for h5py in sdss_explorer
        curl libhdf5-dev pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
pip install --no-cache-dir fastapi["standard"] solara jdaviz gunicorn

COPY app.py /main.py
COPY solara_app.py /solara_app.py
COPY jdaviz_app.py /jdaviz_app.py
COPY custom_style.vue /custom_style.vue
COPY gunicorn_conf.py /gunicorn_conf.py

RUN mkdir /logs

ENV UVICORN_PROXY_HEADERS=1
ENV FORWARDED_PROXY_HEADERS="*"
ENV VALIS_LOGS_DIR=/logs

# single worker unicorn
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8765"]

# multi-worker gunicorn
CMD ["gunicorn", "-c", "gunicorn_conf.py", "main:app"]

# fastapi multi-worker
#CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "8765", "--workers", "4", "main.py"]
