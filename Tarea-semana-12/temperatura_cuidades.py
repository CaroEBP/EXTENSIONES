# Lista de ciudades
ciudades = ["Machala", "Ponce Enríquez", "El Guabo"]

# Lista de días
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Matriz 3D: temperaturas[ciudad][semana][día]
temperaturas = [
    [   # Machala
        [28, 29, 30, 29, 31, 32, 30],  # Semana 1
        [27, 28, 29, 28, 30, 31, 29],  # Semana 2
        [26, 27, 28, 27, 29, 30, 28],  # Semana 3
        [25, 26, 27, 26, 28, 29, 27]   # Semana 4
    ],
    [   # Ponce Enríquez
        [24, 25, 26, 25, 27, 28, 26],
        [23, 24, 25, 24, 26, 27, 25],
        [22, 23, 24, 23, 25, 26, 24],
        [21, 22, 23, 22, 24, 25, 23]
    ],
    [   # El Guabo
        [26, 27, 28, 27, 29, 30, 28],
        [25, 26, 27, 26, 28, 29, 27],
        [24, 25, 26, 25, 27, 28, 26],
        [23, 24, 25, 24, 26, 27, 25]
    ]
]

# Iterar sobre ciudades, semanas y días para mostrar datos y calcular promedios
for ciudad_idx, ciudad in enumerate(temperaturas):
    print(f"\n Ciudad: {ciudades[ciudad_idx]}")
    for semana_idx, semana in enumerate(ciudad):
        suma = 0
        for dia_idx, temp in enumerate(semana):
            print(f" Semana {semana_idx + 1}, {dias[dia_idx]}: {temp}°C")
            suma += temp
        promedio = suma / len(semana)
        print(f" Promedio semana {semana_idx + 1}: {promedio:.2f}°C")
        