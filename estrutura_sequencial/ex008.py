#Exercício 08
#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print('Registro de salário')
v_hora = float(input('Valor por hora: '))
h_trabalho = float(input('Quantidade de horas de trabalho no mês: '))
salario = v_hora * h_trabalho
print(f'Seu salário nesse mês foi de: {salario}R$')