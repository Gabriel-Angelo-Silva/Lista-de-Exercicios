'''Crie um programa que inverta a ordem das linhas do arquivo pares.txt. A primeira linha
deve conter o maior número; e a última, o menor.'''

with open("pares.txt", "w") as pares:
    for n in range(0, 1001):
        if n % 2 == 0:
            pares.write(f"{n}\n")

def inverte_ordem():
    with open("pares.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    linhas_invertidas = []
    for i in range(len(linhas) - 1, -1, -1):
        linhas_invertidas.append(linhas[i])

    with open("pares.txt", "w") as arquivo:
        arquivo.writelines(linhas_invertidas)

inverte_ordem()
