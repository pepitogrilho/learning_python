# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:07:33 2021

@author: pepea
"""

edad = input ( print ("Dame tu edad  y te dire si puedes pasar") )

if type(edad) == int:

    if edad >= 18:
        
        print("Puedes pasar")
        
    else:
        
        print("No puedes pasar")  

else:
    
   print("Escribe un numero entero, te has quedado sin pasar por gilipollas")