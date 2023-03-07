# Create a dict / map with accesion numbers as keys and DOIs as values

import requests

BRAPI_SERVER_BASE_URL = 'https://test-server.brapi.org/brapi/v2/'
BRAPI_SERVICE_URL = BRAPI_SERVER_BASE_URL + 'germplasm'

response = requests.get(BRAPI_SERVICE_URL).json()

germplasm = response['result']['data']

accenumbs_dois = { g['accessionNumber'] : g['germplasmPUI'] for g in germplasm }

accenumbs_dois