# faça um programa que leia um angulo e mostre seu seno, cosseno e tangente
import math

angulo = int(input('Digite um angulo? '))

# Converte o ângulo para radianos
angulo_radianos = math.radians(angulo)

# Calcula seno, cosseno e tangente
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f'o seno de {angulo} tem {math.sin(angulo_radianos) :.2f}')
print(f'o cosseno de {angulo} tem {math.cos(angulo_radianos) :.2f}')
print(f'A tangente de {angulo}° é {tangente :.2f}')
