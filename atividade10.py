'''Escreva um programa que solicite ao usuário uma sequência de caracteres sem limite de
máximo de tamanho e realize as seguintes operações usando uma pilha:
a) Imprimir o texto na ordem inversa;
b) Verificar se o texto é um palíndromo, ou seja, se a string é escrita da mesma maneira de
frente para trás e detrás para frente. Ignore espaços e pontos.'''

def inverter_texto(texto):
    pilha = []
    for char in texto:
        pilha.append(char)
    texto_invertido = ""
    while len(pilha) > 0:
        texto_invertido += pilha.pop()
    return texto_invertido

texto = input("Digite uma sequência de caracteres: ")

texto_invertido = inverter_texto(texto)
if len(texto) != 0: 
    print("Texto invertido:", texto_invertido)
    if texto == texto_invertido:
        print("O texto é um palíndromo.")
    else:
        print("O texto não é um palíndromo.")
else:
    print("Texto Vazio")
