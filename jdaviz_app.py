
import pathlib

import astropy.units as u
import numpy as np
import solara
from specutils import Spectrum1D


def get_config():
    """ create custom jdaviz configuration """
    from jdaviz.core.config import get_configuration

    # get the default specviz config
    config = get_configuration('specviz')

    # set custom settings for embedding
    config['settings']['viewer_spec'] = config['settings'].get('configuration', 'default')
    config['settings']['server_is_remote'] = True
    config['toolbar'].remove('g-data-tools') if config['toolbar'].count('g-data-tools') else None

    return config


@solara.component
def Jdaviz():
    """ component for displaying Jdaviz """
    import os

    import ipygoldenlayout
    import ipysplitpanes
    import ipyvue
    import jdaviz
    from IPython.display import display
    from jdaviz import Application, Specviz
    from jdaviz.app import custom_components

    ipysplitpanes.SplitPanes()
    ipygoldenlayout.GoldenLayout()
    for name, path in custom_components.items():
        ipyvue.register_component_from_file(None, name, os.path.join(os.path.dirname(jdaviz.__file__), path))

    ipyvue.register_component_from_file('g-viewer-tab', "container.vue", jdaviz.__file__)

    css = """
    main.v-content.solara-content-main {
        padding: 0px !important;
    }

    .widget-output {
        margin: 0;
    }

    .jdaviz {
        height: 100vh !important;
    }

    .v-content.jdaviz__content--not-in-notebook {
        height: 100vh !important;
        max-height: 100vh
    }
    """

    solara.Style(css)
    with solara.Column():

        config = get_config()
        app = Application(configuration=config)
        style_path = pathlib.Path(__file__).parent / 'custom_style.vue'
        app._add_style(str(style_path))
        spec = Specviz(app)
        spec.load_data(Spectrum1D(np.arange(100)*u.Jy))

        display(spec.app)


@solara.component
def Page():
    """ main page component """

    with solara.Column():
        solara.Title("Spectral Display")

        Jdaviz()
