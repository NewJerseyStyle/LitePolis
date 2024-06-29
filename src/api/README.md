# Developer doc
- [DB spec](../../doc/database.md)
- [API spec](../../doc/api)
## Getting started
To run the API, execute the following command:
```bash
SQLUSER="root" SQLPASS="mysecret" SQLHOST="localhost" SQLPORT="9030" ui="streamlit" fastapi dev main.py --host 0.0.0.0 --port 8000
```
This will start the API on `http://0.0.0.0:8000` in development mode.

> ℹ️ The API documentation is available at `http://0.0.0.0:8000/docs` through Swagger.

## Generating API client with `openapi-generator`
1. get json from `localhost:8000/openapi.json`
```bash
wget http://localhost:8000/openapi.json
```
2. Generate API client using `openapi-generator` docker image
```bash
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
                -i /local/openapi.json \
                -p litepolis_client \
                -g <target-tech> \
                -o /local/generated
```
> ℹ️ Change `<target-tech>` to `python`, `typescript-axios`, `android`
> or other target technology you want to support
