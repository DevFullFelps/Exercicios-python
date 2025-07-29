#Exercicio 04
#Faça um programa que peça as 4 notas bimestrais e mostre a média.

aluno = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float (input('Digite a segunda nota: '))
nota3 = float (input('Digite a terceira nota: '))
nota4 = float (input('Digite a quarta nota: '))
somatoria = nota1 + nota2 + nota3 + nota4
media = somatoria / 4

print(f'Notas do {aluno}')
print('_________________')
print(f'1° bimestre: {nota1}')
print(f'2° bimestre: {nota2}')
print(f'3° bimestre: {nota3}')
print(f'4° bimestre: {nota4}')
print(f'A média do {aluno} é {media}')
print('_________________')