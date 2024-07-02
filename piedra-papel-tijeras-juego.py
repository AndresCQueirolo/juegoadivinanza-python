#-------------------------------
# JUEGO PIEDRA PAPEL Y TIJERAS
#-------------------------------

nombre1 = input("Cómo se llama el jugador 1?: ")
nombre2 = input("Cómo se llama el jugador 2?: ")

jugador1 = input(f"Hola {nombre1}, ¿qué eliges? ¿piedra, papel o tijeras?: ")
jugador2 = input(f"Hola {nombre2}, ¿qué eliges? ¿piedra, papel o tijeras?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Ha sido un empate")
elif condicion1 or condicion2 or condicion3:
    print(f"Ha ganado {nombre1}")
else:
    print(f"Ha ganado {nombre2}")


# Desafío

# Se puede colocar el nombre en la segunda solicitud
# Lo ingresado por el usuario sea lowercase de tal forma de comparar minúsculas con minúsculas
# Más de un turno con el búcle while