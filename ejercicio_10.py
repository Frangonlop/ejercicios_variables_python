# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión. Fórmula de interés compuesto: Para realizar el cálculo interés compuesto se utiliza esta fórmula: Cn= C0 (1+i)n

quantity = float(input("Dime lo que quieres invertir: "))
years = int(input("Dime el número de años: "))
rate = float(input("Tipo de interés anual: "))/100

amount = quantity * (1+rate)**years

print("Terminas obteniendo " + str(amount))
