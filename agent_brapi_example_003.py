# Extract DOIs of available germplasm

import requests

BRAPI_SERVER_BASE_URL = 'https://test-server.brapi.org/brapi/v2/'
BRAPI_SERVICE_URL = BRAPI_SERVER_BASE_URL + 'germplasm'

response = requests.get(BRAPI_SERVICE_URL).json()

germplasm = response['result']['data']

dois = [ g['germplasmPUI'] for g in germplasm]

dois