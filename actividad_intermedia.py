"""
QA Minds Labs estaría necesitando de un sistema que permita administrar sus cursos. En este sentido el sistema debe
contar con la posibilidad de crear un  Curso, el cual tendrán un nombre, cantidad de alumnos, un estado y cantidad de clases.
El sistema debe poder dar de alta un Curso.
El sistema debe permitir buscar un curso y poder modificar su estado (Ejemplo: de No Iniciado a Activo)
El sistema debe permitir mostrar TODOS los Cursos existentes, como también la posibilidad de mostrar toda la información del curso.
"""


def add_course(SYSTEM_COURSES: dict, courses_list: list):
    print("Dar de alta un Curso:")

    course_name = input("Ingresa nombre del curso: ")
    num_of_students = input("Ingresa numero de estudiantes: ")
    status = input("Cual es el estado?\nACTIVO\nNO INICIADO\nTu respuesta: ")

    nueva_entrada = {
        "course_name": course_name,
        "num_of_students": num_of_students,
        "status": status
    }
    courses_list.append(nueva_entrada)


COURSES_LIST = []
def show_courses(SYSTEM_COURSES: dict, COURSES_LIST: list):
    print(f"Los cursos actuales son: \n{COURSES_LIST}")


def search_course(COURSES_LIST: list, course_name: str):
    for course in COURSES_LIST:
        if course['course_name'] == course_name:
            print(course)

def delete_course(COURSES_LIST: list):
    ACTIONS = ("YES", "NO ")
    respuesta = input("Deseas eliminar un curso?:\nYES\nNO\nTu respuesta:  ")
    if respuesta == ACTIONS[0]:
        course_name = input("Ingresa el nombre del curso a eliminar:  ")
        for course in COURSES_LIST:
            if course['course_name'] == course_name:
                course['course_name'].pop()
                print(f"se elimino: {course_name}")
            else:
                print("Curso no existe, no hubo modificaciones")

def update_status(COURSES_LIST: list):
    ACTIONS = ("YES", "NO ")
    respuesta = input("Deseas actualizar el estatus?:\nYES\nNO\nTu respuesta:  ")
    if respuesta == ACTIONS[0]:
        course_name = input("Ingresa el nombre del curso a actualizar status:  ")
        new_status = input("Ingresa el nuevo Status:  ")
        for course in COURSES_LIST:
            if course['course_name'] == course_name:
                course['status'] = new_status
                print(course['status'])
            else:
                print("Curso no existe, no hubo modificaciones")

def update_varios(COURSES_LIST: list):
    ACTIONS = ("YES", "NO ")
    respuesta = input("Deseas actualizar el estatus?:\nYES\nNO\nTu respuesta:  ")
    if respuesta == ACTIONS[0]:
        course_name = input("Ingresa el nombre del curso a actualizar status:  ")
        new_status = input("Ingresa el nuevo Status:  ")
        for course in COURSES_LIST:
            if course['course_name'] == course_name:
                course['status'] = new_status
                print(course['status'])
            else:
                print("Curso no existe, no hubo modificaciones")


SYSTEM_COURSES = {}

ACTIONS = ("SEARCH", "ADD", "UPDATE", "PRINT", "DELETE", "EXIT ")

while True:
    actions_list = " | ".join(ACTIONS)
    action = input(f"Seleccione una accion: {actions_list}")
    if action == ACTIONS[0]:
        course_to_search = input("Ingresa nombre del curso a buscar: ")
        search_course(COURSES_LIST, course_to_search)
    elif action == ACTIONS[1]:
        add_course(SYSTEM_COURSES, COURSES_LIST)
    elif action == ACTIONS[2]:
        update_status(COURSES_LIST,)
    elif action == ACTIONS[3]:
        show_courses(SYSTEM_COURSES, COURSES_LIST)
    elif action == ACTIONS[4]:
        delete_course(COURSES_LIST)
    elif action == ACTIONS[5]:
        break
    else:
        print(f"Operacion no soportada: {action}")


