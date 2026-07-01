def m_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2.")
    print("3.")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("=====================================")


def l_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Opción inválida. Debe ingresar un número entre 1 y 6.")
        except ValueError:
            print("Error: debe ingresar un número entero.")


def v_nombre(nombre):
    if nombre.strip() == "":
        return False
    if "." in nombre:
        return False

    nombre_sin_espacios = nombre.replace(" ", "")
    if not nombre_sin_espacios.isalpha():
        return False

    return True


def v_edad(edad):
    if edad <= 0 or edad > 120:
        return False
    return True


def v_nota(nota):
    if nota < 1.0 or nota > 7.0:
        return False
    return True


def limpiar_pantalla():
    print("\n" * 60)


def a_estudiante(lista):
    limpiar_pantalla()
    print("=== AGREGAR NUEVO ESTUDIANTE ===")
    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        if v_nombre(nombre):
            break
        print("Error: el nombre solo puede contener letras y espacios, no puede estar vacío ni tener puntos o símbolos.")

    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if v_edad(edad):
                break
            print("Error: la edad debe ser un número entero razonable (entre 1 y 120 años).")
        except ValueError:
            print("Error: la edad debe ser un número entero.")

    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante: "))
            if v_nota(nota):
                break
            print("Error: la nota debe ser un número decimal entre 1.0 y 7.0.")
        except ValueError:
            print("Error: la nota debe ser un número decimal.")

    estudiante = {
        "nombre": nombre.strip(),
        "edad": edad,
        "nota": nota,
        "aprobado": False
    }

    lista.append(estudiante)
    print("\nEstudiante agregado correctamente.")
    input("\nPresione Enter para continuar...")


def a_estados(lista):
    for estudiante in lista:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True
        else:
            estudiante["aprobado"] = False


def m_estudiantes(lista):
    limpiar_pantalla()
    a_estados(lista)
    print("=== LISTA DE ESTUDIANTES ===")
    for estudiante in lista:
        print("Nombre:", estudiante["nombre"])
        print("Edad:", estudiante["edad"])
        print("Nota:", estudiante["nota"])
        if estudiante["aprobado"] == True:
            print("Estado: APROBADO")
        else:
            print("Estado: REPROBADO")
        print("*" * 40)
    input("\nPresione Enter para continuar...")