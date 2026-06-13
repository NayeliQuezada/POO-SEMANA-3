# Función para registrar los datos de la mascota
def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie: ")
    edad = int(input("Ingrese la edad: "))
    return nombre, especie, edad

# Función para mostrar los datos
def mostrar_mascota(nombre, especie, edad):
    print("\n--- Información de la Mascota ---")
    print(f"Nombre: {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad: {edad} años")

# Programa principal
nombre, especie, edad = registrar_mascota()
mostrar_mascota(nombre, especie, edad)