# Programa 1: Búsqueda en Arreglo Multidimensional
# Autora: Carolina Elizabeth Balcázar Pardo

# Paso 1: Definir la matriz 3x3
matriz = [
    [4, 7, 2],
    [9, 1, 5],
    [6, 3, 8]
]

# Paso 2: Mostrar la matriz al usuario
print(" Matriz actual:")
for i, fila in enumerate(matriz):
    print(f"Fila {i}: {fila}")

# Paso 3: Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición si se encuentra
    return None  # Si no se encuentra

# Paso 4: Solicitar el valor a buscar
entrada = input("\n🔍 Ingresa el número que deseas buscar: ")

# Validar que sea un número entero
if entrada.isdigit():
    numero = int(entrada)
    posicion = buscar_valor(matriz, numero)

    # Paso 5: Mostrar el resultado
    if posicion:
        print(f" El número {numero} se encuentra en la posición: fila {posicion[0]}, columna {posicion[1]}.")
    else:
        print(f" El número {numero} no está en la matriz.")
else:
    print(" Entrada inválida. Por favor ingresa un número entero.")