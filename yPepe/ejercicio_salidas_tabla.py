import sys
#el primer argumento es el propio nombre del fichero
if len(sys.argv) == 3:
	filas = int(sys.argv[1])
	columnas = int(sys.argv[2])
	if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
         print("Error - filas o columnas incorrectas")
         print("Ejemplo: tabla.py [1-9] [1-9]")	
         
    else:
         for f in range(filas):
             print("")
             for c in range(columnas):
       	   	     print(" * ", end  )
else:
    print("Error - Argumentos incorrectos")
    print("Ejemplo: tabla.py [1-9] [1-9]")



