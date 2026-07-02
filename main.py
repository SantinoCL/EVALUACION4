import funciones

lista_estudiantes = [
    {"nombre": "Ana Torres", "edad": 20, "nota": 5.5, "aprobado": False},
    {"nombre": "Pedro Soto", "edad": 22, "nota": 3.2, "aprobado": False}
]

try:
    while True:
        funciones.limpiar_pantalla()
        funciones.m_menu()
        opcion = funciones.l_opcion()

        if opcion == 1:
            funciones.a_estudiante(lista_estudiantes)
        elif opcion == 2:
            funciones.b_estudiante(lista_estudiantes)
        elif opcion == 3:
            funciones.e_estudiante(lista_estudiantes)
        elif opcion == 4:
            funciones.limpiar_pantalla()
            funciones.a_estados(lista_estudiantes)
            print("Estados de aprobación actualizados con éxito.")
            input("\nPresione Enter para continuar...")
        elif opcion == 5:
            funciones.m_estudiantes(lista_estudiantes)
        elif opcion == 6:
            funciones.limpiar_pantalla()
            print("Gracias por usar el sistema. Vuelva Pronto")
            break
except KeyboardInterrupt:
    print()
    print("Programa interrumpido por el usuario. Vuelva Pronto")
