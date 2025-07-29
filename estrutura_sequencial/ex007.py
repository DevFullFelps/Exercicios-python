#Exercício 07
#Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input('Digite o comprimento: '))
area = lado ** 2
d_area = area * 2

print(f'Em um quadrado, aonde o lado tem {lado}cm ')
print(f'A área desse quadrado equivale à {area}cm')
print(f'O dobro dessa área é {d_area}cm')