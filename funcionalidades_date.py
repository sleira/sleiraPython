# funcionalidades de date
from datetime import date
from datetime import datetime

# Dia actual
hoy = date.today()

# Fecha 
now = datetime.now()

print(hoy)
print("El dia de Hoy es {}".format(hoy.day))
print("El mes de Hoy es {}".format(hoy.month))
print("El año de Hoy es {}".format(hoy.year))

print(now)
print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))
