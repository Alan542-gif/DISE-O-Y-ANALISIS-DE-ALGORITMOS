import matplotlib.pyplot as plt

# Frecuencia de palabras
frecuencia_ingles = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 
                     'H', 'R', 'D', 'L', 'C', 'U', 'M', 
                     'W', 'F', 'G', 'Y', 'P', 'B', 'V', 
                     'K', 'J', 'X', 'Q', 'Z']

def cargar_texto(archivo):
    with open(archivo, 'r') as f:
        return f.read()

def calcular_frecuencia(texto):
    frecuencias = {}
    total_letras = sum(1 for letra in texto if letra.isalpha())
    
    for letra in texto.upper():
        if letra.isalpha():
            frecuencias[letra] = frecuencias.get(letra, 0) + 1

    return sorted(frecuencias.items(), key=lambda x: x[1], reverse=True), total_letras

def crear_grafico(frecuencias):
    letras, cuenta = zip(*frecuencias)
    plt.figure(figsize=(10, 6))
    plt.bar(letras, cuenta, color='skyblue')
    plt.xlabel('Letras')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia de las letras en el texto')
    plt.show()

sustitucion = {
    'b': 'e', 'r': 't', 'u': 'a', 'i': 'o', 'c': 'n',
    'x': 'h', 'k': 'i', 'l': 's', 'p': 'l', 'a': 'r',
    't': 'f', 'w': 'd', 'y': 'w', 'n': 'm', 'z': 'c',
    'm': 'y', 'g': 'g', 'v': 'u', 'o': 'k', 'h': 'b',
    's': 'p', 'f': 'v', 'q': 'x', 'e': 'z', 'j': 'j',
    'd': 'q'
}

def descifrar_texto(texto, sustitucion):
    return ''.join(sustitucion.get(letra, letra.lower() if letra.isalpha() else letra) for letra in texto)

# Texto cifrado
texto_cifrado = cargar_texto('C:/Users/Alan Ayala/Documents/Python/DISEÑO Y ANALISIS DE ALGORITMOS/cifradosustitucion/texto/AYALA TRUJANO ALAN.txt')

# Calcular frecuencias de letras
frecuencias_letras, total = calcular_frecuencia(texto_cifrado)

# Descifrar el texto
texto_descifrado =  "It was only after the second (I had to understand that he was overextended), that they became aware of their capacity to control their own futures as effectively as they did the successful escape. It seemed their actions were taking them into an entirely different situation, for they became less certain of themselves, less sure of the terms they had previously made, and after their conversation they understood the inevitable link between their different paths that they had constructed for each other. Every new direction saw them seize the initiative, and one might argue that it was only a matter of time before a new chance arose, but I would also note that their progress was surprisingly swift in what was, in many respects, a new beginning.)"

print("Texto descifrado:", texto_descifrado)

# Crear gráfico de frecuencias
crear_grafico(frecuencias_letras)


