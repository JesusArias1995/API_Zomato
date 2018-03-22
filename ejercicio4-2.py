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

cont=0
menu="y"
while menu == "y":
        p2={"city_id":codigo, "start":cont, "count":"20"}
        rest=requests.get("https://developers.zomato.com/api/v2.1/search", params=p2, headers=h)
        if rest.status_code == 200:
                re=rest.json()
                print ("RESTAURANTES DE", ciudad.upper())
                for r in re["restaurants"]:
                        print (r["restaurant"]["name"])
        cont+=20
        menu=input("Quieres mostrar otros 20 restaurantes(y/n): ")
print("")

