import random
print("Programa piedra-papel-tijeras-lagarto-spock")
print("papel = 0")
print("spock = 1")
print("piedra = 2")
print("tijeras = 3")
print("lagarto = 4")

nombres =["papel", "spock", "piedra", "tijeras", "lagarto"]

usuario = int(input ("Escriba su eleccion (0, 1, 2, 3 o 4): "))
compu = random.randint(0,4)

print("Tu elegiste", nombres[usuario])
print("La computadora eligio", nombres[compu])

resultado = (usuario - compu) %5

if resultado == 0:
    print("Empate")
elif resultado  == 3 or resultado == 4:
    print("Ganaste")
else:
    print("Perdiste")
