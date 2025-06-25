# Crear una clase de mascota e instanciarla para hacer una mascota
class Mascota:
    def __init__(self, tipodato: str, 
                 accion: str, 
                 raza: str, 
                 vidas: str): # __init__Es el metodo constructor
        self.tipodato = tipodato
        self.accion = accion
        self.raza= raza
        self.vidas = vidas
        self.historialmedico = []
        print(f"Creamos a un {self.tipodato}, que {self.accion}, es { self.raza} y tiene {self.vidas}")
    
gato = Mascota("gato", "ronronea","europeo",7)

print("Gato")
print(gato.raza)

'''              
              class Mascota:
    def __init__(self, nombre : str, edad : int, raza : str):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.historial = []

    def ladrar(self):
        return f"{self.nombre} está ladrando."
    
    def agregar_historial(self, evento: str):
        self.historial.append(evento)
    
    def mostrar_historial(self):
        if not self.historial:
            return f"{self.nombre} no tiene eventos en su historial."
        return f"Historial de {self.nombre}: " + ", ".join(self.historial)
'''