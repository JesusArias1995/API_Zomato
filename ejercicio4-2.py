import requests
import os

ciudad=input("Introduce el nombre de una ciudad: ")

key=os.environ["key"]
p={"query":ciudad}
h={"Accept":"application/json", "user-key":key}

r=requests.get("https://developers.zomato.com/api/v2.1/locations", params=p, headers=h)

if r.status_code == 200:
        do=r.json()
        for i in do["location_suggestions"]:
                codigo=i["entity_id"]
print ("")

print("ORDENAR POR CRITERIO")
print("1. Costo")
print("2. Clasificación")
print("3. Recientemente agregado")
opcion=input("Elige el numero de opcion que desea realizar: ")
print("1. Ascendente")
print("2. Descendente")
ord=input("Elige el numero de ordenacion que desea filtrar: ")

if opcion=="1":
	sort="cost"
if opcion=="2":
	sort="rating"
if opcion=="3":
	sort="real_distance"
if ord=="1":
	order="asc"
if ord=="2":
	order="desc"

cont=0
menu="y"
while menu == "y":
        p2={"city_id":codigo, "start":cont, "count":"20", "sort":sort, "order":order }
        rest=requests.get("https://developers.zomato.com/api/v2.1/search", params=p2, headers=h)
        if rest.status_code == 200:
                re=rest.json()
                print ("RESTAURANTES DE", ciudad.upper())
                for r in re["restaurants"]:
                        print (r["restaurant"]["name"])
        cont+=20
        menu=input("Quieres mostrar otros 20 restaurantes(y/n): ")
print("")

