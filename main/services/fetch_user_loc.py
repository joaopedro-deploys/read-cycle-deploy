import json
import os
import requests
from ..models import UserModel

def fetch_user_loc_data(user:UserModel, city:str=None, state: str=None, country:str='Brasil') -> dict:
    user_city = user.get('city') or city
    user_state = user.get('state') or state
    user_country = user.get('country') or country

    key = os.environ.get('OPENCAGEDATA_KEY')

    params = [user_city, user_state, user_country]

    url = f'https://api.opencagedata.com/geocode/v1/json?q={params}&key={key}'
    headers = {
        'Content-type': 'Application/json',
        'Accepted': 'Application/json'
    }
    response = requests.get(url=url, headers=headers)
    print('code', response.status_code)
    data = json.loads(response.text)
    return data['results'][0].get('geometry')



