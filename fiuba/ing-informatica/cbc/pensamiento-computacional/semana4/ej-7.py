# 7. Se pide ahora crear 3 tuplas como las del ejercicio 5, con un nombre y una edad. A continuación,
# guardarlas en una lista. Pensar, ¿De que nos servirá guardar las tuplas en una lista en vez de tenerlas
# por separado?

persons = []

for i in "abc":
    persons.append((i, ord(i)))

print(persons)

# para poder tener una estructura de datos más homogenea y que luego pueda ser reutilizada