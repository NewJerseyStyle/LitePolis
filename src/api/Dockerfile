FROM python:3.11

ARG UI="streamlit"
ARG SQLUSER="apiuser"
ARG SQLPASS="sqlpass"
ARG SQLHOST="localhost"
ARG SQLPORT="9030"
ARG API_KEY="apikey"

WORKDIR /code

COPY . .
RUN pip install -U pip
RUN pip install -r requirements.txt

CMD ["fastapi", "run", "/code/main.py"]
