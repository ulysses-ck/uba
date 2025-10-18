# 3. Se representa un ticket de supermercado como una lista de diccionarios, donde cada diccionario tiene
# la siguiente información:
# ● Nombre del producto
# ● Precio por unidad
# ● Cantidad
# Se pide hacer una función que reciba el ticket y devuelva el monto total a pagar.

from typing import TypedDict, List

class Shop(TypedDict):
    name: str
    price_pu: int
    quantity: int

def total_shop(ls: List[Shop]):
    total = 0

    for i in ls:
        total += i["price_pu"] * i["quantity"]

    return total


ticket_ejemplo: List[Shop] = [
    {
        "name": "Leche",
        "price_pu": 120,
        "quantity": 2
    },
    {
        "name": "Pan",
        "price_pu": 85,
        "quantity": 1
    },
    {
        "name": "Huevos",
        "price_pu": 15,
        "quantity": 12
    },
    {
        "name": "Manzanas",
        "price_pu": 50,
        "quantity": 3
    }
]

monto_total = total_shop(ticket_ejemplo)

print(ticket_ejemplo)
print(f"\nEl monto total a pagar es: {monto_total}")