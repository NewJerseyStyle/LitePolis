FROM python:3.11

ARG UI="streamlit"
ARG SQLUSER="apiuser"
ARG SQLPASS="sqlpass"
ARG SQLHOST="localhost"
ARG SQLPORT="9030"
ARG API_KEY="apikey"

WORKDIR /code

COPY api/* .

CMD ["fastapi", "run", "/code/main.py"]
