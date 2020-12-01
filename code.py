#Piedra, Papel o Tijera

#Pedir elección de jugador 1
eleccionJugador1 = input("Jugador 1 elija Piedra, Papel o Tijera ->").lower()

#Verificar que la opción sea valida
while (eleccionJugador1 != "piedra" and eleccionJugador1 != "papel" and eleccionJugador1 != "tijera") :
    print("Eso no es una opción, intenta de nuevo.")
    eleccionJugador1 = input("Jugador 1 elija Piedra, Papel o Tijera ->").lower()

#Pedir elección de jugador 2
eleccionJugador2 = input("Jugador 2 elija Piedra, Papel o Tijera ->").lower()

#Verificar que la opción sea valida
while (eleccionJugador2 != "piedra" and eleccionJugador2 != "papel" and eleccionJugador2 != "tijera") :
    print("Eso no es una opción, intenta de nuevo.")
    eleccionJugador2 = input("Jugador 2 elija Piedra, Papel o Tijera ->").lower()

#Comparar elecciones y declarar ganador
if eleccionJugador1 == "piedra" and eleccionJugador2 == "papel" :
    print("Jugador 2 gana!")
elif eleccionJugador1 == "piedra" and eleccionJugador2 == "tijera" :
    print("Jugador 1 gana!")
elif eleccionJugador1 == "papel" and eleccionJugador2 == "tijera" :
    print("Jugador 2 gana!")
elif eleccionJugador1 == "papel" and eleccionJugador2 == "piedra" :
    print("Jugador 1 gana!")
elif eleccionJugador1 == "tijera" and eleccionJugador2 == "piedra" :
    print("Jugador 2 gana!")
elif eleccionJugador1 == "tijera" and eleccionJugador2 == "papel" :
    print("Jugador 1 gana!")
else :
    print("Empate!")