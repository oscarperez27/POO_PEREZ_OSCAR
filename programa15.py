lista=[11,19,18,15,20,17,16,20]
mayores=[]
menores=[]
for numero in lista:
    if numero>=18:
        mayores.append(numero)
    else:
        menores.append(numero)
print("Esta es la lista de 18 o mayores de 18", mayores)
print("Esta es la lista de menores de 18", menores)



