# <p class = "product-new-price"

from bs4 import BeautifulSoup
import requests
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
from email.mime.text import MIMEText

with open("C:\\Users\\Florin\\Desktop\\MAP\\parola.txt","r") as fisier_parola:
    parola_google = fisier_parola.read().strip()

catre_cine = ['pupzf53@gmail.com']
cc_list = ['']
sender = ['pupzf53@gmail.com']
subiect = 'A scazut pretul la produsul tau!'
email = 'pupzf53@gmail.com'
email_destinatar = 'pupzf53@gmail.com'
pret_de_referinta = 10000

def send_email():
    msg = MIMEText(f"Pretul pentru {titlu_emag()} a scazut la {pret_emag()}")
    msg['Subject'] = 'A scazut pretul la produsul tau'
    msg['From'] = email
    msg['To'] = email_destinatar
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
        smtp_server.login(email,parola_google)
        smtp_server.sendmail(email,email_destinatar,msg.as_string())
    print("Email-ul a fost trimis cu succes!")

url = "https://www.emag.ro/telefon-mobil-apple-iphone-17-pro-max-1tb-5g-cosmic-orange-mfyw4zd-a/pd/D599FV3BM/?ref=fam#1-TB"

def afisare_totala():
    r = requests.get(url)
    contiunt_html = r.text
    with open("C:\\Users\\Florin\\Desktop\MAP\\emag.html","w",encoding="utf-8") as fisier:
        fisier.write(contiunt_html)
        # print(r.text)

#afisare_totala()

def pret_emag():
    pret_de_referinta = 9980
    req = requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
    pret = soup.find('p', attrs={'class':'product-new-price'}).text
    pret_nou = pret[0:5]
    pret_nou = pret_nou.replace(".","")
    pret_nou = int(pret_nou)
    return pret_nou

def verificare_trimitere_email():
    pret_nou = pret_emag()
    if (pret_nou  < pret_de_referinta):
        print("pretul a scazut")
        send_email()


def titlu_emag():
    req = requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
    title = soup.find('h1', attrs={'class':'page-title'}).text
    return title

def job():
    print("Job-ul ruleaza...")
    automatizare = BlockingScheduler()
    automatizare.add_job(pret_emag,'interval',seconds = 10)
    automatizare.start()

# afisare_totala()
verificare_trimitere_email()



