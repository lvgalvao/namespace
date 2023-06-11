def soma_1(x: int) -> int:
    return x + 1

def mymap(f, l):
    return (f(x) for x in l)

def get_info(pokemon_name):
    if pokemon_name == "Pikachu":
        return "Pikachu é um Pokémon elétrico muito fofo!"
    elif pokemon_name == "Charmander":
        return "Charmander é um Pokémon de fogo com uma chama na cauda!"
    elif pokemon_name == "Squirtle":
        return "Squirtle é um Pokémon de água com uma conchinha nas costas!"

pokemons = ["Pikachu", "Charmander", "Squirtle"]

fases_2 = map(get_info, pokemons)
print(fases_2.__reduce__())
print(fases_2.__next__())

