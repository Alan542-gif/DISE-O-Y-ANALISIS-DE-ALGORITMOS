def carga_palabras():
    archivo = open('C:/Users/Alan Ayala/Documents/Python/Tarea/tareacifrado/words.txt', 'r')    # Abre el archivo que contiene las palabras.
    renglon = archivo.readline()        # Lee una línea del archivo.
    palabras = renglon.split()          # Divide el contenido de la línea en una lista de palabras, eliminando los espacios.
    print(len(palabras), 'palabras leidas') # Muestra cuántas palabras se leyeron del archivo.
    return palabras

def carga_cifrado():
    archivo = open('C:/Users/Alan Ayala/Documents/Python/Tarea/tareacifrado/textoCifrado.txt', 'r') # Abre el archivo que contiene el texto cifrado.
    renglon = archivo.readline()            # Lee una línea del archivo.
    return renglon                          # Devuelve el contenido leído del archivo.

def cifra_cesar(cadena, llave):     # Aplica el cifrado César a la cadena dada usando una llave de desplazamiento.
    if llave < 0:                   # Asegura que la llave no sea negativa.
        llave = 26 - llave
    nuevaCadena = ""                # Se utiliza para almacenar el texto cifrado.
    alfabeto = 'abcdefghijklmnopqrstuvwxyz' # Define el alfabeto que se usará como referencia.
    for l in cadena:    # Recorre cada carácter de la cadena.
        if l in alfabeto:   # Si el carácter está en el alfabeto:
            posicionLetra = alfabeto.find(l)    # Obtiene la posición de la letra en el alfabeto.
            nuevaCadena = nuevaCadena + alfabeto[((posicionLetra+llave) % 26)]  # Desplaza la letra según la llave usando el módulo para asegurar que no exceda el rango.
        else:
            nuevaCadena = nuevaCadena + l # Si el carácter no es una letra del alfabeto, lo añade sin modificar.
    return nuevaCadena

def descifra_cesar(cadena, llave):  # Usa el cifrado César para descifrar el texto, invirtiendo el desplazamiento.
    return cifra_cesar(cadena, 26-llave)

def get_aciertos(listaPalabras, diccionario):   # Compara las palabras descifradas con las del diccionario para contar cuántas coinciden.
    numAciertos = sum(map(lambda palabra: palabra in diccionario, listaPalabras))
    return numAciertos

palabras = carga_palabras() # Carga el archivo con las palabras del diccionario.
cadena = carga_cifrado()    # Carga el archivo con el texto cifrado.
maxAciertos = 0             # Inicializa el número máximo de coincidencias encontradas.
posibleLlave = 0            # Inicializa la variable que almacenará la llave correcta.

for cont in range(26):  # Recorre todas las posibles llaves (de 0 a 25).
    cadenaCifrada = descifra_cesar(cadena, cont)    # Prueba descifrar el texto con la llave actual.
    listaCifrada = cadenaCifrada.split()            # Convierte el texto descifrado en una lista de palabras.
    numAciertos = get_aciertos(listaCifrada, palabras)  # Cuenta cuántas palabras coinciden con el diccionario.
    if numAciertos > maxAciertos:   # Si el número de coincidencias es mayor que el máximo anterior:
        maxAciertos = numAciertos   # Actualiza el máximo número de coincidencias.
        posibleLlave = 26 - cont    # Actualiza la llave correcta con base en el número de coincidencias.

print("La llave es", posibleLlave)  # Muestra la llave que se encontró.
print("El texto descifrado es:")    # Muestra el texto descifrado.
print(cifra_cesar(cadena, posibleLlave))  # Imprime el texto descifrado utilizando la llave correcta.
