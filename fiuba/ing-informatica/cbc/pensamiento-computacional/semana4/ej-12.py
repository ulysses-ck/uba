""""
12. Se quiere hacer un sistema en la facultad para que un alumno pueda ir guardando las materias que va
haciendo. Para eso, crear una función que le pregunte al usuario la materia que quiere almacenar, e ir
guardando la información en una lista hasta que ingrese una ‘X’. ¿Qué funciones de listas no permiten
insertar en una lista?

Rta: todas a excepción de extend, append e insert
"""

def ask_subjects():
    subjects = []

    print("ingresa 'X' para terminar el programa")

    while True:
        curr_subject = input("Poné una materia: ")

        if(curr_subject == "X"):
            break

        subjects.append(curr_subject)

    return subjects

print(ask_subjects())
