# Función números:
valores = int(input("Cuantos números vas a introducir? "))
numeros= []

for i in range(valores):
    num = float(input(f"Introduce el número {i+1} con el que quieres aplicar los cálculos: "))
    numeros.append(num)
print(numeros) #Checkpoint OK, se guarda en la variable numeros en forma de lista. luego pasaremos el argumento como *numeros en las funciones para el desempaquetado.

#PENDIENTE: A partir de aqui la lista de numeros se tiene que desempaquetar en las funciones de operaciones.
'''
def operandos(numeros):
    for valor in valores:
        operando = int(input("Indica el numero {valor}: "))
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input ("Introduce el segundo número: "))


# Alcance de la calculadora: definición de las operaciones que puede llevar a cabo: esto lo mapearemos a las funciones cuando esté listo
def operaciones():
    operaciones = {"suma":suma,
                   "resta": resta,
                   "producto":producto,
                   "division":division}
    return operaciones

# Calculadora (pendiente acabar, segundo paso a corregir)
def calculadora (operaciones, operandos):
    for contador in valores:
        contador=-1
    = float(input("Marca el primer número: "))
#que operacion quieres que le aplique
#marca el segundo numero
#Resultado, sigue si contador no es 0, en bucle.

#Funciones operaciones:PENDIENTE DE APLICAR.
def calculadora()
# Función suma
def suma(*numeros):
    
calculo_suma = suma(numero1,numero2)
print(f"La suma de los números introducidos es {calculo_suma}")

# Función resta
def resta(*numeros):
    return numero1-numero2
calculo_resta = resta(numero1,numero2)
print(f"La resta de los números introducidos es {calculo_resta}")

# Función multiplicacion
def producto(*numeros):
    return numero1 * numero2
calculo_producto = producto(numero1,numero2)
print(f"La multiplicación de los números introducidos es {calculo_producto}")

# Función división:
def division (*numeros):
    if numero2 ==0:
        return "No se puede dividir entre 0"
    Else:
    return numero1/numero2
calculo_division = division(numero1,numero2)
print(f"La división de los números introducidos es {calculo_division}")'''