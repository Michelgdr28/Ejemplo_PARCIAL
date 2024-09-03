# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 07:26:43 2024

@author: KryonyxIntegrator
"""

import pandas as pd
datos={"Nombres":["Simon","Pedro"],
       "Apellidos":["Perez","Hernandez"],
       "Carnet":["13846","48331"],
       "Programa":["Sistemas","Electronica"],
       "Promedio":[4.5,3.8],
       "Semestre":[5,7]}
tabla=pd.DataFrame(data=datos)
#print(tabla) #IMPRIME EL DATAFRAME
tabla.to_excel("estudiantes.xlsx",index=False) #ARCHIVO EXCEL
tabla.to_csv("estudiantes.csv",index=False) #ARCHIVO CSV (SEPARADO POR COMAS)
