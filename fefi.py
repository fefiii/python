#Este código es para comentar

#Creacion de la funcion PROMEDIO
#a, b, c son parametros
def promedio (a, b, c):
 prom = (a+b+c)/3
 return prom

def mejor_nota(a,b,c):
 mayor = max(a,b,c)
 return mayor

def peor_nota(a,b,c):
 menor= min(a,b,c)
 return menor

print("Bienvenido a python")
print("")

num1 = int(input("Ingrese primer numero: "))

num2 = int(input("Ingrese segundo numero: "))
num3 = int(input("Ingrese tercer numero: "))

print("El promedio es: ", promedio (num1, num2, num3))

n1 = 15
n2 = 30
n3 = 20
print("El promedio del PROGRAMADOR es: ", promedio (n1, n2, n3))

nota1 = float(input("Ingrese primera nota: "))
nota2 = int(input("Ingrese segunda nota: "))
nota3 = int(input("Ingrese tercera nota: "))

print("El promedio de NOTAS es: ", promedio (nota1, nota2, nota3))
print("La mejor nota es: ", mejor_nota(nota1, nota2, nota3))
print("La peor nota es: ", peor_nota(nota1, nota2, nota3))
