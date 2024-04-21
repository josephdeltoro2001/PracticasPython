from geometria.areas import *
from geometria.perimetros import *

# Ejemplos de uso de las funciones
lado_cuadrado = 60
base_triangulo = 10
altura_triangulo = 21
radio_circulo = 14

#Lados perímetro triángulo
lado1_triangulo = 10
lado2_triangulo = 15
lado3_triangulo = 51

#Áreas
print("Áreas")
print(f"Área del cuadrado con lado {lado_cuadrado} es: {area_cuadrado(lado_cuadrado)}")
print(f"Área del triángulo con base {base_triangulo} y altura {altura_triangulo} es: {area_triangulo(base_triangulo, altura_triangulo)}")
print(f"Área del círculo con radio {radio_circulo} es: {area_circulo(radio_circulo)}")

#Perímetros
print("\nPerímetros")
print(f"Perímetro del cuadrado con lado {lado_cuadrado} es: {perimetro_cuadrado(lado_cuadrado)}")
print(f"Perímetro del triángulo con lados {lado1_triangulo}, {lado2_triangulo} y {lado3_triangulo} es: {perimetro_triangulo(lado1_triangulo, lado2_triangulo, lado3_triangulo)}")
print(f"Perímetro del círculo con radio {radio_circulo} es: {perimetro_circulo(radio_circulo)}")