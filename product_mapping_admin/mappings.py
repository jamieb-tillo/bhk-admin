import os

import requests
from dotenv import load_dotenv

from .auth0.connect import get_token

blackhawk_url = os.getenv('BLACKHAWK_HOST')
url = f'{blackhawk_url}/product_mappings'


def get_headers():
    load_dotenv()
    token = get_token()
    return {
        'Authorization': f'Bearer {token}'
    }


def get_all_products():
    return requests.get(url, headers=get_headers()).json()['data']


def create_new_product(data):
    return requests.post(url, data=data, headers=get_headers())


def edit_product_mapping(product_id, data):
    return requests.put(f'{url}/{product_id}', data=data, headers=get_headers())


def delete_product_mapping(product_id):
    return requests.delete(f'{url}/{product_id}', headers=get_headers())
