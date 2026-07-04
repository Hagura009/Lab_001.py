x=("hoy es ")
y=("martes")
a=("lunes")
print(f" {x}{a} y mañana es {y}")#esto es una practica de interpolacion



H=11
D=2026
Prueba_1=f'''hoy sabado {H} de abril de {D} estoy haciendo una prueba practica de mi conocimiento actual de python que incluyen variables , la funcion print y los tipos de datos , actualmente solo eh profundisado en las cadenas y sus metodos'''
print("load 'Prueba_1'")
print(Prueba_1)
def Integrar_prueba ():
    prueba= f"mi primera prueba fue el sabado {H} de abril de {D}, hoy es 22/06/2026 y esta es una prueba de creacion de funciones"
    return prueba
Prueba2=Integrar_prueba()
print (Prueba2)
input("Prueba de contunuidad, escribe cualquier letra ")
no=0
while not no == 29:
    no=int(input("Numero de llamada:"))
else:
    print(f"Bienvenido No°{no}")
    #ojo con los errores de escrita, me demore mas corriguiendo los nombres de las variantes que estructurando el codigo
    #23/06/2026
 #modifique el codigo usando while, ahora si el usuario no esta registrado no puede entrar
 #27/06/2026
Solicitud_Prueba=int(input("Digite el modulo que quiere acceder"))
if Solicitud_Prueba > 10:
    print("el ultimo modulo publicado es el 10,este modulo aun no a sido publicado")
elif Solicitud_Prueba <= 3:
    print("tu no estuviste precente en esa prueba")
elif Solicitud_Prueba == 4:
    print ("""\n Matematica: 85
   lenguaje:65""")
elif Solicitud_Prueba == 5:
    print('''\n Historia:74
    Filosofia:45)''')
elif Solicitud_Prueba == 6:
    print('''\n Fisica:52
    Extracurricular=Ninguno''')
elif Solicitud_Prueba == 7:
    print ('''\n Educasion Civica:97
    Educasion Fisica:34)''')
elif Solicitud_Prueba >=8:
    print('''\nEn analisis''')
else:
    print("Error")
print (f"user No° {no}, Esperamos que el programa le fuera util")
FX=input ("¿le parecio util el aplicativo?")
if FX.lower()== 'si' :
    print (':)')
elif FX.lower()== "no":
    print ("tu tampoco eres muy util que digamos, asi que aguantese")
else:
    print ('Bueno, tampoco es que realmente leyeramos tus quejas')
cuenta =10
while cuenta  >= 0:
    cuenta = cuenta - 1
    print (cuenta)
else:
    print ("\n Good Bye")