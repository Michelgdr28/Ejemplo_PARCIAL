# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 07:52:32 2024

@author: KryonyxIntegrator
"""

import os 
os.system('cd .. ')
os.system('cd Ejemplo_PARCIAL.git')
os.system('cd EJERCICIOS_CLASE_ALG2')

for i in range (10):
    nombre='carpeta'+str(i)
    texto='mkdir'+'"'+ nombre +'"'
    print(texto)
    os.system(texto)
    