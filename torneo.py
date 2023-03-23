




import os
from enum import Enum
import random


class Datos:
    NOMBRE = ['KENNY', "STAN", "ERICK", "RICK"]
    APODO = [" CRASHBONES", " SKULL_MASTER", " DEATH_EATER", " DISSASTER"]
    EMAIL = "xxx@mail.com"
    RAZA = ["Terran", "Protoss", "Zerg"]

######
# PRIMERO CREO LA CLASE CON LOS ATRIBUTOS Y METODOS QUE DEBE CONTENTENR
######

class Jugador:

    def __init__(self, nombre: str, raza: str, email: str, status: str, puntos: int, partidas: int):
        self.__nombre = nombre
        self.__raza = raza
        self.__email = email
        self.__status = status
        self.__puntos = puntos
        self.__partidas = partidas

    # creamos funciones para modificar indirectamente los atributos de la clase

    def obtener_nombre(self):
        return self.__nombre

    def obtener_raza(self):
        return self.__raza

    def obtener_email(self):
        return self.__email

    def obtener_status(self):
        return self.__status

    def obtener_puntos(self):
        return self.__puntos

    def obtener_partidas(self):
        return self.__partidas

    def actualizar_nombre(self, nombre: str):
        self.__nombre = nombre

    def actualizar_raza(self, raza: str):
        self.__raza = raza

    def actualizar_email(self, email: str):
        self.__email = email

    def actualizar_puntos(self, puntos: str):
        self.__puntos = puntos

    def actualizar_status(self, status: str):
        self.__status = status

    def actualizar_partidas(self, partidas: str):
        self.__partidas = partidas


    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"(nombre={self.__nombre}, raza={self.__raza}, email={self.__email}, status={self.__status}, puntos={self.__puntos}, partidas={self.__partidas})"

#############################################################################
# FUNCION PARA GENERAR DATOS ALEATORIOS
#############################################################################
def generar_datos_aleatorios():
    num_random = str(random.randint(1, 100))
    nombre_random = f"{random.choice(Datos.NOMBRE)}{random.choice(Datos.APODO)}_{num_random}"
    raza_random = random.choice(Datos.RAZA)
    email_random = Datos.EMAIL.replace("xxx", num_random)
    return nombre_random, raza_random, email_random

#############################################################################
# FUNCION PARA CREAR NUEVOS JUGADORES
#############################################################################
def crear_jugador():
    imprimir_header(" Creando jugadores ")
    numero_de_jugadores = int(menu_crear_jugadores())

    for jugador in range(numero_de_jugadores):
        nombre, raza, email = generar_datos_aleatorios()
        status = "ACTIVO"
        puntos = 0
        partidas = 0
        jugador = Jugador(nombre, raza, email, status, puntos, partidas)
        JUGADORES.append(jugador)
        print(f"Jugador registrado: {jugador}")

#############################################################################
# FUNCION PARA IMPRIMIR UN MATCH
#############################################################################
def imprimir_match(jugador_1: Jugador, jugador_2: Jugador, index: int):
    imprimir_header(f" MATCH: {index} ")
    print(f"\n{jugador_1.obtener_nombre()}\n{' ' * 7}VS\n{jugador_2.obtener_nombre()}")

#############################################################################
# FUNCION PARA DEFINIR AL GANADOR ALEATORIAMENTE
#############################################################################
def resultado_de_la_partida(lista_match: list):
    resultado_random = random.choice(lista_match)
    imprimir_header(" WINNER ")
    print(f"\n{resultado_random.obtener_nombre()}")
    return resultado_random

#############################################################################
# FUNCIONES PARA ACTUALIZAR PUNTOS, PARTIDAS, STATUS DE LOS JUGADORES
#############################################################################

def actualizar_puntos(lista_match: list, ganador):
    jugador_1 = lista_match[0]
    jugador_2 = lista_match[1]
    if ganador == jugador_1:
        jugador_1.actualizar_puntos(jugador_1.obtener_puntos() + 3)
        jugador_2.actualizar_puntos(jugador_2.obtener_puntos() + 1)
        print(f"{jugador_1.obtener_nombre()}: +3 pts")
        imprimir_header(" JUGADOR ELIMINADO ")
        print(f"{jugador_2.obtener_nombre()}: +1 pts")
    if ganador == jugador_2:
        jugador_1.actualizar_puntos(jugador_1.obtener_puntos() + 1)
        jugador_2.actualizar_puntos(jugador_2.obtener_puntos() + 3)
        print(f"{jugador_2.obtener_nombre()}: +3 pts")
        imprimir_header(" JUGADOR ELIMINADO ")
        print(f"{jugador_1.obtener_nombre()}: +1 pts")

    return lista_match

def actualizar_partidas(lista_match: list):
    jugador_1 = lista_match[0]
    jugador_2 = lista_match[1]
    jugador_2.actualizar_partidas(jugador_2.obtener_partidas() + 1)
    jugador_1.actualizar_partidas(jugador_1.obtener_partidas() + 1)

    return lista_match

