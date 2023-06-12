import os

def listar_ficheros(directorio):
    ficheros = []
    for nombre_archivo in os.listdir(directorio):
        ruta = os.path.join(directorio, nombre_archivo)
        if os.path.isfile(ruta):
            ficheros.append(nombre_archivo)
    return ficheros

# Ejemplo de uso
directorio = "/ruta/al/directorio"  # Ruta al directorio que deseas listar
ficheros = listar_ficheros(directorio)
for fichero in ficheros:
    print(fichero)
