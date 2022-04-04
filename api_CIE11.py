import requests
import constants
import pprint

from CIE11 import CIE11


def get_access_token() -> str:
    response = requests.post(constants.TOKEN_ENDPOINT, data=constants.PAYLOAD, verify=False).json()
    token = response['access_token']
    return token

get_access_token()


def generate_headers():
    return {
        'Authorization': 'Bearer ' + get_access_token(),
        'Accept': 'application/json',
        'Accept-Language': constants.LANGUAGE,
        'API-VERSION': constants.API_VERSION
    }


def generate_body(parameter: str) -> dict:
    return {
        'q': parameter+'%',
        'useFlexisearch': 'false',
        'flatResults': 'true',
        'highlightingEnabled': 'true'
    }


def search_diagnosis(body: dict, headers: dict) -> CIE11:
    response = requests.post(constants.SEARCH_URI_POST, headers=headers, params=body, verify=False)
    response_json = response.json()
    if response_json['error']:
        return CIE11(error=True, error_message=response_json['errorMessage'], chapters=[])
    else:
        chapters = [x['chapter'] for x in response_json['destinationEntities']]
        if len(chapters) == 0:
            return CIE11(error=True, error_message='No result found!', chapters=[])
        else:
            return CIE11(chapters=chapters)
