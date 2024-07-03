diccionario = {
    "papas" : 20,
    "refresco" : 18,
    "galletas" : 14,
    "pan" : 15
}
for precio in diccionario.values():
    print(precio)
    descuento=precio*0.9
    print("Este es el precio con descuento del 10%:", descuento)
