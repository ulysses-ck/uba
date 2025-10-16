import os

n_files = int(input("Cantidad de archivos a crear: "))
folder = input("Carpeta a crear: ")

for i in range(n_files):
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"Se creó la carpeta '{folder}'.")
    else:
        print(f"La carpeta '{folder}' ya existe.")

    file_path = f"./{folder}/ej-{i+1}.py"

    with open(file_path, "w") as f:
        print(f"Se creó el archivo: '{file_path}'")
