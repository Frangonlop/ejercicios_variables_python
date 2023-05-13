# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.


hours = float(input("Dime el número de horas trabajadas: "))
price = float(input("Dime el precio por hora en euros: "))

amount = hours*price
print(type(amount))
print("La paga total es: " + str(amount))
