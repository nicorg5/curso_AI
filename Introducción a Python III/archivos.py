'''
import os
# Obtener directorio actual de trabajo
cwd = os.getcwd()
print(cwd)
'''

try:
    # Se intenta abrir el archivo en modo lectura
    with open ("mi_archivo.txt", 'r') as file:
        print("El archivo ya existe. No se puede continuar")
except FileNotFoundError:
    # Si el archivo no existe, se crea uno nuevo
    with open ("mi_archivo.txt", 'w') as file:
        print("El archivo no existe. Se ha creado uno nuevo")

        # Se escriben 5 líneas de texto con diferentes contenidos en el archivo
        file.write("Primera línea \n")
        file.write("Segunda línea \n")
        file.write("Tercera línea \n")
        file.write("Cuarta línea \n")
        file.write("Quinta línea \n")


# Se abre el archivo en modo lectura
with open ("mi_archivo.txt", 'r') as file:
    print("Contenido del archivo: ")

    # Bucle para mostrar cada línea del archivo
    while True:
        line = file.readline()
        if not line:
            break # Salida del bucle si no hay más líneas
        print(line)

        # Se muestra la posición actual del cursor
        print("Posición actual del cursor: ", file.tell())


# Se abre el archivo en modo escritura para añadir una nueva línea al final
with open("mi_archivo.txt", "a") as file:
    file.write("Última línea del archivo")


# Se abre el archivo en modo anexar 'a+' y se agrega otra línea al final del archivo
with open("mi_archivo.txt", "a+") as file:
    file.write("\nÚltima línea del archivo con el modo a+")

    # Uso de seek(0) para volver al inicio
    file.seek(0)

    # Lectura del archivo completo
    contenido = file.read()
    print("Contenido del archivo después de añadir otra línea: ")
    print(contenido)


# Se cambia el modificador de 'a+' a 'a'. Este código da error porque se intenta leer el archivo con .read(), pero el modo 'a'
# tan sólo permite escribir en el archivo, no leerlo
with open("mi_archivo.txt", "a") as file:
    file.write("\nÚltima línea del archivo con el modo a")

    # Uso de seek(0) para volver al inicio
    file.seek(0)

    # Lectura del archivo completo
    contenido = file.read()
    print("Contenido del archivo después de añadir otra línea: ")
    print(contenido)