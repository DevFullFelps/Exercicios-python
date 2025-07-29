#Exercício 11
#Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

#O produto do dobro do primeiro com metade do segundo .
#A soma do triplo do primeiro com o terceiro.
#O terceiro elevado ao cubo.

x1 = int(input('Valor 1: '))
x2 = int(input('Valor 2: '))
z3 = float(input('Valor 3: '))

q1 = (x1*2) * (x2/2)
q2 = (x1*3) + z3
q3 = z3**3

print(f'O produto do dobro do {x1} com a metade do {x2}: {q1}')
print(f'A soma do triplo do {x1} com o {z3}: {q2}')
print(f'O {z3} elevado ao cubo: {q3}')