"""
Crear un programa que le solicite al usuario un entero y determine si es par, mostrando por pantalla un
mensaje que indique el resultado.
Para determinar si un número es par o impar, se puede determinar con el uso del operador %, les
dejamos a ustedes el cómo.
"""

num_user = int(input("Ingrese un número entero: "))

is_even = "par" if num_user % 2 == 0 else "impar"

print(f"El número: {num_user} es {is_even}")