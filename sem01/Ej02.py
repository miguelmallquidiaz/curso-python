'''
Elaborar un script que permita ingresar la hora de partida de un avión comercial
horas, minutos y segundos. Si se conoce el tiempo de vuelo en segundos y mostrar
las horas de llegada. "Los aviones comerciales no deben pasar las 13 horas de vuelo"
'''

hora = int(input('Ingresar la hora de partida en horas [0..23]: '))
minuto = int(input('Ingresar la hora de partida en minutos [0..59]: '))
segundo = int(input('Ingresar la hora de partida en segundos [0..59]: '))

# horas que se sabe es de 13 h pasarlo a segundos es 13 * 3600 = 46800 como máximo
tv = int(input('Ingresar el tiempo de vuelo en segundo [1800..46800]: '))
# convertir el tiempo de vuelo a segundos y lo sumanos a la hora de partida inicial al tiempo de vuelo
tv += hora * 3600 + minuto * 60 + segundo
# calcular las horas de llegada
hora = tv // 3600 # Las horas totales
# calcular los minutos que llega
tv %= 3600 # Me da los segundos restantes
minuto = tv // 60 #Los minutos totales
# calculamos los segundos de llegada
segundo = tv - minuto * 60  

print(f'La hora de llegada es: {hora}:{minuto}:{segundo}')