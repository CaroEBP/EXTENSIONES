# Programa: Ordenación de una fila específica en matriz bidimensional
# Autora: Carolina Elizabeth Balcázar Pardo

# Matriz 3x3 con valores numéricos
matriz = [
    [9, 3, 5],
    [7, 2, 8],
    [6, 4, 1]
]

# Mostrar la matriz original
print(" Matriz original:")
for i, fila in enumerate(matriz):
    print(f"Fila {i}: {fila}")

# Función que ordena una fila específica usando Bubble Sort
def ordenar_fila_bubble(matriz, fila_index):
    fila = matriz[fila_index]
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    matriz[fila_index] = fila
    return matriz

# Solicitar al usuario qué fila desea ordenar
indice = int(input("\n🔧 Ingresa el número de fila que deseas ordenar (0, 1 o 2): "))

# Validar el índice y aplicar la ordenación
if 0 <= indice < len(matriz):
    matriz_antes = matriz[indice].copy()
    matriz = ordenar_fila_bubble(matriz, indice)
    matriz_despues = matriz[indice]

    print(f"\n Fila {indice} ordenada:")
    print(f"Antes: {matriz_antes}")
    print(f"Después: {matriz_despues}")
else:
    print(" Índice inválido. Debe ser 0, 1 o 2.")

# Mostrar la matriz final
print("\n Matriz modificada:")
for i, fila in enumerate(matriz):
    print(f"Fila {i}: {fila}")