#!/usr/bin/python3

# Definición del rango de búsqueda
lower = 1   # Límite inferior del intervalo
upper = 500 # Límite superior del intervalo (se calcularán primos hasta el 500)

print("Prime numbers between", lower, "and", upper, "are:")

# Bucle principal que recorre cada número dentro del rango especificado
for num in range(lower, upper + 1):
   
   # De acuerdo a la definición matemática, los números primos deben ser mayores a 1
   if num > 1:
       # Bucle interno para verificar si el número actual (num) tiene divisores
       # Se busca desde 2 hasta el número anterior a 'num'
       for i in range(2, num):
           # Si el resto de la división es cero, significa que se encontró un divisor
           if (num % i) == 0:
               # El número no es primo, por lo tanto salimos del bucle interno
               break
       else:
           # Si el bucle 'for' termina sin ejecutar el 'break', el número es primo
           # Se procede a imprimir el número en la consola
           print(num)