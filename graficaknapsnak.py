import matplotlib.pyplot as plt

# Datos
num_pruebas = list(range(1, 17))
tiempos = [
    0.19144630432128906, 0.39016270637512207, 0.8189573287963867, 1.737415075302124,
    3.508319854736328, 7.070533514022927, 14.706350088119507, 30.32568097114563,
    63.06303596496582, 131.48418354988098, 267.3510413169861, 556.9714482784271,
    1178.411140680313, 2360.5474302768707, 4943.029278993607, 15629.998626708984
]

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(tiempos, num_pruebas, marker='o', color='b', label="Número de pruebas")
plt.xscale("log")  # Escala logarítmica en el eje x para visualizar mejor

# Etiquetas
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Número de pruebas")
plt.title("Número de pruebas en función del tiempo de ejecución")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Mostrar gráfica
plt.show()
