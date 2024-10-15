import random
print("Programa piedra-papel-tijera")
print("papel = 0 ")
print("piedra = 1 ")
print("tijeras = 2 ")
nombres = ["papel", "piedra", "tijeras"]
usuario = input("escriba su eleccion (0,1 o 2):")
compu = random.choice(['0','1','2'])
print("la computadora eligio", nombres[int(compu)])
if usuario == compu:
    print("empater")
else:
    if usuario == '0' and compu =='1':
        print('usted gana')
    else:
        if usuario =='0' and compu == '2':
            print('gana la computadora')  
        else:
            if usuario == '1' and compu == '0':
                print ('gana la computadora')
            else:
                if usuario == '1' and compu == '2':
                    print('usted gana')
                else: 
                    if usuario == '2' and compu == '0':
                        print("usted gana")
                    else:
                        if usuario == '2' and compu == '1':
                            print(" gana la computadora")
                            