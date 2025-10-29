from bs4 import BeautifulSoup
import requests
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
from email.mime.text import MIMEText


with open("C:\\Users\\Florin\\Desktop\\MAP\\parola.txt","r") as fisier_parola:
    parola_google = fisier_parola.read().strip()

email = 'pupzf53@gmail.com'
email_destinatar = 'pupzf53@gmail.com'

url = "https://www.digi24.ro/stiri?__grsc=cookieIsUndef0&__grts=58704408&__grua=cff107a2ea3b38ba389817f7e3b04607&__grrn=1"

def send_email():
    msg = MIMEText(f"Atentie! {titlu_stire()} \n {intro_stire()}")
    msg['Subject'] = 'Stire noua'
    msg['From'] = email
    msg['To'] = email_destinatar
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
        smtp_server.login(email,parola_google)
        smtp_server.sendmail(email,email_destinatar,msg.as_string())
    print("Email-ul a fost trimis cu succes!")

def afisare_totala():
    r = requests.get(url)
    continut_html = r.text
    with open("C:\\Users\\Florin\\Desktop\\MAP\\stiri.html","w", encoding="utf-8") as fisier:
        fisier.write(continut_html)

def titlu_stire():
    req = requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
    titlu = soup.find('h2', attrs={'class':'h4 article-title'}).text
    return titlu

def intro_stire():
    req = requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
    intro = soup.find('p', attrs={'class':'article-intro'}).text
    return intro

send_email()s
afisare_totala()