#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
import requests
import pandas as pd

with open (r'C:\\Users\\Florin\\Desktop\MAP\\API.txt') as f:
    API_KEY = f.read().strip()

print(f"Cheia ta API este: {API_KEY}")

city = input("Introdu numele orasului: ")
API_URL = "https://api.openweathermap.org/data/2.5/weather"

URL_request = f"{API_URL}?q={city}&appid={API_KEY}&units=metric"
raspuns = requests.get(URL_request)

if raspuns.status_code != 200:
    print("A aparut o eroare")
else:
    data = raspuns.json()
    # print(data)
    temperatura = data["main"]["temp"]
    vreme = data["weather"][0]["main"]
    print(f"Temperaura: {temperatura}")
    print(f"Vreme: {vreme}")

    contiunt_fisier = f"Oras: {city}: \nStarea vremii: {vreme}\nTemperatura: {temperatura}"

    with open ('C:\\Users\\Florin\\Desktop\\MAP\\starea_vremii.txt','w') as f:
        f.write(contiunt_fisier)

    df = pd.DataFrame(
        {
            'Oras:':[city],
            'Starea vremii:':[vreme],
            'Temperatura:':[temperatura]
        }
    )

    df.to_excel(f'C:\\Users\\Florin\\Desktop\\MAP\\vremea_in_{city}.xlsx',index=False)





