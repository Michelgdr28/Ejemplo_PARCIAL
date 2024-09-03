# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 08:38:47 2024

@author: KryonyxIntegrator
"""

#RETO Crear diccionarios para una funcion que devuelva el nombre completo de un estudiante
estudiantes=[]
estudiantes.append({
    "Primer nombre":"Juan",
    "Segundo nombre":"Carlos",
    "Primer apellido":"Perez",
    "Segundo apellido":"Lopez",
})
estudiantes.append({
    "Primer nombre":"Maria",
    "Segundo nombre":"Jose",
    "Primer apellido":"Lopez",
    "Segundo apellido":"Giraldo",
})
def nombre_completo(estudiante):
    return estudiante["Primer nombre"]+" "+estudiante["Segundo nombre"]+" "+estudiante["Primer apellido"]+" "+estudiante["Segundo apellido"]
print(nombre_completo(estudiantes[1])) #Maria jose
print(nombre_completo(estudiantes[0])) #Juan Carlos 