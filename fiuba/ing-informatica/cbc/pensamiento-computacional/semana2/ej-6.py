"""
Crear una función que reciba un número y muestre el anterior y el siguiente.
"""
def next_and_before(num: int):
    print(f"Anterior de {num}: {num-1}")
    print(f"Siguiente de {num}: {num+1}")

next_and_before(10)