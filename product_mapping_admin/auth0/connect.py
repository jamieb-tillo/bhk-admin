import os

import requests
from dotenv import load_dotenv


def get_token():
    load_dotenv()
    oath_url = os.getenv('AUTH0_DOMAIN')

    token_url = f'{oath_url}/oauth/token'

    payload = {
        'client_id': os.getenv('AUTH0_CLIENT_ID'),
        'client_secret': os.environ.get('AUTH0_CLIENT_SECRET'),
        'audience': os.environ.get('AUTH0_API_IDENTIFIER'),
        'grant_type': 'client_credentials'
    }

    return requests.post(token_url, data=payload).json()['access_token']
