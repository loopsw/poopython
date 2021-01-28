import time;
from datetime import date
num = 20
year = date.today()
stringAge = "Tengo {} años, la fecha actual es: {}"

print(stringAge.format(num,'->'),year)

# timestamp to datetime
timestamp = 1528797322
dateFromTimestamp = date.fromtimestamp(timestamp)
print(dateFromTimestamp)

# use time module in python
currentTimeinTimestamp = time.time()
print(" El tiempo transcurrido desde 01/01/1970 es {} segundos".format(currentTimeinTimestamp))
myTimestamp = 1545925769.9618232
localTimeFromTimestamp = time.ctime(myTimestamp) 
print("De {}, el tiempo local es {}".format(myTimestamp,localTimeFromTimestamp))

# struct time
print("hora actual: ", time.time())

result = time.localtime(time.time())
print("Estructura de la hora ",result)
print("Año: ", result.tm_year)
print("Minuto: ",result.tm_min)
print("Segundo: ",result.tm_sec)

timeInTuple = time.localtime()
timeString = time.strftime("%d/%m/%Y, %H:%M:%S")
print(timeInTuple)
print(timeString)
print(timeInTuple.tm_wday)