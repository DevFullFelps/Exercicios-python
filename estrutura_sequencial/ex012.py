#Exercício 12
#Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula: Gigabytes * 1024

print('Conversão')
arq_gb = int(input('Quantidade em Gigabytes: '))
arq_mg = arq_gb * 1024
print(f'{arq_gb}Gb equivalem à {arq_mg}Mb')