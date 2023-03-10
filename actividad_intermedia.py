"""
QA Minds Labs estaría necesitando de un sistema que permita administrar sus cursos. En este sentido el sistema debe
contar con la posibilidad de crear un  Curso, el cual tendrán un nombre, cantidad de alumnos, un estado y cantidad de clases.
El sistema debe poder dar de alta un Curso.
El sistema debe permitir buscar un curso y poder modificar su estado (Ejemplo: de No Iniciado a Activo)
El sistema debe permitir mostrar TODOS los Cursos existentes, como también la posibilidad de mostrar toda la información del curso.
"""


def add_course():
    print("\nIngresa un nuevo curso: ")
    course_name = input("Ingresa el nombre del curso: ")
    num_students = input("Ingresa numero de alumnos: ")
    status = input("Ingresa el STATUS del curso\nINICIADO\nNO INICIADO\nTu respuesta:  ")

    nueva_entrada = {
        "COURSE_NAME": course_name,
        "NUM_STUDENTS": num_students,
        "STATUS": status,
    }
    COURSES_LIST.append(nueva_entrada)


COURSES_LIST = []
def show_courses():
    n_courses = str(len(COURSES_LIST))
    print(f"\nLos cursos actuales en el sistema son {n_courses}: \n{COURSES_LIST}")


def search_course():
    course_name = input("Ingresa nombre de curso: ")
    cont = 0
    existe = False
    # comprobar si el curso existe en la lista de diccionariosADD

    for course in COURSES_LIST:
        if course['COURSE_NAME'] != course_name:
            cont += 1
    if cont == len(COURSES_LIST):
        print(f"El curso {course_name} no esta en la lista")
        return False
    else:
        existe = True
    # buscar el nombre del curso e imprimir la entrada
    if existe:
        for course in COURSES_LIST:
            if course['COURSE_NAME'] == course_name:
                print(course)
                return course
                # print(course)


def delete_course(COURSES_LIST: list):
    ACTIONS = ("YES", "NO ")
    respuesta = input("Deseas eliminar un curso?:\nYES\nNO\nTu respuesta:  ")
    if respuesta == ACTIONS[0]:
        course_name = input("Ingresa el nombre del curso a eliminar:  ")
        for course in COURSES_LIST:
            if course['course_name'] == course_name:
                pop(course['course_name'])
                print(f"se elimino: {course_name}")
            else:
                print("Curso no existe, no hubo modificaciones")

def update_course():
    print("\nQuieres quieres actualizar una entrada?\n")
    ACTIONS = ["YES", "NO"]
    action = input('|'.join(ACTIONS) + '|: ')
    if action == ACTIONS[0]:
        print("\nIngresa nombre de curso que quieres actualizar: ")
        course = search_course()
        if course is not False:
            print("\nQue dato quieres actualizar?\n")
            DATA = ["COURSE_NAME", "NUM_STUDENTS", "STATUS"]
            respuesta = input('|'.join(DATA) + '|: ')
            if respuesta == DATA[0]:
                course_name = input("Ingresa el nuevo nombre del curso: ")
                course['COURSE_NAME'] = course_name

            elif respuesta == DATA[1]:
                num_students = input("Ingresa nuevo numero de alumnos: ")
                course['NUM_STUDENTS'] = num_students

            elif respuesta == DATA[2]:
                status = input("Ingresa el nuevo STATUS del curso\nINICIADO\nNO INICIADO\nTu respuesta:  ")
                course['STATUS'] = status

            print(f"Tu entrada actualizada es la siguiente:\n{course}")
        else:
            pass


ACTIONS = ("SEARCH", "ADD", "UPDATE", "PRINT", "DELETE", "EXIT ")

while True:
    actions_list = " | ".join(ACTIONS)
    action = input(f"Seleccione una accion: {actions_list}")
    if action == ACTIONS[0]:
        search_course()
    elif action == ACTIONS[1]:
        add_course()
    elif action == ACTIONS[2]:
        update_course()
    elif action == ACTIONS[3]:
        show_courses()
    elif action == ACTIONS[4]:
        pass
    elif action == ACTIONS[5]:
        print("\nCerrando Sistema")
        break
    else:
        print(f"Operacion no soportada: {action}")


