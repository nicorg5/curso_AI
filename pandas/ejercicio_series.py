import pandas as pd

# Se crea y se muestra la serie
serie = pd.Series([1, 3, 5, 7, 9, 55])
print(f"La serie creada es: \n{serie}")

# Se agrega un elemento a la serie
serie = pd.concat([serie, pd.Series([11])], ignore_index=True)

# Se elimina un elemento de la serie
serie = serie.drop(1)

# Operaciones aritméticas a la serie
#Suma
suma_resultado = serie.sum()
#Resta
resta_resultado = serie.subtract(1)
#Multiplicación
multiplicacion_resultado = serie.multiply(2)
#Division
division_resultado = serie.divide(2)

# Resultados de cada operacion
print(f"Serie:\n{serie}\n")
print(f"Suma de la Serie: {suma_resultado}\n")
print(f"Serie restando 1:\n{resta_resultado}\n")
print(f"Serie multiplicada por 2:\n{multiplicacion_resultado}\n")
print(f"Serie dividida por 2:\n{division_resultado}\n")