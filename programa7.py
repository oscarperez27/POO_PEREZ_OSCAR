x=float(input("Ingresa la cantidad de kg a comprar"))
if x<1:
    print("La cantidad a pagar son $50")
elif x<5:
    print("La cantidad a pagar son $100")
elif x<10:
    print("La cantidad a pagar son $200")
else:
    print("La cantidad a pagar son $500")