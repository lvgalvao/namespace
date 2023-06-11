from typing import Callable

dataset = [
    {"nome": "Pikachu", "tipo": "Elétrico", "altura": 0.4, "peso": 6.0},
    {"nome": "Charmander", "tipo": "Fogo", "altura": 0.6, "peso": 8.5},
    {"nome": "Squirtle", "tipo": "Água", "altura": 0.5, "peso": 9.0},
    {"nome": "Golden", "tipo": "Água", "altura": 0.2, "peso": 2.0}

]

# Funções de processamento para extrair estatísticas

def get_altura(pokemon: dict):
    return pokemon['altura']

def get_peso(pokemon: dict):
    return pokemon['peso']

def get_tipo(pokemon: dict):
    return pokemon['tipo']

# Função de mapeamento

# Aplicar as funções de processamento usando mymap

# map

def mymap(f: Callable,l: list) -> list:
    return [f(x) for x in l]

def mysum(numeros: list) -> int:
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

def mylen(numeros: list) -> int:
    count = 0
    for _ in numeros:
        count += 1
    return count

def meu_append(lista: list, numero: int) -> list:
    nova_lista = lista + [numero]
    return nova_lista

def criar_conjunto_unico(lista: list) -> list:
    conjunto: list = []
    for _ in lista:
        if _ not in conjunto:
            conjunto = meu_append(conjunto, _)
    return conjunto

lista_de_alturas = mymap(get_altura, dataset)
lista_de_pesos = mymap(get_peso, dataset)
lista_de_tipos = mymap(get_tipo, dataset)

# Calcular estatísticas a partir dos resultados

altura_média = mysum(lista_de_alturas) / mylen(lista_de_alturas)
peso_médio = mysum(lista_de_pesos) / mylen(lista_de_pesos)
todos_os_tipos = criar_conjunto_unico(lista_de_tipos)

print("Altura média dos Pokémon:", altura_média)
print("Peso médio dos Pokémon:", peso_médio)
print("Todos os típos: ", todos_os_tipos)