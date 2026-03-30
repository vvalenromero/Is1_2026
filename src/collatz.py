import matplotlib.pyplot as plt

def contar_iteraciones(n):
    iteraciones = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iteraciones += 1
    return iteraciones

# Listas para almacenar los datos del gráfico
numeros_n = []
iteraciones_lista = []

# Calcular para cada número entre 1 y 10000
print("Calculando secuencias de Collatz...")
for i in range(1, 10001):
    numeros_n.append(i)
    iteraciones_lista.append(contar_iteraciones(i))

# Generar el gráfico
plt.figure(figsize=(10, 6))
plt.scatter(numeros_n, iteraciones_lista, s=1) # Usamos scatter para puntos pequeños
plt.title("Conjetura de Collatz: Iteraciones para converger a 1")
plt.xlabel("Número inicial (n)")
plt.ylabel("Iteraciones")
plt.grid(True)
plt.show()