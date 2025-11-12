import requests
import tkinter as tk
from tkinter import messagebox
#Back-End
def obtine_vreme():
    oras = entry_oras.get()
    if not oras:
        messagebox.showwarning("ATENTIE","Te rog sa introduci un nume de oras")
        return

    API_KEY = "xxx"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parametrii ={
        "q" : oras,
        "appid": API_KEY,
        "units": "metric",
        "lang" : "ro"
    }
    try:
        raspuns = requests.get(URL, params=parametrii)
        data = raspuns.json()
        if raspuns.status_code == 200:
            descriere = data["weather"][0]["description"]
            temperatura = data["main"]["temp"]
            label_oras_val.config(text=oras)
            label_descriere_val.config(text=descriere)
            label_temperatura_val.config(text=temperatura)
        else:
            messagebox.showerror("ERROARE","NU AM GASIT ORASUL")

    except Exception as e:
        messagebox.showerror("EROARE",f"A aparut problema: \n{e}")
        
def obtine_vremea_in_fisier():
    oras = entry_oras.get()
    if not oras:
        messagebox.showwarning("ATENTIE","Te rog sa introduci un nume de oras")
        return
    API_KEY = "xxx"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parametrii ={
        "q" : oras,
        "lang" : "ro",
        "appid": API_KEY,
        "units": "metric"
        
    }
    try:
        raspuns = requests.get(URL, params=parametrii)
        data = raspuns.json()
        if raspuns.status_code == 200:
            contiunt_fisier = f"Oras: {oras}: \nStarea vremii: {data["weather"][0]["description"]}\nTemperatura: {data["main"]["temp"]}"
            with open (f'C:\\Users\\Florin\\Desktop\\MAP\\vreme_{oras}.txt','w') as f:
                 f.write(contiunt_fisier)

        else:
            messagebox.showerror("ERROARE","NU AM GASIT ORASUL")
    except Exception as e:
        messagebox.showerror("EROARE",f"A aparut problema: \n{e}")


    



#Partea Vizuala a aplicatiei (Front-End)
root = tk.Tk()
root.title("Starea vremii folosind OpenWeahter API")
root.geometry("400x350")
root.config(padx=20,pady=20)
tk.Label(root, text = "Introdu numele orasului: ", font = ("Arial", 12)).pack()
entry_oras = tk.Entry(root, font = ("Arial",12),justify="center")
entry_oras.pack(pady=10)

#De pus comanda pentru buton
tk.Button(root,text="Afiseaza vremea", font=("Arial", 12), command=obtine_vreme).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)
tk.Label(frame, text="Oras",font=("Arial", 12)).grid(row=0,column=0, sticky="e")
tk.Label(frame, text="Vreme",font=("Arial", 12)).grid(row=1,column=0, sticky="e")
tk.Label(frame, text="Temperatura",font=("Arial", 12)).grid(row=2,column=0, sticky="e")
label_oras_val = tk.Label(frame, text="-")
label_oras_val.grid(row=0,column=1)

label_descriere_val = tk.Label(frame, text="-")
label_descriere_val.grid(row=1,column=1)

label_temperatura_val = tk.Label(frame, text="-")
label_temperatura_val.grid(row=2,column=1)

tk.Button(root,text="Afiseaza vremea in fisier", font=("Arial", 12), command=obtine_vremea_in_fisier).pack(pady=10)



root.mainloop()
