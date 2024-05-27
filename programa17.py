def c_a_f(c):
    return (c * 9/5) + 32
def f_a_c(f):
    return (f - 32) * 5/9
while True:
    print("¿Que desea hacer?")
    print("1.- De Celsius a Fahrenheit")
    print("2.- De Fahrenheit a Celsius")
    print("3.- Salir")
    x = input("Ingrese el número de la opción deseada: ")
    if x == '1':
        c = float(input("Ingrese la temperatura en Celsius: "))
        print("La temperatura en Fahrenheit es:", c_a_f(c))
    elif x == '2':
        f = float(input("Ingrese la temperatura en Fahrenheit: "))
        print("La temperatura en Celsius es:", f_a_c(f))
    elif x == '3':
        print("Saliste del programa")
        break
    else:
        print("Ingrese 1, 2 o 3.")