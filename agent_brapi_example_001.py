# List all available services of a BrAPI server

import requests

BRAPI_SERVER_BASE_URL = 'https://test-server.brapi.org/brapi/v2/'
BRAPI_SERVICE_URL = BRAPI_SERVER_BASE_URL + 'serverinfo'

response = requests.get(BRAPI_SERVICE_URL).json()

calls = response['result']['calls']

services = [call['service'] for call in calls]

services