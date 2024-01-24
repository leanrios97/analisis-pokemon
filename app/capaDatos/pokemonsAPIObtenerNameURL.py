import requests

class PokemonsAPIObtenerNameURL:
    
    def obtenerPokemons(self, CantPokemon_get):
        # CantPokemon_get = 1025
        url = f"https://pokeapi.co/api/v2/pokemon?limit={CantPokemon_get}&offset=0"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            pokemons = data['results']
            return pokemons
        else: 
            raise ValueError(f'Error al realizar la solicitud: {response.status_code}')
    
    def extract_info(self, data):
        raise NotImplementedError("Las subclases deben implementar este método.")
    
    def get_pokemon_info(self, resource_id):
        data = self.fetch_data(resource_id)
        return self.extract_info(data)
    
if __name__ == '__main__':
    pokemonsClass = PokemonsAPIObtenerNameURL()
    pokemons = pokemonsClass.obtenerPokemons(151)
    
    for pokemon in pokemons:
        print(pokemon)