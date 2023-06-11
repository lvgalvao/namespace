from typing import Callable, List, Any

dataset = [
    {"nome": "Pikachu", "tipo": "Elétrico", "altura": 0.4, "peso": 6.0},
    {"nome": "Charmander", "tipo": "Fogo", "altura": 0.6, "peso": 8.5},
    {"nome": "Squirtle", "tipo": "Água", "altura": 0.5, "peso": 9.0},
    {"nome": "Golden", "tipo": "Água", "altura": 0.2, "peso": 2.0}
]

# Funções de processamento para extrair estatísticas

def get_altura(pokemon: dict) -> float:
    return pokemon['altura']

def get_peso(pokemon: dict) -> float:
    return pokemon['peso']

def get_tipo(pokemon: dict) -> str:
    return pokemon['tipo']

# Função de mapeamento

def mymap(f: Callable[[dict], Any], l: List[dict]) -> List[Any]:
    return [f(x) for x in l]

def mysum(numeros: List[float]) -> float:
    soma = 0.0
    for numero in numeros:
        soma += numero
    return soma

def mylen(numeros: List[Any]) -> int:
    count = 0
    for _ in numeros:
        count += 1
    return count

def meu_append(lista: List[Any], numero: Any) -> List[Any]:
    nova_lista = lista + [numero]
    return nova_lista

def criar_conjunto_unico(lista: List[Any]) -> List[Any]:
    conjunto: List[Any] = []  # Adicionando a anotação de tipo para a variável "conjunto"
    for elemento in lista:
        if elemento not in conjunto:
            conjunto = meu_append(conjunto, elemento)
    return conjunto

lista_de_alturas: list = mymap(get_altura, dataset)
lista_de_pesos: list = mymap(get_peso, dataset)
lista_de_tipos: list = mymap(get_tipo, dataset)

# Calcular estatísticas a partir dos resultados

altura_media: float = mysum(lista_de_alturas) / mylen(lista_de_alturas)
peso_medio: float = mysum(lista_de_pesos) / mylen(lista_de_pesos)
todos_os_tipos: List[Any] = criar_conjunto_unico(lista_de_tipos)  # Adicionando a anotação de tipo para a variável "todos_os_tipos"

print("Altura média dos Pokémon:", altura_media)
print("Peso médio dos Pokémon:", peso_medio)
print("Todos os tipos: ", todos_os_tipos)
