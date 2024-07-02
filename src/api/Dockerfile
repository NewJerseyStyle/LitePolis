FROM python:3.11

ENV UI="streamlit"
ENV SQLUSER="apiuser"
ENV SQLPASS="sqlpass"
ENV SQLHOST="localhost"
ENV SQLPORT="9030"
ENV API_KEY="apikey"

WORKDIR /code

COPY . .
RUN pip install -U pip
RUN pip install -r requirements.txt

CMD ["fastapi", "run", "/code/main.py"]
