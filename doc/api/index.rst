.. LitePolis API documentation master file, created by
   sphinx-quickstart on Thu Jun 27 03:45:19 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to LitePolis API's documentation!
=========================================

## Getting Started
To run the API, execute the following command:
```bash
$ SQLUSER="root" SQLPASS="mysecret" SQLHOST="localhost" SQLPORT="9030" ui="streamlit" fastapi dev main.py --host 0.0.0.0 --port 8000
```
This will start the API on `http://0.0.0.0:8000` in development mode.

> The API documentation is available at `http://0.0.0.0:8000/docs` through Swagger.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   main
   route
   db

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
