import os

bind = ["0.0.0.0:8765"]
workers = os.getenv("VALIS_WORKERS", 4)
worker_class = "uvicorn.workers.UvicornWorker"
daemon = False
errorlog = os.path.join(os.getenv("VALIS_LOGS_DIR", '/tmp/valis'), 'valis_app_error.log')
accesslog = os.path.join(os.getenv("VALIS_LOGS_DIR", '/tmp/valis'), 'valis_app_access.log')
root_path = '/valis'
timeout = 600