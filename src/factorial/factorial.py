#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Función original para calcular el factorial
def factorial(num): 
    if num < 0: 
        print(f"Factorial de {num} (negativo) no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# 1. Si se omite el número como argumento, lo solicita (Punto 5.1 del PDF)
if len(sys.argv) < 2:
    entrada = input("Debe informar un número o rango (ej. 10 o 4-8): ")
else:
    entrada = sys.argv[1]

# 2. Lógica para aceptar rangos desde-hasta y rangos abiertos (Puntos 5.2 y 5.3 del PDF)
if "-" in entrada:
    partes = entrada.split("-")
    
    # Extraemos las partes del rango
    inicio_str = partes[0]
    fin_str = partes[1]

   
    inicio = int(inicio_str) if inicio_str != "" else 1
    fin = int(fin_str) if fin_str != "" else 60

    print(f"Calculando factoriales en el rango {inicio} hasta {fin}:")
    for i in range(inicio, fin + 1):
        print(f"Factorial {i}! es {factorial(i)}")

else:
    # 3. Caso de un solo número (especificación original)
    try:
        num = int(entrada)
        print(f"Factorial {num}! es {factorial(num)}")
    except ValueError:
        print("Error: Debe ingresar un número entero válido o un rango con el formato 'inicio-fin'.")

