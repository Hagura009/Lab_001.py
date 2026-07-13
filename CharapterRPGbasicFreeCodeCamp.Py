print("El nombre no puede ser mas mas largo que 10")
print("\n ay 7 puntos de estatus, la suma de las estadisticas tiene que ser exactamente 7")
print("""\n Estructura recomendada:
    *nombre*
    stat_1=3
    stat_2=2
    stat_3=2  """)
full_dot = '●'
empty_dot = '○'
def create_character (name,stat_1,stat_2,stat_3):
    if not isinstance(name,str):
        return 'The character name should be a string'
    if not name:
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if " " in name:
        return 'The character name should not contain spaces'
    if not isinstance (stat_1,int):
        return 'All stats should be integers'
    if not isinstance (stat_2,int):
        return 'All stats should be integers'
    if not isinstance (stat_3,int):
        return 'All stats should be integers'
    if stat_1 < 1 or stat_2 < 1 or stat_3 < 1:
        return 'All stats should be no less than 1'
    if stat_1 > 4 or stat_2 > 4 or stat_3 > 4:
        return 'All stats should be no more than 4'
    if stat_1 + stat_2 + stat_3 != 7:
        return 'The character should start with 7 points'
    linea_str = f"STR {full_dot * stat_1}{empty_dot * (10 - stat_1)}"
    linea_int = f"INT {full_dot * stat_2}{empty_dot * (10 - stat_2)}"
    linea_cha = f"CHA {full_dot * stat_3}{empty_dot * (10 - stat_3)}"  
    return f"{name}\n{linea_str}\n{linea_int}\n{linea_cha}"   
name=input('name: ')
B=int(input("stat_1: "))
C=int(input("stat_2: "))
D=int(input("stat_3: "))
Ch= create_character(name,B,C,D)
print(Ch)
#es un ejércicio de Freecodecamp, aunque lo modifique un poco añadiendo los input y imprimiendo el resultado 