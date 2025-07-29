#Exercício 15
#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

ir = 11
inss = 8
sindicato = 5

print('Folha de pagamento')
v_hora = float(input('Valor por hora: '))
h_trab = float(input('Horas trabalhadas: '))
sal_bruto = v_hora * h_trab

v_ir = (sal_bruto * ir) / 100
v_inss = (sal_bruto * inss) / 100
v_sind = (sal_bruto * sindicato) / 100

descontos = v_ir + v_inss + v_sind
sal_liq = sal_bruto - descontos

print(f'+ Salário Bruto: R${sal_bruto:.2f}')
print(f'- IR ({ir}%): R${v_ir:.2f}')
print(f'- INSS({inss}%): R${v_inss:.2f}')
print(f'- Sindicato({sindicato}%): R${v_sind:.2f}')
print(f'= Salário Liquido: R${sal_liq:.2f}')