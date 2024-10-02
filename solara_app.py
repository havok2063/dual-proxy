
import solara
from jdaviz_app import Page as JPage

@solara.component
def Page():
  solara.Button("hi")


@solara.component
def Layout(children=[]):
    # there will only be 1 child, which is the Page()
    return children[0]


@solara.component
def Home():
    solara.Markdown("Solara Home")

routes = [
    solara.Route(path="/", component=Home, label="Home", layout=Layout),
    solara.Route(path="test", component=Page, label="Test"),
    solara.Route(path='jdaviz', component=JPage, label='Jdaviz')
]