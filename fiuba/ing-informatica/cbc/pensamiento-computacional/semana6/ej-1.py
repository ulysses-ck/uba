# 1. En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener
# mejor organizado sus datos.
# a. Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las
# características que se consideren más relevantes para identificar a una persona (su nombre,
# DNI, edad, etc).
# b. Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso
# del estudiante y sus características (año, división, orientación, etc).
# c. Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad
# e imprimirla por pantalla.

students = [
    {
        "name": "Chadberto",
        "age": 66,
        "dni": 12345678,
        "subject": {
            "age": 66,
            "division": "A",
            "orientation": "Abogacía"
        }
    },
    {
        "name": "Chadzza",
        "age": 21,
        "dni": 45678901,
        "subject": {
            "age": 22,
            "division": "B",
            "orientation": "Abogacía"
        }
    },
    {
        "name": "Ricardo",
        "age": 34,
        "dni": 98765432,
        "subject": {
            "age": 19,
            "division": "A",
            "orientation": "Arquitectura"
        }
    },
    {
        "name": "Maria",
        "age": 45,
        "dni": 23456789,
        "subject": {
            "age": 21,
            "division": "C",
            "orientation": "Ingeniería"
        }
    },
    {
        "name": "Juan",
        "age": 50,
        "dni": 56789012,
        "subject": {
            "age": 20,
            "division": "B",
            "orientation": "Diseño Gráfico"
        }
    },
    {
        "name": "Laura",
        "age": 28,
        "dni": 34567890,
        "subject": {
            "age": 23,
            "division": "C",
            "orientation": "Psicología"
        }
    },
    {
        "name": "Felipe",
        "age": 30,
        "dni": 67890123,
        "subject": {
            "age": 20,
            "division": "A",
            "orientation": "Economía"
        }
    }
]

max = 0
idx = 0

for i, s in enumerate(students):

    if s["age"] >= max:
        max = s["age"]
        idx = i


print(students[idx]["name"])