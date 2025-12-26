import requests  # type: ignore

def fetch_pokemon_abilities(base_url, poke, headers):
    try:
        response = requests.get(
            base_url + poke,
            headers=headers,
            timeout=10
        )

        # Raises error for 4xx / 5xx responses
        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        print("❌ Request timed out. Please try again.")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"❌ Pokémon '{poke}' not found.")
        else:
            print(f"❌ HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")

    return None


base_url = "https://pokeapi.co/api/v2/pokemon/"
pokemon = input("Enter pokemon name: ").lower()

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

print(f"\nThese are the abilities of {pokemon}")

data = fetch_pokemon_abilities(base_url, pokemon, headers)

if data:
    for ability in data["abilities"]:
        print("-", ability["ability"]["name"])
