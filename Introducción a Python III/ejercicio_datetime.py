from datetime import datetime

# Se crea una fecha actual
fecha_fundacion_celta = datetime(1923, 8, 23)

# Se saca el día de la semana
dia_semana = fecha_fundacion_celta.weekday()

# Bucle if para sacar el día de la semana 
if dia_semana == 0:
    print('El Celta de Vigo se fundó un lunes')
elif dia_semana == 1:
    print('El Celta de Vigo se fundó un martes')
elif dia_semana == 2:
    print('El Celta de Vigo se fundó un miércoles')
elif dia_semana == 3:
    print('El Celta de Vigo se fundó un jueves')
elif dia_semana == 4:
    print('El Celta de Vigo se fundó un viernes')
elif dia_semana == 5:
    print('El Celta de Vigo se fundó un sábado')
elif dia_semana== 6:
    print('El Celta de Vigo se fundó un domingo')
