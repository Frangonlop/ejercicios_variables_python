# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

price_today = 3.49
price_offer = price_today - price_today*60/100

n_today = input("Número de barras de hoy: ")
while n_today.isdecimal()==False:
    print("No has introducido un número de barras, vuelve a probar")
    n_today = input("Número de barras de hoy: ")

n_today=int(n_today)

n_offer = input("Número de barras de ayer: ")
while n_offer.isdecimal()==False:
    print("No has introducido un número de barras, vuelve a probar")
    n_offer = input("Número de barras de ayer: ")

n_offer = int (n_offer)

total = round(n_today*price_today+n_offer*price_offer, 1)
print("El total es: " + str(total))
