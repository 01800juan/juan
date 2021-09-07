import requests
#
#Script en python que consulta la api de pokemon
#para listar los nombres de pokemon pero se lo agrego
#una funcion para que tuviera interaccion.
if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon form/'

    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results',[])

        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)

        next = input("'¿continuar listando?' [Y/N]").lower()
        if next = y
            get_pokemons(offset=offset+20)
if __name__ == '__main__':
    get_pokemons()
