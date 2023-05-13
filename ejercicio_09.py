# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales. El usuario podrá poner el peso y la altura con . o con , en los decimales

height = input("Dime tu altura en metros, por ejemplo 1.7: ")
height = height.replace(',', '.')
clean_height = height.replace('.', '')

while(clean_height.isnumeric() == False):
    print("No has introducido un valor correcto. Vuelve a intentarlo: ")
    height = input("Dime tu altura en metros: ")
    height = height.replace(',', '.')
    clean_height = height.replace('.', '')

height = float(height)


weight = input("Dime tu peso en kg: ")
weight = weight.replace(',', '.')
clean_weight = weight.replace('.', '')
while(clean_weight.isnumeric() == False):
    print("No has introducido un valor correcto. Vuelve a intentarlo: ")
    weight = input("Dime tu peso en kg: ")
    weight = weight.replace(',', '.')
    clean_weight = weight.replace('.', '')

weight = float(weight)

imc = weight/height**2
imc = round(imc, 2)

print("Tu IMC es: " + str(imc))
