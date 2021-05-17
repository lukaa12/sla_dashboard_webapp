# SLA Dashboard web application
Example web application visualizing SLA adherence based on Kentik synthetic mesh test data

## Run the app


Run the web server with:
```bash
export KTAPI_AUTH_EMAIL=<your kentik api email>
export KTAPI_AUTH_TOKEN=<your kentik api token>
python main.py
```

## Application configuration

Configuration is stored in config file [config.yaml](./config.yaml)

## Development

1. Prepare virtual environment with `virtualenv venv`
1. Activate virtual environment with `source venv/bin/activate`
1. Install requirements with `pip install -r requirements.txt`
1. (Optionally) Update the local schema as described [here](##Updating-the-local-schema)
1. Generate synthetics client with `generate_client.sh`

## Updating the local schema

1. Get swagger specification for synthetics from <https://github.com/kentik/api-schema-public/tree/master/gen/openapiv2/kentik/synthetics/v202101beta1>
1. Convert swagger spec to openapi 3 spec using <https://mermade.org.uk/openapi-converter>
1. Save the openapi 3 spec as `synthetics.openapi.yaml` in project root directory

## TODO

- change Dash config "debug" -> False
- change default Flask development http server to production ready server
