#Edison Remache
# estudiante de primer semestre parealeo E

import numpy as np

# Definimos las constantes
ciudades = ['QUITO', 'RIOBAMBA', 'BABAHOYO']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4  # Número de semanas

# Creamos una matriz 3D con temperaturas fijas (ejemplo)
# Formato: [ciudad][día][semana]
temperaturas = np.array([
    [
        [20, 21, 19, 22],  # Ciudad A
        [23, 24, 22, 21],  # Ciudad A
        [18, 19, 20, 21],  # Ciudad A
        [25, 26, 24, 23],  # Ciudad A
        [27, 28, 26, 25],  # Ciudad A
        [30, 31, 29, 28],  # Ciudad A
        [22, 21, 20, 19]   # Ciudad A
    ],
    [
        [15, 16, 14, 15],  # Ciudad B
        [17, 18, 16, 15],  # Ciudad B
        [14, 15, 14, 13],  # Ciudad B
        [19, 20, 18, 17],  # Ciudad B
        [21, 22, 20, 19],  # Ciudad B
        [24, 25, 23, 22],  # Ciudad B
        [16, 15, 14, 13]   # Ciudad B
    ],
    [
        [30, 31, 29, 30],  # Ciudad C
        [32, 33, 31, 30],  # Ciudad C
        [29, 30, 28, 27],  # Ciudad C
        [35, 36, 34, 33],  # Ciudad C
        [37, 38, 36, 35],  # Ciudad C
        [40, 41, 39, 38],  # Ciudad C
        [32, 31, 30, 29]   # Ciudad C
    ]
])

# Calculamos y mostramos el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for semana in range(semanas):
        promedio = np.mean(temperaturas[i, :, semana])
        print(f"  Semana {semana + 1}: {promedio:.2f} °C")

