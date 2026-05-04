# def saludar(nombre):
#     print("hola", nombre)

# saludar("ana")
# saludar("juan")



# def sumar(a,b):
#     return a + b
# resultado = sumar(10, 20)
# print(resultado)



# def multiplicar(a, b):
#     return a * b
# resultado = multiplicar(4, 3)
# print("el resultado es", resultado)



# def es_mayor_de_edad(edad):
#     return edad >= 18



# while True:
#     try:
#         numero1 = int(input("ingrese un numero: "))
#         numero2 = int(input("ingrese otro numero: "))
#         print(numero1 / numero2)
#         salir = input("quieres continuar? s/n ").lower
#         if salir == "n".lower:
#             print("adios")
#             break
#         else:
#             continue
        
#     except ValueError:
#         print("debes poner un numero valido")
#     except ZeroDivisionError:
#         print("no se puede dividir por 0")
#         continue 



# try:
#     numero = int(input("numero: "))
# except ValueError:
#     print("numero invalidad")
# else:
#     print("todo a salido bien")
# finally:
#     print("fin del proceso")

# archivo = open("datos.txt", "w")
# with open("Datos.txt", "w", encoding="utf-8") as archivos:
#     archivo.write("\nxd")


# archivo = open("datos.txt", "a")
# with open("Datos.txt", "a", encoding="utf-8") as archivos:
#     archivo.write("\nxd\n")
# archivo = open("Datos.txt", "r")
# with open("datos.txt", "r", encoding="utf-8") as archivos:
#     contenido = archivo.read()
#     print(contenido)




# archivo = open("datos.txt", "r")
# with open("datos.txt", "r", encoding="utf-8")as archivos:
#     for linea in archivo:
#         print(linea.strip())



nombre = input("ingresa tu nombre: ")

with open("usuarios.txt", "a", encoding="utf-8") as archivo:
    archivo.write(nombre + "\n")
                
print("usuario creado")