# tipos de modulos
#
#   1. own modules
#   2. thirdy party modules --> https://pypi.org/
#   3. python modules --> https://docs.python.org/3/py-modindex.html
#

# # example 1 import module
import datetime 

print(datetime.date.today()) # imprime la fecha en formato AAAA-MM-DD
print(datetime.timedelta(minutes=70)) # convierte los minutos en horas con formato HH:MM:SS

# example 2 from module import
from datetime import timedelta, date
import fmath # own module
from fmath import add, substract
from colorama import Fore, Style, init

print(timedelta(minutes=70)) # convierte los minutos en horas con formato HH:MM:SS
print(date.today())

# import fmath 
fmath.add(1, 2)
fmath.substract(1, 2)

# from fmath import add, substract
add(3, 4)
substract(5, 2)

init(convert=True) # For Windows
print(Fore.RED + "Hello world")
