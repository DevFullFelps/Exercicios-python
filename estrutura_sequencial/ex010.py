#Exercício 10
#Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print('Conversor de temperatura')
g_cel = float(input('Digite os graus em Celcius: '))
g_fah = (g_cel * 9/5) + 32
print(f'{g_cel}°C equivalem a {g_fah}°F')