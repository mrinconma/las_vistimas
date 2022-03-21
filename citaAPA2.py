import json


global year
global title
global city
global publisher
global bandera

def autor_personal():
    print("\nOPCION MENU LIBRO PERSONAL\n\n")
    lastName = input("Ingrese los apellidos: ")
    initialName = input("Ingrese iniciales del nombre seguido de punto: ")
    year = input("Ingrese año: ")
    title = input("Ingrese título: ")
    city = input("Ingrese ciudad: ")
    publisher = input("Ingrese editorial: ")
    print (" (" + lastName + ", "  + year + ").")
    print(lastName + ", " + initialName +" (" + year + "). " + title +  ". " + city + ". " + publisher + ".")

def autor_Institucional():
    print("\nOPCION MENU LIBRO PERSONAL\n\n")
    corporativeName = input("Ingrese Institución: ")
    year = input("Ingrese año: ")
    title = input("Ingrese título: ")
    city = input("Ingrese ciudad: ")
    publisher = input("Ingrese editorial: ")
    print (" (" + corporativeName + ", "  + year + ").")
    print(corporativeName +" (" + year + "). " + title +  ". " + city + ". " + publisher + ".")

def sin_autor():
    print("\nOPCION MENU LIBRO PERSONAL\n\n")
    title = input("Ingrese título: ")
    year = input("Ingrese año: ")
    city = input("Ingrese ciudad: ")
    publisher = input("Ingrese editorial: ")
    print (" (" + title + ", "  + year + ").")
    print(title +" (" + year + "). " + city + ". " + publisher + ".")

def menu(opc):
    if opc  == 1:
        autor_personal()
    elif opc == 2:
        autor_Institucional()
    elif opc == 3:
        sin_autor()
    else:
        print("opcion no valida")

def validar_menu(opc):
    if opc < 4:
        menu(opc)
        op = int(input("\n1.Autor personal\n2.Autor corporativo\n3.Sin Autor\n0.Salir\n\nIngrese una opcion: "))
        validar_menu(op)

    else:
        print("\nopcion del menu no valida vuelva a intentar \n\n")
        op = int(input("\n1.Autor personal\n2.Autor corporativo\n3.Sin Autor\n0.Salir\n\nIngrese una opcion: "))
        validar_menu(op)


op = int(input("\n1.Autor personal\n2.Autor corporativo\n3.Sin Autor\n0.Salir\n\nIngrese una opcion: "))

if op == 0:
    print("Gracias por usar el sistema")
else:
    validar_menu(op)