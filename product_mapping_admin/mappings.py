import os

import requests
from dotenv import load_dotenv

from .auth0.connect import get_token


def get_all_products():
    load_dotenv()
    token = get_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    blackhawk_url = os.getenv('BLACKHAWK_HOST')
    url = f'{blackhawk_url}/product_mappings'

    return requests.get(url, headers=headers).json()['data']