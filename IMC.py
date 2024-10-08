# Calculadora de Índice de masa corporal

def solicitar_datos():
    while True:
        nombre = input("Ingresa tu nombre: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")
        
    while True:
        apellido_paterno = input("Ingresa tu apellido paterno: ").strip()
        if apellido_paterno:
            break
        print("El apellido paterno no puede estar vacío.")
        
    while True:
        apellido_materno = input("Ingresa tu apellido materno: ").strip()
        if apellido_materno:
            break
        print("El apellido materno no puede estar vacío.")
    
    while True:
        try:
            edad = int(input("Ingresa tu edad: ").strip())
            if edad > 0:
                break
            print("La edad debe ser un número positivo.")
        except ValueError:
            print("Debes ingresar un número válido para la edad.")
    
    while True:
        try:
            peso = float(input("Ingresa tu peso en kilogramos: ").strip())
            if peso > 0:
                break
            print("El peso debe ser un número positivo.")
        except ValueError:
            print("Debes ingresar un número válido para el peso.")
    
    while True:
        try:
            estatura = float(input("Ingresa tu estatura en metros (ej. 1.75): ").strip())
            if estatura > 0:
                break
            print("La estatura debe ser un número positivo.")
        except ValueError:
            print("Debes ingresar un número válido para la estatura.")
    
    return nombre, apellido_paterno, apellido_materno, edad, peso, estatura

def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def mostrar_datos(nombre, apellido_paterno, apellido_materno, edad, peso, estatura, imc):
    print("\nDatos ingresados:")
    print(f"Nombre: {nombre} {apellido_paterno} {apellido_materno}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Estatura: {estatura} m")
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

# Programa principal
nombre, apellido_paterno, apellido_materno, edad, peso, estatura = solicitar_datos()
imc = calcular_imc(peso, estatura)
mostrar_datos(nombre, apellido_paterno, apellido_materno, edad, peso, estatura, imc)