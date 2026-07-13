while exit != 'si':
    try:
        color = {1:'azul',2:'rojo',3:'verde',4:'amarillo',5:'rosa'}
        color_select = int(input("ColorSet"))
        if color_select <= 5:
            print (color[color_select])
        else:
            print ("Solo estan registrados los numeros del 1 al 5")
    except ValueError:
            print ("solo use numeros al seleccionar el color")
    except KeyError:
           print("solo inserte numeros del 1 al 5 , no ponga 0, numeros negativos ni cosas raras")
    exit = input("¿desea cerrar el programa?").lower()
