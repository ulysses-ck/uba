"""
Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
● la suma de ambos números
● la resta de ambos números
● la multiplicación de ambos números
● la división entera de ambos números
● el resto
Más adelante podríamos crear nuestra propia calculadora :)
"""

num_1 = int(input("Ingrese el número 1: "))
num_2 = int(input("Ingrese el número 2: "))

sum = num_1 + num_2
minus = num_1 - num_2
product = num_1 * num_2
division = num_1 / num_2
rest = num_1  % num_2

print(f"Suma: {num_1} + {num_2} = {sum}")
print(f"Resta: {num_1} - {num_2} = {minus}")
print(f"Producto: {num_1} * {num_2} = {product}")
print(f"División: {num_1} / {num_2} = {division}")
print(f"Resto: {num_1} % {num_2} = {rest}")