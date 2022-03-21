print("Ingresar búsqueda")
"""description=input()#ingresa palabras clave
#print(description+":)")
print("buscar en el repositorio")
if description=="Química":
    print("Encontrar autor")
    print("Ingrese autor:")
    authorTest=input()
    if authorTest=="Muñoz, Daniel":
        print("Traiga autor")
    else: 
        print("Se va a hacer otra comparación")

else:
    print("Rehaga la búsqueda")"""
description=""
while description!="Química":
    description=input()
    print("Rehaga la búsqueda")

print("buscar en el repositorio")
print("Encontrar autor")
print("Ingrese autor:")
authorTest=input()
if authorTest=="Muñoz, Daniel":
    print("Traiga autor")
else: 
    print("Se va a hacer otra comparación")



