
contactos=[]

def opcion_1():
    print("Agregar Contacto")
    nombre=input("Ingrese nombre\n> ")
    telefono=int(input("Ingrese telefono\n> "))
    correo=input("Ingrese Correo\n > ")
    contacto={"nombre":nombre,
              "telefono":telefono,
              "correo":correo
              }
    contactos.append(contacto)

    print("Contacto Agregado!")

def opcion_2():
    print("Lista Contactos")

    if len(contactos)==0:
        print("No existen contactos!, agruege al menos un contacto!")
    else:
        for x in contactos:
            print(f"Nombre: {x['nombre']} ")
            print(f"Telefono: {x['telefono']} ")
            print(f"Correo: {x['correo']} \n")
            


def opcion_3():
    pass

def opcion_4():
    pass

def validar_int(nro1):
    while True:
        try:
            nro1=int(input("> "))
            if nro1>0:
                break
            else:
                print("ERROR! ingrese una opcion Valida")     
        except:
            print("Error!, ingrese una opcion en numero ENTERO!")