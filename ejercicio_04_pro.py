nom=input("Dame tu nombre: ")
num=input("Dame el nº de veces que quieres que lo repita: ")
while num.isdecimal()==False:
    print("No has introducido un número, prueba otra vez")
    num=input("Dame el nº de veces que quieres que lo repita: ")
num=int(num)
print((nom+"\n")*num)