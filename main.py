import funciones

lista_estudiantes = []

while True:
    funciones.m_menu()
    opcion = funciones.l_opcion()

    if opcion == 1:
        funciones.a_estudiante(lista_estudiantes)
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        funciones.a_estados(lista_estudiantes)
    elif opcion == 5:
        funciones.m_estudiantes(lista_estudiantes)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
