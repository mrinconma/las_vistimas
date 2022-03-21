import json

def inputData(type):
    year = input("Ingrese año: ")
    title = input("Ingrese título: ")
    city = input("Ingrese ciudad: ")
    publisher = input("Ingrese editorial: ")
    returnJson='{​​"year":'+year+',"title":'+title+'"city":'+city+'"publisher":'+publisher+'}​​​'
    
condition = int(input("Ingrese los datos solicitados para generar la cita de un libro según las opciones: 1. autor personal, 2. autor Institucional, 3. sin autor"))
if condition==1:
    lastName = input("Ingrese los apellidos: ")
    initialName = input("Ingrese iniciales del nombre seguido de punto: ")
    year = input("Ingrese año: ")
    title = input("Ingrese título: ")
    city = input("Ingrese ciudad: ")
    publisher = input("Ingrese editorial: ")
    print (" (" + lastName + ", "  + year + ").")
    print(lastName + ", " + initialName +" (" + year + "). " + title +  ". " + city + ". " + publisher + ".")
elif condition==2:
    print("Ingrese los datos solicitados: ")
    corporativeName = input("Ingrese Institución: ")
    year = input("Ingrese año: ")
    title = input("Ingrese título: ")
    city = input("Ingrese ciudad: ")
    publisher = input("Ingrese editorial: ")
    print (" (" + corporativeName + ", "  + year + ").")
    print(corporativeName +" (" + year + "). " + title +  ". " + city + ". " + publisher + ".")
elif condition==3:
    print(3)
    print("Ingrese los datos solicitados: ")
    title = input("Ingrese título: ")
    year = input("Ingrese año: ")
    city = input("Ingrese ciudad: ")
    publisher = input("Ingrese editorial: ")
    print (" (" + title + ", "  + year + ").")
    print(title +" (" + year + "). " + city + ". " + publisher + ".")
else: 
    print("error en el ingreso de datos, ")
