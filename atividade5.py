'''A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T =
[-10,-9,0,1,2,5,-2,-4]. Faça um programa que imprima a menor e a maior temperatura, assim
como a temperatura média, usando funções.'''

def menor(lista):
    if len(lista) != 0:
        menor = 0
        for i in range(0, len(lista)):
            if lista[i] <= menor:
                menor = lista[i]
        return menor

def maior(lista):
    if len(lista) != 0:
        maior = lista[0]
        for i in range(0, len(lista)):
            if lista[i] >= maior:
                maior = lista[i]
        return maior

def media(lista):
    if len(lista) != 0:
        soma = 0
        for i in range(0, len(lista)):
            soma += lista[i]
        media = soma / len(lista)
        return media
    
lista = [-10,-9,0,1,2,5,-2,-4]
maior(lista)
menor(lista)
media(lista)
if len(lista) != 0:
    if maior(lista) == menor(lista):
        print(f"a maior {maior(lista)} e menor {menor(lista)} temperatura são iguais, e a media de temperatura foi {media(lista)}°C")
    else:
        print(f"A menor temperatura é {menor(lista)}°C e a maior é {maior(lista)}°C, e a media de temperatura foi {media(lista)}°C")
else:
    print("lista zerada")
