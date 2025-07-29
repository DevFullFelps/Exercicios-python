#Exercício 09
#Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

print('Conversor de temperatura')
g_fah = float(input('Digite os graus em Fahrenheit: '))
g_cel = 5 * ((g_fah-32)/9)
print(f'{g_fah}°F equivalem a {g_cel}°C')