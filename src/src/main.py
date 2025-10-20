from sistema import SistemaControlEscolar

def menu():
    print("1) Registrar alumno")
    print("2) Eliminar alumno")
    print("3) Listar alumnos")
    print("4) Registrar profesor")
    print("5) Registrar materia")
    print("6) Asignar materia a alumno")
    print("7) Listar materias")
    print("8) Salir")

if __name__ == "__main__":
    sistema = SistemaControlEscolar()

    # Datos de ejemplo
    sistema.registrar_profesor("Ana", "Lopez", "F", 35, "Matemáticas", "CED123")
    sistema.registrar_materia("Álgebra", 8, "CED123")
    sistema.registrar_alumno("Luis", "Calva", "NC001", 22, "M", 3)

    while True:
        menu()
        op = input("Opción: ").strip()

        if op == "1":
            n = input("Nombre: ")
            a = input("Apellido: ")
            nc = input("No. Control: ")
            e = int(input("Edad: "))
            s = input("Sexo: ")
            sem = int(input("Semestre: "))
            sistema.registrar_alumno(n, a, nc, e, s, sem)
        elif op == "2":
            nc = input("No. Control a eliminar: ")
            sistema.eliminar_alumno(nc)
        elif op == "3":
            sistema.listar_alumnos()
        elif op == "4":
            n = input("Nombre: ")
            a = input("Apellido: ")
            s = input("Sexo: ")
            e = int(input("Edad: "))
            t = input("Título: ")
            c = input("Cédula: ")
            sistema.registrar_profesor(n, a, s, e, t, c)
        elif op == "5":
            n = input("Nombre materia: ")
            cr = int(input("Créditos: "))
            c = input("Cédula profesor: ")
            sistema.registrar_materia(n, cr, c)
        elif op == "6":
            nc = input("No. Control del alumno: ")
            mat = input("Nombre de la materia: ")
            sistema.asignar_materia_a_alumno(nc, mat)
        elif op == "7":
            sistema.listar_materias()
        elif op == "8":
            break
        else:
            print("Opción inválida")

