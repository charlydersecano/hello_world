import requests
import random

gente_max = 82

random_id = random.randint(1, gente_max)

personajes = requests.get(f'https://swapi.dev/api/people/{random_id}/')
datos_personaje = personajes.json()
print(datos_personaje.get('name',f'This {random_id} is not associated with any person'))