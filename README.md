
# Readme

example of a FastAPI python application deployed behind a dual-proxy nginx config.
The FastAPI app has a Solara application sub-mounted into it.  The Solara app has
three pages: a home page, a test page, and a page with a Jdaviz component.

# Setup

## Set up fake production domains

1. Edit your `/etc/hosts` file
2. Add the following lines:

- 127.0.0.1 data.prod.org
- 127.0.0.1 viz.prod.org

First proxy is `data.prod.org` and the second proxy is `viz.prod.org`


## Run docker

1. run `docker compose up --build`
2. navigate to `data.prod.org/valis/` for main fast api app
3. navigate to `data.prod.org/valis/solara` for main solara app
4. navigate to `data.prod.org/valis/solara/jdaviz` for jdaviz page
5. kill and run `docker compose down`