def actualizar_status_de_jugadores(lista_match: list, ganador):
    jugador_1 = lista_match[0]
    jugador_2 = lista_match[1]
    if ganador == jugador_1:
        jugador_2.actualizar_status("INACTIVO")
    if ganador == jugador_2:
        jugador_1.actualizar_status("INACTIVO")

    return lista_match

#############################################################################
# FUNCION MENU PARA CREAR JUGADORES CON UN NUMERO VALIDO
#############################################################################
def menu_crear_jugadores():

    NUMERO_PARTICIPANTES = ["2", "4", "8", "16"]
    OPTIONS = ' | '.join(NUMERO_PARTICIPANTES)

    while True:
        eleccion = input(f"\nCuantos jugadores participan en el torneo?\n {OPTIONS}: ")
        if eleccion in NUMERO_PARTICIPANTES:
            return eleccion
        else:
            print(f"opcion no soportada: '{eleccion}'")


#############################################################################
# FUNCION DE SALIR
#############################################################################

def salir():
    print("Hasta la proxima!!")
    os.abort()

#############################################################################
# FUNCION PARA IMPRIMIR HEADER
#############################################################################

def imprimir_header(HEADER: str):
    print(F"\n{'*' * 40} {HEADER} {'*' * 40}")

def imprimir_header_menu(HEADER: str):
    print(F"\n{'>' * 50} {HEADER} {'<' * 50}")

#############################################################################
# FUNCION PARA ESCRIBIR DATOS EN UN ARCHIVO .TXT
#############################################################################
def guardar_en_archivo(diccionario: dict, campeon):

    with open("torneo.txt", "w") as file:
        file.write(f"{'-'*40} RESULTADOS DEL TORNEO {'-'*40}\n")
        file.write(f"El Campeon es: {str(campeon)}\n")
        file.write(f"{'-'*100}\n")
        for index, jugador in diccionario.items():
            file.write(f"[{index}] {repr(jugador)}\n")

def iniciar_torneo():
    imprimir_header(" TORNEO INICIADO ")
    JUGADORES_COPY = JUGADORES
    diccionario = {}
    cont = 1
    while True:
        for index,jugador in enumerate(JUGADORES):
            diccionario[index] = jugador
        lista_match = []
        lista_ganador = []
        for index, jugador in enumerate(JUGADORES):

            partidas_jugadas = diccionario[index].obtener_partidas()
            puntos_obtenidos = diccionario[index].obtener_puntos()
            status_actual = diccionario[index].obtener_status()

            if status_actual == 'ACTIVO' and jugador.obtener_status() == 'ACTIVO' and partidas_jugadas == jugador.obtener_partidas() and puntos_obtenidos == jugador.obtener_puntos():

                if len(lista_match) < 2:
                    lista_match.append(jugador)
                if len(lista_match) == 2:
                    jugador_1 = lista_match[0]
                    jugador_2 = lista_match[1]
                    imprimir_match(jugador_1, jugador_2, cont)
                    ganador = resultado_de_la_partida(lista_match)
                    lista_ganador.append(ganador)
                    actualizar_puntos(lista_match, ganador)
                    actualizar_partidas(lista_match)
                    actualizar_status_de_jugadores(lista_match, ganador)
                    diccionario[index] = jugador#[jugador.obtener_partidas(), jugador.obtener_puntos(), jugador.obtener_status()]
                    lista_match.clear()

        if len(lista_ganador) != 0:
            imprimir_header(" PASAN A LA SIGUIENTE RONDA ")
            print(lista_ganador)
            if len(lista_ganador) == 1:
                imprimir_header(" GANADOR FINAL ")
                print(lista_ganador[0].obtener_nombre())
                print(lista_ganador)
                campeon = lista_ganador[0].obtener_nombre()
                guardar_en_archivo(diccionario, campeon)
                break
        cont += 1



##########################################################################################
# CONTROL PRINCIPAL
# CREO EL MENU QUE LO CONTROLARA EL TORNEO
# USANDO UN DICCIONARIO, LA LLAVE ES LA ACCION Y EL VALOR ES EL NOMBRE DE LA FUNCION QUE DEFINIMOS
##########################################################################################
JUGADORES = []

MENU = {
    "registrar": crear_jugador,
    "iniciar": iniciar_torneo,
    "salir": salir
}

OPTIONS = ' | '.join(MENU.keys())  # alta | buscar por nombre | mostrar todos | mostrar por estado

while True:
    imprimir_header_menu(" MENU DEL TORNEO ")
    action = input(f"\nQue accion deseas realizar?\n {OPTIONS}: ").lower()
    if action in MENU.keys():
        MENU[action]()
    else:
        print(f"Accion no soportada: '{action}'")
