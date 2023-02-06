import requests
import pandas as pd
from datetime import datetime
from datetime import timedelta

url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.2/lat/59.4/data.json'
response = requests.get(url)

if response.status_code == 200:
    print("Status code:", response.status_code, "successful connection")
data = response.json()
exportData = []

i = 0
prognos ={}
idag = datetime.now()
övermorgon = idag + timedelta(2)
dagenEfter = idag + timedelta(3)
sistaDagen = idag + timedelta(4)
while i < 53:
    prognos["Today"] = data["timeSeries"][i]["parameters"][10]["values"]
    i+=16  
    prognos["Tomorrow"] = data["timeSeries"][i]["parameters"][10]["values"]
    i+=12
    prognos[övermorgon.strftime("%A")] = data["timeSeries"][i]["parameters"][10]["values"]
    i+=12
    prognos[dagenEfter.strftime("%A")] = data["timeSeries"][i]["parameters"][10]["values"]
    i+=12
    prognos[sistaDagen.strftime("%A")] = data["timeSeries"][i]["parameters"][10]["values"]
    exportData.append(prognos["Today"])
    exportData.append(prognos["Tomorrow"])
    exportData.append(prognos[övermorgon.strftime("%A")])
    exportData.append(prognos[dagenEfter.strftime("%A")])
    exportData.append(prognos[sistaDagen.strftime("%A")])
    i+=1

print(exportData)


df = pd.DataFrame(exportData)
df.columns = ["Prognosis"]
df.index = ["Today", "Tomorrow", övermorgon.strftime("%A"), dagenEfter.strftime("%A"), sistaDagen.strftime("%A")] 
df.to_excel("Prognos.xlsx")
df.to_csv("Prognos.csv")