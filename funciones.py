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
    opcion = input("Seleccione una opción: ")
    while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 6:
        print("Opción inválida. Debe ingresar un número entre 1 y 6.")
        opcion = input("Seleccione una opción: ")
    return int(opcion)


def v_nombre(nombre):
    if nombre.strip() == "":
        return False
    else:
        return True


def v_edad(edad):
    if edad.isdigit() == False:
        return False
    if int(edad) <= 0:
        return False
    return True


def v_nota(nota):
    try:
        nota = float(nota)
    except:
        return False
    if nota < 1.0 or nota > 7.0:
        return False
    return True


def a_estudiante(lista):
    nombre = input("Ingrese el nombre del estudiante: ")
    if v_nombre(nombre) == False:
        print("Error: el nombre no puede estar vacío ni contener solo espacios.")
        return

    edad = input("Ingrese la edad del estudiante: ")
    if v_edad(edad) == False:
        print("Error: la edad debe ser un número entero mayor que cero.")
        return

    nota = input("Ingrese la nota del estudiante: ")
    if v_nota(nota) == False:
        print("Error: la nota debe ser un número decimal entre 1.0 y 7.0.")
        return

    estudiante = {}
    estudiante["nombre"] = nombre
    estudiante["edad"] = int(edad)
    estudiante["nota"] = float(nota)
    estudiante["aprobado"] = False

    lista.append(estudiante)
    print("Estudiante agregado correctamente.")


def a_estados(lista):
    for estudiante in lista:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True
        else:
            estudiante["aprobado"] = False


def m_estudiantes(lista):
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
