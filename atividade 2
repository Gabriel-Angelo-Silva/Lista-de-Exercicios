'''Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou
iguais, de 15%.'''


salario = float(input("digite o seu salario: "))
if salario > 1250:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f"Seu salario de R${salario}, teve um aumento de R${aumento} ou 10% de aumento, tendo o novo valor de R${novo_salario}")
elif salario > 0 and salario <= 1250:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"Seu salario de R${salario}, teve um aumento de R${aumento} ou 15% de aumento, tendo o novo valor de R${novo_salario}")
else:
    print(f"{salario} Salario menor ou igual a zero")
