from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


data = []
url = "https://www.smhi.se/q/Stockholm/2673730"
skrapare = webdriver.Chrome()
skrapare.get(url)
tempArray = {}
time.sleep(10)
temperaturKnapp = skrapare.find_elements(By.CLASS_NAME, 
    '_2lcnH')
time.sleep(10)
for dag in temperaturKnapp:
    dag = dag.text
    tempArray["Temperatur"] = dag.find("div")
    print(tempArray["Temperatur"])
    data.append(dag)

datum = skrapare.find_elements(By.CLASS_NAME, 'gbLXx')
skrapare.implicitly_wait(15)
dagArray = {}
for dagar in datum:
    dagar = dagar.text
    dagArray["Datum"] = dagar.find("span")
    print(dagArray["Datum"])
    data.append(dagar)

df = pd.DataFrame(data)
df.to_csv("Dagens väder.csv")
df.to_excel("Dagens väder.xlsx")
print("Färdigskrapat")

#skrapare.find_element(By.XPATH, "")
#
#
#


