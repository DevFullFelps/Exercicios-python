#Exercício 13
#Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

#Para Megabytes: Gigabytes * 1024
#Para Kilobytes: Gigabytes * 1024 * 1024
#Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.

quant_Mb = 1024
quant_Kb = 1024 * 1024
print('Conversão')
arq_Gb = int(input('Digite o tamanho em Gigabyte: '))
arq_Mb = arq_Gb * quant_Mb
arq_Kb = arq_Gb * quant_Kb
print(f'{arq_Gb}Gb equivalem a {arq_Mb}Mb e {arq_Kb}Kb')