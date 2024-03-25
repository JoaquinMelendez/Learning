hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Calcula la hora de salida sumando las horas y redondeando los minutos
hour_salida = (hour+(dura+mins)//60)%24
mins_salida = (dura+mins)%60

print("Su hora de salida es: ", hour_salida, ":", mins_salida)
