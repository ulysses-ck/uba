"""
Crear una función que una un string y un entero, ambos dentro de un string.
"""
def concatenate_int_string(string: str, num: int):
    return f"{string}{num}"

print(concatenate_int_string("e", 42))