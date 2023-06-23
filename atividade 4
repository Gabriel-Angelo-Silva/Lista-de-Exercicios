'''Faça um programa que recebe três números do usuário, e identifica o maior através de
uma função e o menor número através de outra função.'''

def menor(a,b,c):
    if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return b
    if c <= a and c <= b:
        return c

def maior(a,b,c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= a and c >= b:
        return c
a = float(input("digite um numero: "))
b = float(input("digite um numero: "))
c = float(input("digite um numero: "))
maior(a,b,c)
menor(a,b,c)
if menor(a,b,c) == maior(a,b,c):
    print("são iguais")
else:
    print(f"o menor é {menor(a,b,c)} e o maior foi {maior(a,b,c)}")
