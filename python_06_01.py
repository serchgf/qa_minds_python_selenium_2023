"""
Escribe un script que dado la edad de una persona y su altura pueda determinar si la misma puede o no subirse en la montaña rusa “Push-Pull”, dado que se debe ser mayor a 14 años y tener
una altura no menor de 1,62. El script debe ser capaz de informar si puede o no subirse y en el caso de que no, porque razon (Si por edad, por tamaño u ambas) (edited)
"""


edad = input("Dime tu edad: ")
altura = input("Dime tu estatura: ")
edad = int(edad)
altura = float(altura)



if edad>14 and altura>=1.62:
    print("si puedes subir al 'Push-Pull")
else:
    if edad<14 and altura<1.62:
        print(f'No puedes subir porque debes tener mas de 14 años y debes medir mas de 1.62')
    if edad<14 and altura>1.62:
        print(f'No puedes subir porque debes tener mas de 14 años')
    if edad>14 and altura<1.62:
        print(f'No puedes subir porque debes medir al menos 1.62')

