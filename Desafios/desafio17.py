#  faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo, calcule e mostre o comprimento da hipotenusa.

import math

cateto_oposto = float(input('Qual o tamanho do cateto oposto? '))
cateto_adjacente = float(input('Qual o tamanho do cateto adjacente? '))


elevadoOposto = cateto_oposto * cateto_oposto
elevadoAdjacente = cateto_adjacente * cateto_adjacente
elevadoFinal = elevadoAdjacente + elevadoOposto


# print(elevadoOposto)
# print(elevadoAdjacente)
print(f'a hipotenusa vai medir {math.sqrt(elevadoFinal) :.2f}')

