def Herencia():
    return "Permite a una clase heredar atributos y metodos de otra clase."
def Abstraccion():
    return "Oculta los detalles complejos de la implementación y expone solo la funcionalidad esencial al usuario."
def Encapsulamiento():
    return "Agrupa los datos (atributos) y los métodos que operan sobre esos datos en una sola unidad llamada clase."
def Polimorfismo():
    return "Permite a objetos de diferentes clases ser tratados a través de una interfaz común, generalmente mediante un método con el mismo nombre pero implementaciones diferentes."

while True:
    print("¿Que desea saber?")
    print("1.- Que es Abstraccion")
    print("2.- Que es Encapsulamieto")
    print("3.- Que es Herencia")
    print("4.- Que es Polimorfismo")

    x = input("Ingrese el número de la opción deseada: ")
    if x == '1':
        print(Abstraccion())
    elif x == '2':
        print(Encapsulamiento())
    elif x == '3':
        print(Herencia())
    elif x == '4':
        print(Polimorfismo())
        break
    else:
        print("Ingrese 1, 2, 3 o 4.")