import math

radio = float(input("ingrese el valor"))
height = float(input("ingrese el valor"))
volume = math.pi * radio**2 * height 
area = 2 * math.pi * radio * height + 2 * math.pi * radio**2
print("el volumen del cilindro es:", volume)
print("el area es:", area)