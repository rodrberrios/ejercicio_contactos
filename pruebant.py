from funciones import *

import time, os

os.system("cls")


while True:
    print("""
Menu Concactos

1. Agregar 
2. Mostrar 
3. Guardar Archivo
4. Salir

Ingrese Opcion:""")
    validar_int()
    menu= validar_int


    if menu==1:
        opcion_1()
    elif menu==2:
        opcion_2()
    elif menu==3:
        opcion_3()
    elif menu==4:
        opcion_4()