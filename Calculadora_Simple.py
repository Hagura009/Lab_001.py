def sumar(num_1,num_2):
    return num_1+num_2
def restar (num_1,num_2):
    return num_1 - num_2
def multiplicar (num_1,num_2):
    return num_1 * num_2
def dividir (num_1,num_2):
    return num_1/num_2
def potencia (num_1,num_2):
   return num_1** num_2
a=int(input('num1'))
b=int(input('num2'))
solicitud=0
while not solicitud  or solicitud >5:
    try:
        solicitud =int(input('''cual funcion vas a probar?
dividir()-->1
sumar()-->2
restar()-->3
multiplicar()-->4
potencia()-->5
en caso de bucle:Asegurese de que sea un numero del 1 al 5, no 0, mayor que 5 o una letra
'''))
    except ValueError:
        print('Prueba con un numero entero')
    
if solicitud ==1:
    res=dividir(a,b)
elif solicitud == 2:
    res=sumar(a,b)
elif solicitud == 3:
    res=restar(a,b)
elif solicitud == 4:
    res=multiplicar(a,b)
elif solicitud == 5:
    res=potencia(a,b)
print (res)
R=str(input("¿volveras a hacer una operacion: si o no ")).lower()
#_______________________#
if R == 'si':
    solicitud = 0
    a=int(input('num1'))
    b=int(input('num2'))
    solicitud=0
    while not solicitud  or solicitud >5:
        try:
            solicitud =int(input('''cual funcion vas a probar?
dividir()-->1
sumar()-->2
restar()-->3
multiplicar()-->4
potencia()-->5
en caso de bucle:Asegurese de que sea un numero del 1 al 5, no 0, mayor que 5 o una letra
'''))
        except ValueError:
            print('Prueba con un numero entero')
    
    if solicitud ==1:
        res=dividir(a,b)
    elif solicitud == 2:
        res=sumar(a,b)
    elif solicitud == 3:
        res=restar(a,b)
    elif solicitud == 4:
       res=multiplicar(a,b)
    elif solicitud == 5:
       res=potencia(a,b)
    print (res)
else:
    print(":)")
#esta es una práctica rústica de creación de funciones y reutilización de codigo
#también aprendí a manejar tri/exept en este proyecto 
#4/07/2026