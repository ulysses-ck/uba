"""
8.
    a. Crear una función que reciba dos enteros y que retorne (devuelva) el resto de la división.
    b. Crear una función que reciba dos enteros y que retorne (devuelva) el cociente.
"""
def rest(num_1: int, num_2: int):
    return num_1 % num_2

def quotient(num_1: int, num_2: int):
    return num_1 / num_2

print(f"Resto de 5 y 2: {rest(5, 2)}")
print(f"División de 5 y 2: {quotient(5, 2)}")