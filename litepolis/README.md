Developer doc

DB spec

API spec

generating client with `openapi-generator`

get json from `localhost:8000/openapi.json`
```bash
wget http://localhost:8000/openapi.json
```
use docker image
```bash
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
                -i /local/openapi.json \
                -p litepolis_client \
                -g <target-tech> \
                -o /local/generated
```
> ℹ️ Change `<target-tech>` to `python`, `typescript-axios`, `android`
> or other target technology you want to support
