#Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

def remove_repetidos(lista1, lista2):
    lista3 = []
    for i in lista1:
        if not e_repetido(lista3, i):
            lista3.append(i)
    for i in lista2:
        if not e_repetido(lista3, i):
            lista3.append(i)
    return lista3

def e_repetido(lista, elemento):
    for i in lista:
        if i == elemento:
            return True
    return False

lista1 = [0, 8, 7, 6 , 6, 10, 11]
lista2 = [0, 8, 7, 6 , 6, 10, 11, 33, 34, 5, 6, 66, 77, 78, 67]
lista3 = remove_repetidos(lista1, lista2)

if len(lista3) != 0:
    print(lista1)
    print(lista2)
    print("Lista 3 sem elementos repetidos:")
    print(lista3)
else:
    print("Listas zeradas")
