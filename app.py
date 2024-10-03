
import os
from fastapi import FastAPI

try:
    os.environ['SOLARA_ROOT_PATH'] = os.getenv("SOLARA_ROOT")
    os.environ['SOLARA_APP'] = 'solara_app.py'
    os.environ['SOLARA_THEME_VARIANT'] = 'dark'
    # this solara import needs to come after the os environ setup
    import solara.server.fastapi as solara_server
except ImportError:
    solara_server = None

app = FastAPI(title='Valis', description='Test', root_path="/valis")

@app.get("/", summary='Hello World route', response_model=dict)
def hello():
    return {"Hello": "This is the FastAPI World"}


app.mount('/solara/', app=solara_server.app)

if __name__ == "__main__":
    app.run()
