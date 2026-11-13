cantidad_chefs = 0

while cantidad_chefs <= 0:
    try:
        cantidad_chefs = int(input("Ingrese la cantidad de chefs que desea registrar: "))
        if cantidad_chefs <= 0:
            print("¡Ingrediente invalido! Ingresa un entero positivo para continuar al registro.")
    except:
        print("¡Ingrediente invalido! Ingresa un entero positivo para continuar el registro.")
        cantidad_chefs = 0 

chefs_maestros = 0
chefs_aprendices = 0

for i in range(cantidad_chefs):
    print("\nRegistro del Chef", i + 1)

    codigo_culinario = input("Ingrese el codigo culinario: ")

    while len(codigo_culinario) < 6 or " " in codigo_culinario:
        print("El codigo debe tener al menos 6 caracteres y no contener espacios.")
        codigo_culinario = input("Ingrese nuevamente el codigo culinario: ")

    experiencia = 0

    while experiencia <= 0:
        try:
            experiencia = int(input("Ingrese la experiencia culinaria en años: "))
            if experiencia <= 0:
                print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
        except:
            print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
            experiencia = 0

    if experiencia > 5:
        print("Clasificacion : Chef Maestro")
        chefs_maestros += 1
    else:
        print("Clasificacion Chef Aprendiz")
        chefs_aprendices += 1

print("\n¡La escuela cuenta con", chefs_maestros, "Chef Maestros y", chefs_aprendices, "Chef Aprendices! ¡A cocinar!")
print("Total de chefs registrados:", cantidad_chefs)