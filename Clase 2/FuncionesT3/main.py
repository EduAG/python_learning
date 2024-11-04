# Author: Eduardo Alvarez
# mail: jesus.e.alvarez@gmail.com
# Date: 01/08/2024
# linkedin: www.linkedin.com/in/jesus-eduardo-alvarez-garcia

"""
Crear una calculadora básica que  realice operaciones aritméticas simples como suma, resta, multiplicación y división.

""" 
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    if b == 0:
       print("Error division por cero no es posible") 
    else:
        return a/b
    
def calculadora():
    opcion = input("Selecciona la opcion: \n1- Suma. \n2- Resta. \n3- Multiplicacion. \n4- Division. ")

    a = float(input("propociona el primer valor: "))
    b = float(input("proporcione el segundo valor: "))

    if opcion in ['1','2','3','4']:
        
        if opcion == '1':
            print(f"\n\nEl resultado de la suma es : {suma(a,b)}")
            calculadora()

        if opcion == '2':
            print(f"\n\nEl resultado de la suma es : {resta(a,b)}")
            calculadora()

        if opcion == '3':
            print(f"\n\nEl resultado de la suma es : {mult(a,b)}")
            calculadora()

        if opcion == '4':
            print(f"\n\nEl resultado de la suma es : {div(a,b)}")
            calculadora()


calculadora()

