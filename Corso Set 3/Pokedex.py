import json
import os
import requests
from random import randrange, random

# ----------  LE TUE FUNZIONI  -------------------------------------------------

from random import randrange
import requests

def ricerca_pokemon():

    try:
        num = randrange(1, 1025)

        pokemon_url  = f"https://pokeapi.co/api/v2/pokemon/{num}"
        species_url  = f"https://pokeapi.co/api/v2/pokemon-species/{num}"

        pok_resp = requests.get(pokemon_url,  timeout=8)
        spe_resp = requests.get(species_url, timeout=8)
        pok_resp.raise_for_status()
        spe_resp.raise_for_status()

        pokemon_data  = pok_resp.json()
        species_data  = spe_resp.json()

        nome = pokemon_data["forms"][0]["name"].capitalize()
        print(f"È apparso un {nome} selvatico!")

        return pokemon_data, species_data["capture_rate"]

    except requests.RequestException as e:
        print("Errore nella richiesta alla PokeAPI:", e)
    except (KeyError, ValueError) as e:
        print("Errore nei dati ricevuti:", e)
    return None, None



POKEDEX_FILE = "pokedex.json"

def leggi_pokedex(path: str = POKEDEX_FILE) -> dict:

    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4, ensure_ascii=False)
        print(" Creato nuovo pokedex.json ")
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Errore")
        return {}

def salva_pokedex(pokedex: dict, path: str = POKEDEX_FILE) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(pokedex, f, indent=4, ensure_ascii=False)
    except OSError as e:
        print("Errore nel salvataggio del Pokédex:", e)


def presente_in_pokedex(pokedex: dict, pokemon) -> bool:
    if isinstance(pokemon, int):
        poke_id = str(pokemon)
    elif isinstance(pokemon, dict):
        poke_id = str(pokemon.get("id"))
    else:
        raise TypeError("Il parametro 'pokemon' deve essere un int o un dict.")

    return poke_id in pokedex


def cattura_pokemon(Pokemon, catch_rate, poke_ball,pokedex):
    while poke_ball >0:
        ac = input("Vuoi usare una poké ball, esca, pantano oppure fuggire? (1 per poké ball, 2 per esca, 3 per pantano, 0 per no): ")
        probabilita_cattura = catch_rate/255
        probabilita_fuga = 0.15
        if ac == "1":
            if randrange(256) < probabilita_cattura:
                poke_id = str(Pokemon["id"])
                pokedex[poke_id] = {
                    "nome": Pokemon["name"],
                    "abilità": [ab["ability"]["name"] for ab in Pokemon["abilities"]],
                    "xp": Pokemon["base_experience"],
                    "peso": Pokemon["weight"],
                    "altezza": Pokemon["height"],
                }
                salva_pokedex(pokedex)
                print("Successo! Pokémon aggiunto al Pokédex.")
                poke_ball -=1
                break
            elif random() < probabilita_fuga:
                print("Oh no! Il Pokémon è fuggito.")
                poke_ball -=1
                break
        elif ac == "2":
            print("Hai lanciato un'esca!")
            probabilita_fuga -= 0.05
            probabilita_cattura = catch_rate/255 * 0.9
            if random() < probabilita_fuga:
                print("Oh no! Il Pokémon è fuggito.")
                break

        elif ac == "3":
            print("Hai lanciato pantano!")
            probabilita_fuga += 0.05
            probabilita_cattura = catch_rate/255 * 1.1
            if random() < probabilita_fuga:
                print("Oh no! Il Pokémon è fuggito.")
                break

        elif ac == "0":
            print("Scampato pericolo!")
            break


# ----------  MAIN  ------------------------------------------------------------
def main():
    leggi_pokedex()


# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
