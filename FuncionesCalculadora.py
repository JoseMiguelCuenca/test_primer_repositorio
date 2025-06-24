'''# Función números:
numeros = int(input("Indica la cantidad de números en los quieres aplicar cálculos: "))

def entrada(numeros):
    for valores in numeros:
        input(f"Introduce el número {valores}: ")'''

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input ("Introduce el segundo número: "))

# Función suma
def suma(numero1,numero2):
    return numero1+numero2
calculo_suma = suma(numero1,numero2)
print(calculo_suma)

# Función resta
def resta(numero1,numero2):
    return numero1-numero2
calculo_resta = resta(numero1,numero2)
print(calculo_resta)

# Función multiplicacion
def producto(numero1,numero2):
    return numero1 * numero2
calculo_producto = producto(numero1,numero2)
print(calculo_producto)

# Función división:
def division (numero1,numero2):
    return numero1/numero2
calculo_division = division(numero1,numero2)
print(calculo_division)