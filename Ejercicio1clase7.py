'''
# Crear una clase de mascota e instanciarla para hacer una mascota
# Crearlo con métodos y no con funciones 

class Mascota:
    def __init__(self, tipodato: str, 
                 accion: str, 
                 raza: str, 
                 vidas: str): # __init__Es el metodo constructor
         B
        self.tipodato = tipodato
        self.accion = accion
        self.raza= raza
        self.vidas = vidas
        self.historialmedico = []
        print(f"Creamos a un {self.tipodato}, que {self.accion}, es { self.raza} y tiene {self.vidas}")
    
gato = Mascota("gato", "ronronea","europeo",7)

print("Gato")
print(gato.raza)

# Ejercicio: crear dos personajes y un combate entre ambos
Crear una clase Personaje OK
Hacer dos personajes OK
Darles un metodo de ataque (que sea capaz de afectar al otro!)
Ver como se pegan entre si, tal vez uno muera!

combatientes = []

class Personaje:
    def __init__(self, nombre: str,
                 ataque: int, 
                 defensa: int, 
                 vida: int): # __init__Es el metodo constructor)
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        combatientes.append(self)

        print(f"Se ha creado a {self.nombre}, y está listo para luchar: ")

Personaje1 = Personaje("Thor",12,8,60)
Personaje2 = Personaje("Hulk",15,6,100)

print(combatientes)

def seleccion_personajes_combate():
    nombre1 = input("Introduce el nombre del primer personaje: ")
    nombre2 = input("Introduce el nombre del segundo personaje: ")
    return validar_personajes(nombre1,nombre2)

def validar_personajes(nombre1,nombre2):
    if nombre1 and nombre2 in combatientes:
        combate(nombre1, nombre2)
    else:
        print("Uno o los dos personajes introducidos no han sido creados, créalos primero")
        return

def combate(atacante: Personaje, defensor: Personaje):
    turno = 0
    while atacante.vida > 0 and defensor.vida > 0:
        if turno % 2 == 0: # turno del atacante
            daño = (atacante.ataque - defensor.defensa)
            defensor.vida =- daño
            print(f"{atacante.nombre} ataca a {defensor.nombre} y reduce su vida a {defensor.vida}")
        else: #turno del defensor
            daño = defensor.ataque - atacante.defensa
            atacante.vida=-daño
            print(f"{defensor.nombre} ataca a {atacante.nombre} y reduce su vida a {atacante.vida}")
        turno=+1
    if atacante.vida <= 0 and defensor.vida <=0:
        print("Empate! Ambos combatientes han caído en el mismo turno!")
    elif atacante.vida <= 0:
        print(f"{defensor.nombre} ha ganado el combate!")
    else:
        print(f"{atacante.nombre} ha ganado el combate!")

seleccion_personajes_combate()

#Ultimoejercicio
#Hay que hacer una clase de Tajamar que tenga alumnos, uno debe ser dataclass(alumnos) y el otro no (cursos)

'''

import dataclasses
# Dataclass

class Alumno(): # Dataclase
    nombre: str
    apellido1: str
    apellido2: str
    edad: int
    curso: str
    def Curso_Tajamar(Alumno, nombre_curso: str, profesor: str, horas: int):
        nombre_curso.curso = "Python"

Alumno1 = Alumno(nombre="José Miguel", apellido1 ="Cuenca",apellido2 ="Fernández", edad=34, curso="Python")

import dataclasses

# Dataclass
@dataclasses.dataclass

class Persona():  # dataclass!
    edad: int
    nombre: str = ""

    def comer(self):
        ...

heily = Persona(nombre="Heily", edad=22)
print(heily.nombre)