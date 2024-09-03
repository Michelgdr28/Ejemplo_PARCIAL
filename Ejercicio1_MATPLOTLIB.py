# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 08:20:08 2024

@author: KryonyxIntegrator
"""
#GRAFICAR CIRCULO
import matplotlib.pyplot as plt
import numpy as np
t=np.linspace(0,2*np.pi,100)
x=np.cos(t)
y=np.sin(t)
plt.plot(x,y)
plt.gca().set_aspect('equal',adjustable='box')
plt.show()

#USANDO EL MISMO CODIGO GRAFICAR CURVAS DE LISSAJOUS
import matplotlib.pyplot as plt
import numpy as np
t=np.linspace(0,2*np.pi,400)
a=7
b=5
x=np.cos(a*t)
y=np.sin(b*t)
plt.plot(x,y)
plt.gca().set_aspect('equal',adjustable='box')
plt.show()
