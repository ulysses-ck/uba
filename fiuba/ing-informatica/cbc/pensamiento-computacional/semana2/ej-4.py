"""
Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía
el usuario en el año ingresado.
"""
user_age = int(input("Ingrese año de nacimiento"))
other_age = int(input("Ingrese otro año"))

remainder = other_age - user_age

print(f"Tu edad en el año {other_age} era de {remainder}")