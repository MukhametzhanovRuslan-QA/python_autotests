import requests
import json

token = '2a6a79730d7817f07c35090ca4548164'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token},json={
       'name':'РусланТест',
    'photo':'https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png'
})

response_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
print(response_json)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    'pokemon_id': 2858,
    'name': 'РусланТест2',
    'photo': ''
})

response_json2 = json.dumps(response_put.json(), indent=4, ensure_ascii=False)
print(response_json2)


response_pokeball= requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token': token}, json={
    'pokemon_id': '2859'
})

response_json3 = json.dumps(response_pokeball.json(), indent=4, ensure_ascii=False)
print(response_json3)