#Autor: Gabriel Cely
#Fecha: 25 de septiembre de 2024
#Estructura de una clase
class Perro:
    def __init__(self,nombre):
        self.nombre = nombre 
    def feliz(self):
        print (f"{self.nombre} está feliz")
        
mi_perro = Perro (input("Ingrese el nombre de su perro: "))
mi_perro.feliz()