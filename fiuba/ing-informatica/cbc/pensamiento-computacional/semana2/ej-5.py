"""
Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos.
Es muy común usar variables para acumular valores.
"""
sum = 0
for i in range(1, 6):
    num = int(input(f"Escribe el entero nro° {i}: "))
    sum += num

print(f"El promedio es de {sum / 5}")

