import pandas as pd

# Datos para la serie de temperaturas semanales en grados Celsius
serie_temperaturas = pd.Series([22, 24, 25, 21, 20, 23, 22])


# Datos para la serie de precipitación semanal en milímetros
serie_precipitacion= pd.Series([5, 10, 2, 15, 8, 3, 12])


# Operaciones de slicing en ambas series
#para obtener temperaturas de la tercera a la quinta semana
sliced_serie_temperaturas = serie_temperaturas[2:6]

#para obtener precipitaciiones de la tercera a la sexta semana
sliced_serie_temperaturas = serie_precipitacion[2:7]


# Combinación de las series resultantes del slicing en una nueva serie
combined_serie = pd.concat([sliced_serie_temperaturas, sliced_serie_temperaturas], ignore_index=True)


# Operaciones básicas en la Serie combinada
#suma
suma_combinada = combined_serie.sum()

#promedio
promedio_combinada = combined_serie.mean()


# 4. Mostrar resultados
print(f"Serie de temperaturas:\n{serie_temperaturas}\n")
print(f"Serie de precipitaciones):\n{serie_precipitacion}\n")
print(f"Slicing en serie de temperaturas (semana 3 a semana 5):\n{sliced_serie_temperaturas}\n")
print(f"Slicing en serie de precipitaciones (semana 3 a semana 6):\n{sliced_serie_temperaturas}\n")
print(f"Serie combinada:\n{combined_serie}\n")
print(f"Suma de la serie combinada: {suma_combinada}\n")
print(f"Promedio de la serie combinada: {promedio_combinada}\n")