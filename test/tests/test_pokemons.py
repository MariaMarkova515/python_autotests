import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ab72e87febc052f9345dc2e07cb94df5'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRANER_ID = '8252'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRANER_ID})
    assert response.status_code == 200
   

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRANER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Marvel'


'''@pytest.mark.parametrize('key, value',[('name','Бульбазавр'), ('trainer_id', TRANER_ID), ('id', '119898')])
def test_parametrize(key, value): 
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRANER_ID})
    assert response_parametrize.json()["data"][0][key] == value
'''