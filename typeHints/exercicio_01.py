# Função chamada dobro para mostrar map

def dobro(numero: int) -> int:
    return numero * 2

lista = [2,5,7,23,56]
lista_apos_dobro = map(dobro,lista)
print(list(lista_apos_dobro))

# Função para encontrar os números pares usanfo filter

def pares(numero: int) -> bool:
    return numero % 2 == 0

lista_somente_pares = filter(pares, lista)
print(tuple(lista_somente_pares))