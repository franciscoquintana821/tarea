vehiculo = input("seleccione un vehiculo (moto, auto, camioneta): ") .lower()
horas= int(input("cuantas horas piensa dejarlo?: "))

if vehiculo == "moto":
    precio= 300
elif vehiculo == "auto":
    precio= 600
elif vehiculo == "camioneta":
    precio= 800 
else:
    precio=0
    print("variable incorrecta")

total= precio * horas
print(f"el valor del uso es {total}")

