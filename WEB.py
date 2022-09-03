from selenium import webdriver
import requests
import time
from random import randint

URL = "https://svnweb.freebsd.org/csrg/share/dict/propernames?revision=61767&view=co&pathrev=69978"
datos = requests.get(URL)
texto = datos.text
palabras = texto.splitlines()
name_aleatorio = palabras[randint(0, len(palabras))] + str(randint(100, 900))

Username = name_aleatorio
Password = "1234567890"
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://opentunnel.net/ssh-server-83/")
time.sleep(4)
#Username Xpath
User = driver.find_element("xpath",'//*[@id="username"]')
User.send_keys(Username)
#Password Xpath
Pass = driver.find_element("xpath",'//*[@id="password"]')
Pass.send_keys(Password)
#Click Login Button Xpath
driver.find_element("xpath",'/html/body/main/div[5]/div[2]/div[2]/button').click()
time.sleep(4)
#Informacion de la cuenta Xpath
XUsername = driver.find_element("xpath",'//*[@id="report"]/div[2]/ul/li[1]/b')
XUsername = XUsername.text
XPassword = driver.find_element("xpath",'//*[@id="report"]/div[2]/ul/li[2]/b')
XPassword = XPassword.text
XHost_NameIP = driver.find_element("xpath",'//*[@id="report"]/div[2]/ul/li[3]/text()[1]')
XHost_NameIP = XHost_NameIP.text
XHost_Name = driver.find_element("xpath",'//*[@id="report"]/div[2]/ul/li[5]')
XHost_Name = XHost_Name.text
XDropbear = driver.find_element("xpath",'//*[@id="report"]/div[2]/ul/li[7]')
XDropbear = XDropbear.text
XExpiration_Date = driver.find_element("xpath",'//*[@id="report"]/div[2]/ul/li[10]/b')
XExpiration_Date = XExpiration_Date.text
XPubli_Key = driver.find_element("xpath",'//input[@id="public-key"]')
XPubli_Key = XPubli_Key.text
print(Inf)
time.sleep(1)

with open("Cuenta.txt", "w") as f:
    f.write(XUsername + "\n")
    f.write(XPassword + "\n")
    f.write(XHost_NameIP + "\n")
    f.write(XHost_Name + "\n")
    f.write(XDropbear + "\n")
    f.write(XExpiration_Date + "\n")
    f.write(XPubli_Key + "\n")
    f.close()
