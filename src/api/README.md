# Developer doc

- [DB spec](../../doc/database.md)
- [API spec](../../doc/api)

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
