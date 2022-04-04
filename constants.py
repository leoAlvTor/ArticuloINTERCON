TOKEN_ENDPOINT = 'https://icdaccessmanagement.who.int/connect/token'
CLIENT_ID = '-da09-492c-8d7d-aaafcdb263d0_08a84125---9161-6b47d642553b'
CLIENT_SECRET = '='
SCOPE = 'icdapi_access'
GRANT_TYPE = 'client_credentials'

PAYLOAD = {'client_id': CLIENT_ID,
           'client_secret': CLIENT_SECRET,
           'scope': SCOPE,
           'grant_type': GRANT_TYPE}

LANGUAGE = 'es'
API_VERSION = 'v2'

SEARCH_URI_POST = 'https://id.who.int/icd/entity/search'
