import requests
import constants
import pprint


def get_access_token() -> str:
    response = requests.post(constants.TOKEN_ENDPOINT, data=constants.PAYLOAD, verify=False).json()
    token = response['access_token']
    return token


connection_token = get_access_token()

headers = {
    'Authorization': 'Bearer ' + connection_token,
    'Accept': 'application/json',
    'Accept-Language': constants.LANGUAGE,
    'API-VERSION': constants.API_VERSION
}

body = {
    'q': 'Retraso%',
    'useFlexisearch': 'false',
    'flatResults': 'true',
    'highlightingEnabled': 'true'
}

response = requests.post(constants.SEARCH_URI_POST, headers=headers, params=body, verify=False)
pprint.pprint(response.json())
