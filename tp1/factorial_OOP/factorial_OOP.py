#!/usr/bin/python
import sys

class Factorial:
    def __init__(self):
        # El constructor puede estar vacío o inicializar variables si fuera necesario
        pass

    def calcular(self, n):
        # Esta es la lógica base del factorial
        if n < 0: return 0
        if n == 0: return 1
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

    def run(self, min_val, max_val):
        # Este es el método que pide el PDF
        print(f"Calculando factoriales de {min_val} a {max_val}:")
        for i in range(min_val, max_val + 1):
            print(f"Factorial {i}! es {self.calcular(i)}")

# --- Bloque principal para probar la clase ---
if __name__ == "__main__":
    # Creamos una instancia de la clase
    obj = Factorial()
    # Ejecutamos el método run
    obj.run(1, 10)