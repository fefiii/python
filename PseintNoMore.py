#Condicional Si
#Ingrese 5 ususarios
#Debe ingresar su nombre y el color de su alianza
#3 opciones: ROJO, AZUL y AMARILLO

print("Bienvenido al ANIVERSARIO INSUCO")
print("")
cont_rojo=0
cont_azul=0
cont_amarillo=0

def max_color(1,2,3,4,5):
    mayor = max (1,2,3,4,5)
    return mayor

def min_color(1,2,3,4,5):
    menor = min (1,2,3,4,5)
    return menor

#Ingreso de datos
#"USUARIO 1"

user1 = input ("Ingrese nombre del usuario 1: ")
color1 = input("Ingrese color de su alianza 1: ")
if(color1 =="rojo"):
    cont_rojo = cont_rojo + 1

if(color1 =="azul"):
    cont_azul = cont_azul + 1

if(color1 =="amarillo"):
    cont_amarillo = cont_amarillo + 1
    
#"USUARIO 2"

user2 = input ("Ingrese nombre del usuario 2: ")
color2 = input("Ingrese color de su alianza 2: ")
if(color2 =="rojo"):
    cont_rojo = cont_rojo + 1

if(color2 =="azul"):
    cont_azul = cont_azul + 1


if(color2 =="amarillo"):
    cont_amarillo = cont_amarillo + 1

#"USUARIO 3"

user3 = input ("Ingrese nombre del usuario 3: ")
color3 = input("Ingrese color de su alianza 3: ")
if(color3 =="rojo"):
    cont_rojo = cont_rojo + 1

if(color3 =="azul"):
    cont_azul = cont_azul + 1

if(color3 =="amarillo"):
    cont_amarillo = cont_amarillo + 1

#"USUARIO 4"

user4 = input("Ingrese nombre del usuario 4: ")
color4 = input("Ingrese color de su alianza 4: ")
if(color4 =="rojo"):
    cont_rojo = cont_rojo + 1

if(color4 =="azul"):
    cont_azul = cont_azul + 1

if(color4 =="amarillo"):
    cont_amarillo = cont_amarillo + 1

#"USUARIO 5"

user5 = input ("Ingrese nombre del usuario 5: ")
color5 = input("Ingrese color de su alianza 5: ")
if(color5 =="rojo"):
    cont_rojo = cont_rojo + 1

if(color5 =="azul"):
    cont_azul = cont_azul + 1

if(color5 =="amarillo"):
    cont_amarillo = cont_amarillo + 1

print("La cantidad de usuarios ROJOS es ", cont_rojo)
print("La cantidad de usuarios AZULES es ", cont_azul)
print("La cantidad de usuarios AMARILLOS es ", cont_amarillo)

print("hay mas cantidad de la alianza del color: ", max_color(1,2,3,4,5))
print("hay menos cantidad de la alianza del color: ", min_color(1,2,3,4,5))
