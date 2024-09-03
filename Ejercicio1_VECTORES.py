# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 08:33:12 2024

@author: KryonyxIntegrator
"""

#HALLANDO LA VARIANZA DE UNOS DATOS

cantidad= int(input("ingrese el tamaño de la pobacion"))
datos= []
for i in range (cantidad):
    datos.append(float(input("ingrese el dato"))) #se va agregando a la lista lo que tengo en pantalla 
x_barra= sum(datos)/cantidad #sacando promedio
varianza=0
for i in range (cantidad):
    varianza += (datos[i]-x_barra)**2
varianza=varianza/cantidad
print("la varianza es igual a", varianza)

#HALLANDO LA DESVIACION TIPICA 

