num = float(input("ingrese un número: "))
try:
    print("5/",num,"=",5/num)
except ZeroDivisionError:
    print("Error al dividir por cero")
except ValueError:
    print("No es posiblre realizar la división")

