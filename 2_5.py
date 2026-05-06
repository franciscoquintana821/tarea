try:
    numero=int(input("coloque su numero: "))

    for i in range (1, numero + 1): 
        if i %2 != 0: 
            print(i)
except ValueError:
    print("ingresa un numero valido")