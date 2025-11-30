# Abre el archivo "ejemplo.txt" en modo lectura ("r").
# El contexto `with` se encarga de cerrar el archivo automáticamente al salir del bloque.
with open("ejemplo.txt", "r") as archivo:
    # Lee todo el contenido del archivo y lo asigna a la variable `contenido`.
    # `contenido` será un único string con todo el texto del archivo.
    contenido = archivo.read()
    # Imprime en la salida estándar (consola) el string almacenado en `contenido`.
    print(contenido)
# Al llegar aquí, el bloque `with` terminó y el archivo `archivo` ya está cerrado.
