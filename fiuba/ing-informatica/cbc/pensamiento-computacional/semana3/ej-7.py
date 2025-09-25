# 7. Se tienen letras para representar las estaciones del año:
# ● V para verano
# ● O para otoño
# ● I para invierno
# ● P para primavera
# Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es
# decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a
# ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O,
# B, V e I.

def show_station(char: str):
    if char == "V":
        return "VERANO. good"
    elif char == "O":
        return "OTOÑO. meh"
    elif char == "I":
        return "INVIERNO. bad"
    elif char == "P":
        return "PRIMAVERA. very good"
    else: 
        return "error"
    
tests = "A,P,O,B,V,I".split(",")
for i in tests:
    print(f"{i}: {show_station(i)}")
