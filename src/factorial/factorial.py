#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# [Inferencia] Verificamos si se pasó un argumento
if len(sys.argv) < 2:
    entrada = input("No ingresó argumento. Por favor, ingrese el número o rango: ")
else:
    entrada = sys.argv[1]

