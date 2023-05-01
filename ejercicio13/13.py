import math
radio = float(input("ingrese el radio de la circunferencia"))
length = 2 * math.pi * radio 
area = math.pi * radio ** 2
enrolled_area =(math.pi * radio ** 2) / 2
print("el area es:", area)
print("la longitud:", length)
print("el area del circulo inscrito es:", enrolled_area)