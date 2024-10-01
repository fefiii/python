#Este codigo es para comentar

def calcular_pagto (can, prent):
    pagto = can * prent
    return pagto


def nomape_clo (nombre, ape):
    NPclo = (nombre +" "+ ape)
    return NPclo

def cal_vuelto (x,i):
    vuelto = x - i
    return vuelto




print("Bienvenido a la fruteria y verdurelia de fefi")
print("")

#ingreso de nombre y apellido de vendedor
nomven = input("Ingrese su nombre: ")
print ("")

apeven = input("Ingrese su apellido: ")
print ("")


#ingreso de nombre del cliente
nombrecli = input("Ingrese el nombre del cliente: ")
print ("")

apecli= input("Ingrese el apellido del cliente: ")
print ("")


#ingreso la contidad a comprar por el cliente
cantidad = int(input("Ingrese cantidad que va comprar el cliente (en kgs): "))
print ("")
#ingreso de que comprara el usuario
productfv = input("ingrese la fruta o verdura que llevara el cliente: ")
print("")

#ingreso de valores 
precio = int (input("Ingrese el valor de la fruta o verdura: "))
print ("")

#ingreso de pago cliente
pagclin= int (input("Ingrese con cuanto va a pagar: "))
print("")



pago_total= calcular_pagto(cantidad, precio)


#ingreso de informacion
print("El total que pago el clientes es de ", calcular_pagto(cantidad, precio))

#Ingreso de funciones
print ("INFORMACIÓN")
print("El total a pagar es de: ", calcular_pagto(cantidad, precio))
print("El total a pagar es de: ", pago_total)
print("El vuelto es de: ", cal_vuelto(pagclin, pago_total ))
print("El nombre completo del cliente es: ",nomape_clo(nombrecli, apecli))
print("El nombre completo del vendedor es: ",nomape_clo(nomven, apeven))