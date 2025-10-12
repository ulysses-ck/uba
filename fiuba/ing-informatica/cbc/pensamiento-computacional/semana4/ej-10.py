# 10. Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos
# números elevados al cuadrado.

a = list(range(1,11))
b = []
for i in a:
    b.append((i ** 2))

print(a)
print(b)