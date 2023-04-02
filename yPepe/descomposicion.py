import sys

print(sys.argv)

if len(sys.argv) == 2:
     numero = int(sys.argv[1])
     input(numero)
     if numero < 0 or numero > 9999:
         print("error - numero desconocido")
         print("ejemplo: descomposicion.py [0-9999]")
     else:
         cadena = str(numero)
         longitud = len(cadena) 

         for i in range(longitud):
             print("{:04d}".format( int(cadena[longitud-1-i]) * 10 ** i)) 
else:
     print("error - argumentos desconocidos") 
     print("ejemplo: descomposicion.py .[0-9999]")        