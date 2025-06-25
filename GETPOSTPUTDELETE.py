'''Haced un sistema de peticiones HTTP:
Las peticiones HTTP son GET, POST, PUT y DELETE (hay mas), 
hacer un sistema de enrutado (router) que me registre las diferentes direcciones con sus metodos, y ademas, 
un sistema renderizado (render) que me resuelva cierta logica para esas urls'''

# Ejemplo Joaquin:
'''def GET(url:str):
    return f"Haciendo GET a {url}", 200
'''
# Definición de los datos (de forma general, sin métodos concretos para URLs)
direcciones = {url:}

# Diccionario que guarda los libros con la URL de datos
datos = {"Libro": direccion_url}

def enrutado(metodo,direccion_url):
    "La función registra la direccion URL con su método y contenido"
    metodo = metodo.upper()
    if direccion_url not in direcciones:
        direcciones[url] = {}
        direcciones[url][metodo] = contenido
    else:
       print(f"Dirección {} registrada")

def GET(direccion_url): # Seleccion de una URL, está completado
    if dirreccion_url in direcciones:
        return direcciones[direccion_url]
    else:
        print("Error 404, dirección no encontrada")

def POST(nuevo_contenido, direccion_url): # Creación de nuevo libro, está completado.
    if dirreccion_url not in direcciones:
        direcciones[direccion_url]
    nuevo_contenido = datos.fromkeys("LibroNuevo":direccion_url)

def put():  # 1 - Guarde mis urls + verbos 3 falta terminar, a tener en cuenta que el diccionario es datos
    return

def delete(): # - Elimina los datos de ese libro #falta terminar
