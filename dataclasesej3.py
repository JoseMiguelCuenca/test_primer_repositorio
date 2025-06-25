import dataclasses

@dataclasses.dataclass

class Alumno(): # Dataclase
    nombre: str
    apellido1: str
    apellido2: str
    edad: int
    curso: str
    def Curso_Tajamar(self,Alumno, nombre_curso: str, profesor: str, horas: int):
        nombre_curso.curso = "Python"
        
Alumno1 = Alumno(self, nombre="José Miguel", apellido1 ="Cuenca",apellido2 ="Fernández", edad=34, curso="Python")