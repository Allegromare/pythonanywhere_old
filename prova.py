# 1. Import libraries
import requests, json


f = requests.get('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json')

print(type(f))

superHeroSquad = f.json()
print(type(superHeroSquad))

print(superHeroSquad.keys())
