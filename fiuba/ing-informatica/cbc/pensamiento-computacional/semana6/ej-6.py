# 6. En una fábrica, se hace un chequeo de calidad a los productos antes de cada entrega. El resultado del
# chequeo de la entrega se guarda en una lista de diccionarios, donde cada diccionario tiene la siguiente
# información de cada producto:
# ● Código del producto
# ● Fecha de vencimiento
# ● Si pasó el chequeo de calidad o no
# Se pide hacer una función que reciba esta lista de diccionarios y elimine todos los productos que no
# pasaron el chequeo de calidad. Devolver en una tupla el diccionario con los elementos eliminados y la
# cantidad de elementos que quedaron en el diccionario.
# Dado que la tupla es inmutable y nosotros no podemos ir agregando elementos a una tupla, ¿En qué
# momento deberíamos crear la tupla?

# rta: lo creas al final, y convertis la lista a una tupla

from typing import Tuple, TypedDict, List

class Product(TypedDict):
    code: int
    exp_date: str
    is_qual: bool

def delete_not_qual(ls: List[Product]) -> Tuple[Tuple[Product], int]:
    ls_not_qual: List[Product] = []
    ls_qual: List[Product] = []

    for i in ls:
        if(not i["is_qual"]):
            ls_not_qual.append(i)
        else:
            ls_qual.append(i)

    ls[:] = ls_qual

    result = (
        ls_not_qual,
        len(ls_qual)
    )

    return result

delivery_check: List[Product] = [
    {
        "code": 1001,
        "exp_date": "2024-12-01",
        "is_qual": True 
    },
    {
        "code": 1002,
        "exp_date": "2023-11-15",
        "is_qual": False 
    },
    {
        "code": 1003,
        "exp_date": "2025-01-20",
        "is_qual": True 
    },
    {
        "code": 1004,
        "exp_date": "2024-06-10",
        "is_qual": False 
    },
    {
        "code": 1005,
        "exp_date": "2024-09-05",
        "is_qual": True 
    }
]

delivery_original_copy = delivery_check[:]

resultado_chequeo = delete_not_qual(delivery_check)

print("--- Chequeo de Calidad ---")
print("Lista Original de Productos:")
print(delivery_original_copy)

print("\nResultado de la Función (Tupla):")
productos_eliminados, cantidad_restante = resultado_chequeo

print(f"Productos Eliminados (No Pasaron): {productos_eliminados}")
print(f"Cantidad de Productos que Quedaron (Aptos): {cantidad_restante}")

print("\nLista Original DESPUÉS de ejecutar la función (solo Aptos):")
print(delivery_check)