'''Escreva um programa que recebe duas listas encadeadas de inteiros e efetue os seguintes
passos:
a) Verifique se as listas estão ordenadas;
b) Ordene as listas, caso não estejam ordenadas;
c)Mescle os elementos da segunda lista na primeira, mantendo a ordenação na lista final.'''

def check(lista):
    check = True
    i = 0
    while check and i != len(lista) - 1:
        if lista[i] > lista[i + 1]:
            check = False
        i += 1
    return check

def ordena(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

lista = [0, 5, 6, 7, 4]
lista2 = [0, -1, 1, 5, 6]
ordena(lista)
ordena(lista2)
lista += lista2

if (len(lista) != 0):
    ordena(lista)
    print(lista)
else: 
    print("lista vazia")
