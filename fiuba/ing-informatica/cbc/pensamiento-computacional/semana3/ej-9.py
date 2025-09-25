# 9. Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior. Ahora se
# necesita una funcionalidad que permita a los niños aprender las tablas. Crear una función que reciba un
# número entero e imprima por pantalla la tabla de ese número del 1 al 10.

def print_table(num: int):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")


print_table(5)