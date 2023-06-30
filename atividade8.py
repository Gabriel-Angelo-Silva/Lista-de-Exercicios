'''Crie um programa que imprima as linhas de um arquivo. Esse programa deve receber três
parâmetros pela linha de comando: o nome do arquivo, a linha inicial e a última linha a
imprimir.'''

import sys

if len(sys.argv) != 4:
    print("Uso: python programa.py nome_arquivo linha_inicial linha_final")
    sys.exit(1)

nome_arquivo = sys.argv[1]
linha_inicial = int(sys.argv[2])
linha_final = int(sys.argv[3])

with open(nome_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()
    total_linhas = len(linhas)
    
    if linha_inicial < 1 or linha_final > total_linhas or linha_inicial > linha_final:
        print("Linhas inválidas.")
        sys.exit(1)
    
    for i in range(linha_inicial, linha_final+1):
        print(linhas[i], end="")
