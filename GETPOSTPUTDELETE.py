'''Haced un sistema de peticiones HTTP:
Las peticiones HTTP son GET, POST, PUT y DELETE (hay mas), 
hacer un sistema de enrutado (router) que me registre las diferentes direcciones con sus metodos, y ademas, 
un sistema renderizado (render) que me resuelva cierta logica para esas urls'''

# Ejemplo Joaquin:
'''def GET(url:str):
    return f"Haciendo GET a {url}", 200
'''
# Definición de los datos (de forma general, sin métodos concretos para URLs)
direcciones = {}

def GET(direccion_url): # Seleccion de una URL
    dirreccion_url = "f{valor}"
    seleccion = direccion_url
    return seleccion

def POST(nuevo_contenido, direccion_url): # Creación de nuevo libro
    datos =  {"LibroNuevo":direccion_url}
    nuevo_contenido = datos.fromkeys("LibroNuevo":direccion_url)

def router():  # 1 - Guarde mis urls + verbos
    return

def render():  # Aplica funcion a esa url+verbo SI EXISTE
    return