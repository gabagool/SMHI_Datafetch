from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from datetime import datetime
from datetime import timedelta
import locale
locale.setlocale(locale.LC_TIME, "sv_SE")
data = []
url = "https://www.smhi.se/vader/prognoser/ortsprognoser/q/Stockholm/2673730"
skrapare = webdriver.Chrome()
skrapare.get(url)
tempArray = {}
idag = datetime.now()
imorgon = idag + timedelta(1)
övermorgon = idag + timedelta(2)
efterÖvermorgon = idag + timedelta(3)
sistaDagen = idag + timedelta(4)

temperaturKnapp = skrapare.find_elements(By.CLASS_NAME, 
    '_2lcnH')

for dag in temperaturKnapp:
    dag = dag.text
    data.append(dag)
data.pop()
data.pop()
data.pop()
data.pop(1)
data.pop(1)
data.pop(1)
data.pop(2)
data.pop(2)
data.pop(2)
data.pop(3)
data.pop(3)
data.pop(3)
data.pop(4)
data.pop(4)
data.pop(4)
while len(data) > 5:
    data.pop()
print(data)
df = pd.DataFrame(data)
df.columns = ["max/min"]
df.index = [idag.strftime("%A"), imorgon.strftime("%A"), övermorgon.strftime("%A"),
 efterÖvermorgon.strftime("%A"), sistaDagen.strftime("%A")]
df.to_excel("Testing 10dagar temperatur.xlsx")
df.to_csv("Testing 10dagar temperatur.csv")
print("Färdigskrapat!")
