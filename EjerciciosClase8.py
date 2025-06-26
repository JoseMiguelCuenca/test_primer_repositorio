# *****Ejerccio 1*****
#=====Crear dos clases (mago y medico) de personaje=======
#=====el mago deberia poder hacer magia===================
#=====el medico deberia poder curar a otros personajes====
from inspect import stack


class Personaje:
    def __init__(self, nombre: str, rol: str):
        self.nombre = nombre
        self.rol = rol
        self.puntos_vida = 100
        self.inventario = []
        self.nivel = 1
        print(f"Se ha creado a {self.nombre}, un {self.rol} de nivel {self.nivel}!")

    def ataque_basico(self):
        print(f"{self.nombre} ha atacado!")

class Mago(Personaje):
    def magia(self):
        print(f"{self.nombre} ha realizado un ataque especial, ataque mágico!")

class Medico(Personaje): # Se le puede dar más chicha, darle la vida si las instanciamos
    def curar(self, other: Personaje):
        print(f"{self.nombre} cura a {other.nombre}")

 # *****Ejerccio 2*****
'''
x = 10
y = 0

try:
    resultado = x / y  # Intento dividir por cero
except ZeroDivisionError:
    print("No se puede dividir por cero!)


edad = int(input("Pon aqui tu edad: "))

if edad < 0:
    raise ValueError("Esta edad es incorrecta!")


numero = input("Dime un numero: ")
try:
    numero += 10
except Exception as error:
    print(error)'''

# Crear un error para un objeto que se ha agotado en un ecommerce
'''class RetiradaIncorrecta(Exception):
    pass

class CuentaBancaria:
    def __init__(self, saldo: float):
        self.saldo_bancario = saldo

    def retirar_efectivo(self, cantidad: float) -> float:
        if self.saldo_bancario < cantidad:
            raise RetiradaIncorrecta(f"No puedes retirar {self.cantidad} de tu cuenta")
        else:
            self.saldo_bancario -= cantidad
            return cantidad'''

class ProductoAgotado(Exception): #Clase para añadir el error
    pass

class InventarioOnline: #Método
    #Atributos
    def __init__(self,descripcionproducto:str,cantidad:int):
        self.descripcionproducto = descripcionproducto 
        self.cantidad = cantidad
    def retirada(self, unidadesretirada: int)-> str:
        if self.cantidad = 0
            raise ProductoAgotado(f"El producto no está en stock, por lo que no puede ser retirado")
        elif self.cantidad < unidadesretirada:
             unidadesdisponibles = self.cantidad -unidadesretirada
             raise ProductoAgotado(f"El producto no tiene suficientes unidades en stock, por lo que solo se retirarán las unidades disponibles {unidadesdisponibles}")
        else:
            self.cantidad-= unidadesretirada
            return unidadesretirada