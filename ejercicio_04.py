# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

name = input("¿Cuál es tu nombre? ") + "\n"
veces = int(input("¿Cuántas veces quieres que te salude? "))

output = name*veces
print(output)
