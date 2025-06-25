# Ejercicio: Crea una base de datos con nombre, edad, notas

asignaturas = [{"id_asignatura":2 , "nombre":"Matemáticas"},
               {"id_asignatura": 5, "nombre":"Álgebra"},
               {"id_asignatura": 4 , "nombre":"Estadística"},
               {"id_asignatura":6 , "nombre":"Programación con Python para Data Science"},
               {"id_asignatura": 3 , "nombre":"Fundamentos de programación en Python"},
               {"id_asignatura": 1 , "nombre":"Algoritmos"}]

alumnos = [
            {"Nombre":"David", "apellido1":"Gonzalez", "apellido2": "Ramirez", "edad": 30},
            {"Nombre":"Marc", "apellido1":"Perez", "apellido2": "Gutierrez", "edad": 22},
            {"Nombre":"Antonio", "apellido1":"Castro", "apellido2": "Alarcon", "edad": 19},
            {"Nombre":"Felipe", "apellido1":"Puig", "apellido2": "Puyol", "edad": 25}]

#Pendiente:

'''Matricuaciones la generaremos como resultado de alumnos y asignaturas, haremos un recorrido de 
ambos diccionarios y de forma aleatoria generaré el diccionario de matriculaciones'''

'''
matriculaciones = [ 
    {"id_alumno":, "id_asignatura":,"año_matriculacion":, "nota_obtenida":},
    {"id_alumno":, "id_asignatura":,"año_matriculacion":, "nota_obtenida":},
    {"id_alumno":, "id_asignatura":,"año_matriculacion":, "nota_obtenida":},
    {"id_alumno":, "id_asignatura":,"año_matriculacion":, "nota_obtenida":}]


# Uso de la librería random para generar datos aleatorios:
import random as rd

base_datos = {}

# Introducción de los datos
num_alumnos = int(input("Dime cuantos alumnos quieres que tenga la base de datos: "))
num_asignaturas = int(input("Dime cuantas asignaturas quieres que tenga la base de datos: "))
num_cursos = int(input("Dime cuantos cursos quieres que tenga la base de datos: "))

'''