"""
Pide al usuario dos variables a = 12 y b = 34, crea funciones que permitan calcular la suma, resta, multiplicación y división, como también el valor del módulo de b entre a
Crea un método que permita convertir cualquier numero entero y a flotante
Extra: Define una función para convertir de grados Celsius a Fahrenheit, pide al usuario que ingrese la temperatura en Celsius e imprima la conversión.
"""




def suma(num_1: int,  num_2: int):
    suma=num_1+num_2
    return suma

def resta(num_1: int,  num_2: int):
    resta=num_1-num_2
    return resta

def multiplicacion(num_1: int,  num_2: int):
    multiplicacion=num_1*num_2
    return multiplicacion

def division_entera(num_1: int,  num_2: int):
    division=num_1//num_2
    return division

def modulo(num_1: int,  num_2: int):
    modulo=num_1%num_2
    return modulo

def conversion_int_a_float(num_1: int, num_2: int):
    num_1 = float(num_1)
    num_2 = float(num_2)
    return num_1, num_2

def convertir_temperatura(temperatura: int):
    farenheit= (temperatura*1.8)+32
    return  farenheit

num_1 = input("Dame un numero entero: ")
num_2 = input("Dame un numero entero: ")
num_1 = int(num_1)
num_2 = int(num_2)

print(f'la suma es: {suma(num_1,num_2)}')
print(f'la resta es: {resta(num_1,num_2)}')
print(f'la multiplicacion es: {multiplicacion(num_1,num_2)}')
print(f'la entera es: {division_entera(num_1,num_2)}')
print(f'el modulo es: {modulo(num_1,num_2)}')
float_num_1, float_num_2= conversion_int_a_float(num_1, num_2)
print(f'numeros convertidos a flotantes: {float_num_1} y {float_num_2}')

celcius = input("Dame una temperatura en celcius: ")
celcius= float(celcius)

print(f'la temperatura en farenheit es: {convertir_temperatura(celcius)}')
