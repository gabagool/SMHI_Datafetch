import requests
import pandas as pd
from datetime import datetime
from datetime import timedelta
import locale


url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18/lat/59.4/data.json'
response = requests.get(url)

if response.status_code == 200:
    print("Status code:", response.status_code, "successful connection")
data = response.json()
exportData = []


prognos ={}
locale.setlocale(locale.LC_TIME, "sv_SE")
idag = datetime.now()
imorgon = idag + timedelta(1)
övermorgon = idag + timedelta(2)
efterÖvermorgon = idag + timedelta(3)
sistaDagen = idag + timedelta(4)
i=0
while i < 66:
    prognos["Idag"] = data["timeSeries"][i]["parameters"][10]["values"]
    i+=24   
    print(prognos["Idag"])  
    prognos["Imorgon"] = data["timeSeries"][i]["parameters"][10]["values"]
    i+=24
    print(prognos["Imorgon"])
    prognos["I övermorgon"] = data["timeSeries"][i]["parameters"][10]["values"]
    i+=9
    print(prognos["I övermorgon"])
    prognos["dagenEfter"] = data["timeSeries"][i]["parameters"][10]["values"]
    i+=4
    print(prognos["dagenEfter"])
    prognos["sistaDagen"] = data["timeSeries"][i]["parameters"][10]["values"]
    i+=4
    print(prognos["sistaDagen"])
    exportData.append(prognos["Idag"])
    exportData.append(prognos["Imorgon"])
    exportData.append(prognos["I övermorgon"])
    exportData.append(prognos["dagenEfter"])
    exportData.append(prognos["sistaDagen"])
    i+=1

print(exportData)


df = pd.DataFrame(exportData)
df.columns = ["Grader C°"]
df.index = [idag.strftime("%A"), imorgon.strftime("%A"), övermorgon.strftime("%A"),
 efterÖvermorgon.strftime("%A"), sistaDagen.strftime("%A")]
df.to_excel("Prognos.xlsx")
df.to_csv("Prognos.csv")
print("Anropat")
