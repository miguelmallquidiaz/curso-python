# Conversor de una hora, minutos y segundos que se visualizar las horas en segundos

hora = int(input("Ingrese la hora: "))
minuto = int(input("Ingrese minutos: "))
segundo = int(input("Ingrese segundos: "))

# horas (60)> minutos (60)> seg
# horas para pasar a segundos se mult por 3600
# min para pasar a seg se mult por 60

hora_segundo = hora * 3600 + minuto * 60 + segundo

input(f'La hora en segundos es: {hora_segundo} s.')