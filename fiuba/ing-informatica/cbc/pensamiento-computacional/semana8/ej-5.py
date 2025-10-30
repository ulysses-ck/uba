# 5. Se tiene un archivo csv que contiene información sobre el stock de una librería. Se guarda por cada
# línea, el nombre del producto, el código, el precio por unidad y el stock actual, es decir:
# nombre;código;precio;stock
# Un posible ejemplo de este archivo es el siguiente:
# lapiceras;34512;50;120
# cuadernos;41611;500;130
# sacapuntas;62812;30;210
# Se pide:
# a. Leer el archivo y mostrarlo por pantalla con el siguiente formato:
# Nombre producto: lapiceras
# Código producto: 34512
# Precio por unidad: 50
# Stock: 120
# Nombre producto: cuadernos
# Código producto: 41611
# Precio por unidad: 500
# Stock: 130
# b. Hacer una función que reciba un diccionario que describa una línea del archivo y lo
# agregue, es decir que si se recibe un diccionario del tipo:
# {
# “nombre”: “hojas A4”,
# “código”: 35662,
# “precio”: 600,
# “stock”: 45
# }

from typing import TypedDict, List



# a

def print_info(path):
    with open(file=path, mode="r") as file:
        content = file.readlines()

        for i in content:
            name, code, price, stock = i.split(";")
            print(f"Nombre: {name}")
            print(f"Código: {code}")
            print(f"Precio: {price}")
            print(f"Stock: {stock}")


# b

class Product(TypedDict):
    name: str
    code: int
    price: int
    stock: int

def add_new_prod(data: Product, path: str):
    with open(file=path, mode="a") as file:
        new_prod = f"\n{data["name"]};{data["code"]};{data["price"]};{data["stock"]}"
        file.writelines(new_prod)


path="stock.csv"
print_info(path)

add_new_prod({
"code": 123,
"name": "nuevo prod",
"price": 123,
"stock": 1
}, path)

print_info(path)