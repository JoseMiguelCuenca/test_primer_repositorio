'''#*****EJERCICIO 1*****
# =====Crear una clase de mascota e instanciarla para hacer una mascota=====
# =====Crearlo con métodos y no con funciones===============================
class Mascota: #Defino la clase Mascota
    def __init__(self, animal: str, # Incorporo sus nombres de cada clase con el método especial de construcción: 
                 raza: str, 
                 vidas: str): # __init__Es el metodo constructor
        # Incorporo sus atributos con el método especial de construcción (un atributo para cada nombre de clase): 
        self.animal = animal
        self.raza= raza
        self.vidas = vidas
        self.historialmedico = []
        print(f"Creamos a un {self.animal}, es  {self.raza}, y tiene {self.vidas}") 

    def accion(self):  #Incorporo un método acción, con las acciones que hace la clase, el método ha de estar pensado para
                       #todos los elementos de la clase mascota, pero se ha añadido ronronea para practicar (debería ser más amplio)
        print(f"El {Mascota.nombre} ronronea")

gato = Mascota("Gato","Europeo","7 vidas") # Creo la instancia Gato, generando un registro en la clase Mascota

print(gato.animal)
print(gato.raza)
print(gato.vidas)'''
'''# *****EJERCICIO 2*****
# =====Crear dos personajes y un combate entre ambos===========================
# (pasos para llevarlo a cabo):
#======1. Crear una clase Personaje OK=========================================
#=======2. Hacer dos o más personajes (instancias) OK==========================
#=======3. Darles un metodo de ataque (que sea capaz de afectar al otro)=======
#=======4. Ver como se pegan entre si, tal vez uno muera!======================
#=====correccion a aplicar: (Método: funciones dentro de la clase!)============

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
        combatientes.append(self.nombre) # Le añado a (self) el atributo nombre para que solo me guarde en la lista el nombre.
        print(f"Se ha creado a {self.nombre}, con ataque {self.ataque}, defensa {self.defensa}, {self.vida} puntos de vida, y está listo para luchar! ")
    
    def seleccion_personajes_combate(self): # Un par de inputs que nos hacen elegir los personajes a combatir, argumentos solo self (lo que uso fuera del metodo)
        luchador_1 = input("Introduce el nombre del primer luchador: ")
        if luchador_1 not in combatientes:
            return "El personaje no ha sido creado, créalo como luchador antes de iniciar un combate con él"
        else:
            luchador_2 = input("Introduce el nombre del segundo luchador: ")
            if luchador_2 in combatientes:
                return "Los dos luchadores están preparados, que comience el combate!"
                # En este punto añadiré más adelante que no se puede seleccionar el combatiente seleccionado como luchador_1 +
                # dado que un personaje no debería poder luchar contra sí mismo!
            else:
                return "El segundo personaje no ha sido creado, créalo como luchador antes de iniciar un combate con él"
# Creación de dos instancias (dos posibles combatientes)
Thor = Personaje ("Thor",12,8,60)
Hulk = Personaje ("Hulk", 15,5,85)
# Checkpoint (OK)
print(combatientes)
# Checkpoint2 (OK)
# No entiendo por que le tengo que llamar desde Thor, si quiero que sea una opcion de interacción para iniciarla
# Cuando quiera, sin necesidad de llamar a una instancia
Combate = Thor.seleccion_personajes_combate()
print(Combate)
    # Pendiente separar el método de selección del de validación
    
    def validar_personajes(self): # Comprobar que se han creado y su nombre está en combatientes
    """   ...
       idea:
       # inicioestructuraidea
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
        # finestructuraidea
        """
    def combate(self, atacante: Personaje, defensor: Personaje): 
            #Dinámica del combate, he indicar las clases ya que utilizaré los atributos que la contienen
        ...
    
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
'''
'''# *****EJERCICIO 3*****
#====Crear un coche======================================================
#====Crear una persona===================================================
#====La persona va a conducir el coche#==================================
#====Habra luego mas personas que seran los pasajeros#===================
#====TRUCO: Las ruedas, volante, etc... pueden ser objetos tambien!======

pendiente hacer
''''''

'''#*****EJERCICIO 4*****
'''# *****EJERCICIO 4*****
#========Hay que hacer una clase de Tajamar que tenga alumnos===========
#========uno debe ser dataclass(alumnos) y el otro no (cursos)==========

import dataclasses

@dataclasses.dataclass # Decorador: Decora una funcionalidad aumenta la forma de trabajar, de forma visual, etc.

class Alumno(): # Dataclase
    nombre: str
    apellido1: str
    apellido2: str
    edad: int
    curso: str

    def Curso_Tajamar(self, Alumno, nombre_curso: str, profesor: str, horas: int): # Se incluye el sel(para cualquier método de clase)
        nombre_curso.curso = "Python"

Alumno1 = Alumno(nombre="José Miguel", apellido1 ="Cuenca",apellido2 ="Fernández", edad=34, curso="Python")'''