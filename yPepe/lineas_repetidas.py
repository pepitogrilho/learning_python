import sys #hay qeu importar esta libreria
if len(sys.argv) == 3: #si la longitud es igual a 3 vamos bien , si no informamos del error
    texto = sys.argv[1] #el texto es el segundo argumento , porque el 0 es el nombre del programa

    repeticiones = int(sys.argv[2])#el tercer argumento es el numero de repeticiones
    for r in range(repeticiones):
        print(texto)
else:
    print("error, introduce los argumentos correctos")
    print("ejemplo: lineas_repetidas.py 'texto' 5")

