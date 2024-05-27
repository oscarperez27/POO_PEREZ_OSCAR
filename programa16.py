x=int(input("Ingresa el primer valor"))
y=int(input("Ingresa el segundo valor"))
z=int(input("Ingresa el tercer valor"))
if x>y and x>z:
    print("El primer valor es el mayor")
elif y>x and y>z:
    print("El segundo valor es el mayor")
else: 
    print("El tercer valor es el mayor")