print()
print("--------------------------------------------")
print("-----------Calcular Notas-------------------")
print("--------------------------------------------")
print()

#Input

R = int(input("Ingrese su codigo: "))
X = int(input("Ingrese la primera nota: "))
Y = int(input("Ingrese la segunda nota: "))
Z = int(input("Ingrese la tercera nota: "))

# Procesing

K = (X+Y+Z)/3

#Output

A = input("Su codigo es: " + str(R) + " y su nota final es: " + str(K))