from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from datetime import datetime
from datetime import timedelta
import locale
locale.setlocale(locale.LC_TIME, "sv_SE")
data = []
url = "https://www.smhi.se/q/Stockholm/2673730"
skrapare = webdriver.Chrome()
skrapare.get(url)
tempArray = {}
idag = datetime.now()
imorgon = idag + timedelta(1)
övermorgon = idag + timedelta(2)

temperaturKnapp = skrapare.find_elements(By.CLASS_NAME, 
    '_2lcnH')

for dag in temperaturKnapp:
    dag = dag.text
    print(dag)
    data.append(dag)

data.pop()
data.pop()
data.pop(4)
data.pop(4)
data.pop(1)
data.pop(1)
print(data)
df = pd.DataFrame(data)
df.columns = ["max/min"]
df.index = [idag.strftime("%A"), imorgon.strftime("%A"), övermorgon.strftime("%A")]
df.to_excel("Stockholm temperatur.xlsx")
df.to_csv("Stockholm temperatur.csv")
print("Färdigskrapat!")
#
#
#


