import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ab72e87febc052f9345dc2e07cb94df5'
HEADER = {'Content-Type': 'application/json','trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "german@dolnikov.ru",
    "password": "Iloveqa1"
}
body_confirmation = {
     "trainer_token":  TOKEN

}
body_create = {
    "name": "generate",
    "photo_id": -1
}

body_smena = {
    "pokemon_id": "119897",
    "name": "New Name"
}

body_pokebol = {
    "pokemon_id": "119897"
}
#response = requests.post(url = f'{URL}/trainers/reg', headers= HEADER, json= body_registration)
#print(response.text)

#response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers= HEADER, json= body_confirmation)
#print(response_confirmation.text)

#response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
#print(response_create.text)

#message = response_create.json()['message']
#print(message)


"""response_smena = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_smena)
print(response_smena.text)"""

"""message = response_smena.json()['message']
print(message)"""

response_pokebol = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokebol)
print(response_pokebol.text)

message = response_pokebol.json()['message']
print(message)