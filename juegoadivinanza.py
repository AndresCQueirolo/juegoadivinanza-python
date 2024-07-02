#------------------------
# JUEGO DE ADIVINANZAS
#------------------------

import random

numero_secreto = random.randint(1, 100)
cant_intentos = 0
adivinado = False
cant_max_intentos = 5

print("¡Bienvenido al juego de adivinar el número secreto!\nSólo tienes 5 intentos\n")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("¡Game Over! No has podido adivinar dentro de los 5 intentos")
        break

    numero = int(input("Introduce un número de 1 al 99: "))

    if numero == numero_secreto:
        print("¡Felicitaciones!, has adivinado el número secreto")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
    cant_intentos += 1
  