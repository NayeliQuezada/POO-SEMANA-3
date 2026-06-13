class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    def mostrar_información(self):
        print("\n=== Información de la Mascota ===")
        print(f"Nombre : {self.nombre}")
        print(f"Especie : {self.especie}")
        print(f"Edad : {self.edad}")

    def hacer_sonido(self):
        if self.especie == "perro":
            print("Sonido: Guau Guau")
        elif self.especie == "conejo":
            print(f"{self.nombre} dice: ¡Ñic ñic!")
           
        else:
            print("Sonido: Sonido detectado")
