# How to connect an API using Python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    # print(response)
    if response.status_code == 200:
        # print("Data retrieved !")
        # pokemon_data = response.json()
        return response.json()

    else:
        print(f"Failed to retrieve data. Error {response.status_code}")

pokemon_name = "qwilfish"
pokemon_info = get_pokemon_info(pokemon_name)


if pokemon_info:
    print(f"Name : {pokemon_info["name"].capitalize()}")
    print(f"id : {pokemon_info["id"]}")
    print(f"abilities : {pokemon_info["abilities"]}")
    print(f"height : {pokemon_info["height"]}")
    print(f"weight : {pokemon_info["weight"]}")