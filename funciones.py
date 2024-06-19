
contactos=[]

def opcion_1():
    print("Agregar Contacto")
    nombre= validar_nombre()
    telefono= validar_telefono()
    correo= validar_correo()
    contacto={"nombre":nombre,
              "telefono":telefono,
              "correo":correo
              }
    contactos.append(contacto)

    print("Contacto Agregado!")

def opcion_2():
    print("Lista Contactos")

    if validar_contactos:
        for x in contactos:
            print(f"Nombre: {x['nombre']} ")
            print(f"Telefono: {x['telefono']} ")
            print(f"Correo: {x['correo']} \n")
            


def opcion_3():
    if validar_contactos():
        nombre_archivo=input("Ingrese nombre del archivo\n> ")
        import csv
        with open(f"{nombre_archivo}.csv","w") as archivo:
            escritor= csv.DictWriter(archivo, ["nombre","telefono","correo"])
            escritor.writeheader()
            escritor.writerows(contactos)
        

def opcion_4():
    print("Adios")
    exit()



def validar_int(nro):
    while True:
        try:
            nro=int(input("> "))
            if nro>0:
                return nro
            else:
                print("ERROR! ingrese una opcion Valida")
                  
        except:
            print("Error!, ingrese una opcion en numero ENTERO!")
            

def validar_nombre():
    while True:
        nombre=input("Ingrese nombre\n> ")
        if len(nombre)>=3 and nombre.isalpha():
            return nombre
        else:
            print("Error, ingrese nombre valido")

def validar_telefono():
    while True:
        try:
            telefono= int(input("Ingrese telefono: "))
            if len(str(telefono))==9 and str(telefono)[0]=='9':
                return telefono
            else:
                print("Error! el telefono debe comenzar con 9 y tener 9 digitos")
        except:
            print("error")

def validar_correo():
    while True:
        correo=input("Ingrese correo: ")
        if correo.lower().endswith("@gmail.com") and len(correo.strip())>=13:
            return correo
        else:
            print("Error!, correo invalido")

def validar_contactos():
    if len(contactos)==0:
        print("No existen contactos!, agruege al menos un contacto!")
        return False
    return True