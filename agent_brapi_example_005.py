# Get phenotypic observations for a specific germplasm / accessions

import requests
import pandas as pd

BRAPI_SERVER_BASE_URL = 'https://test-server.brapi.org/brapi/v2/'
BRAPI_SERVICE_URL = BRAPI_SERVER_BASE_URL + 'observations'

params = { 'germplasmDbId': 'germplasm1'}

response = requests.get(BRAPI_SERVICE_URL, params).json()

observations = response['result']['data']

pd.json_normalize(observations)