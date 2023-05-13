# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

# Calculadora de la suma total de números naturales hasta un número concreto

n = input("Dime hasta qué número natural quieres sumar: ")

while n.isdecimal()==False:
    print("No has introducido un número natural, vuelve a probar")
    n = input("Dime hasta qué número natural quieres sumar: ")

n=int(n)
sum = int((n*(n+1)) / 2)
print("La sumatoria desde 0 hasta " + str(n) + " es igual a : " + str(sum))