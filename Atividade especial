'''Defina em Python uma função recursiva que recebe como argumento uma
lista de listas de números inteiros e devolve True se todas as listas em verificam a
propriedade de mais de metade dos seus elementos serem 0 e False em caso contrário. Por
exemplo, no caso da lista [[0,0,3,0],[0,5,0],[0,0,0]] a função deve devolver True pois em
todas as listas mais de metade dos elementos são 0. Pode, se achar conveniente, definir
funções auxiliares desde que sejam funções recursivas.'''

def mais_da_metade_zeros(lista):
    if len(lista) == 0:
        return True
    primeira_lista = lista[0]
    if mais_zeros(primeira_lista):
        return mais_da_metade_zeros(lista[1:])
    else:
        return False

def mais_zeros(sublista):
    if len(sublista) == 0:
        return True
    if sublista[0] == 0:
        return mais_zeros(sublista[1:])
    else:
        return False

lista = [[0, 0, 3, 0], [0, 5, 0], [0, 0, 0]]
if len(lista) != 0:
    resultado = mais_da_metade_zeros(lista)
    print(resultado)
else:
    print("lista zerada")
