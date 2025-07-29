#Exercício 14
#João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

reg_SP_kg = 50
multa_kg = 4

print('Microcomputador do João')
kg_peixe = float(input('Insira a quantidade em Kg de peixes pescados: '))
if kg_peixe > reg_SP_kg:
    excesso = kg_peixe - reg_SP_kg
    multa = excesso * multa_kg
    print(f'João, lamento... Você pescou {kg_peixe}kg de peixe, porém o limite pelo regulamento de São Paulo é {reg_SP_kg}kg')
    print(f'Você excedeu {excesso}kg. Para continuar com os peixes deverá pagar uma multa de R${multa}')
else:
    print(f'João, não terá problemas com o regulamento. O máximo de acordo com o regulamento de São Paulo é de {reg_SP_kg}kg')
    print(f'Porém, você trouxe apenas {kg_peixe}kg')