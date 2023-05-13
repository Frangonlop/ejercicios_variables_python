# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

name = input("¿Cuál es tu nombre? ")
while name.isalnum()==False:
    print("No has intrdoducido nada, vuelve a probar")
    name=input("¿Cuál es tu nombre? ")
while name.isalpha()==False:
    print("No has introducido un nombre, vuelve a probar")
    name=input("¿Cuál es tu nombre? ")
print("¡Hola " + name + "!")
