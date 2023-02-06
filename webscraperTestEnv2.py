from bs4 import BeautifulSoup                               # Jag importerar bibliotek av kod som är skapade för web scraping
import requests
import pandas as pd                                                     # Här skapar jag en variabel som jag kallar "data" och den har variabeltypen "lista"
import html.parser
from selenium import webdriver
import time
import lxml

def get_data(url):
    url = "https://www.smhi.se/q/Stockholm/2673730"                                                      # som jag ska skrapa från min valda hemsida.
    response = requests.get(url)                           # 
    soup = BeautifulSoup(response.text,                             # "response" skapas för att anropa klassen "requests" som jag importerat.
                         "lxml")                                # Variabeln "soup" skapas för att spara dataon som jag hämtar online, och jag gör
                                                               # genom att anropa klassen "BeautifulSoup" som jag importerat från biblioteket "bs4"
    time.sleep(5)
    väderprognos = soup.find_all("div",                           # 
                            class_="whiteBlock").text               # På SMHI heter elementet som jag vill skrapa "span")
    data = []
    print("testing testing !!")                                                           
    print(väderprognos)
    print("lol")
    for days in väderprognos:                                        # Klassen heter "fvTWj tDjoY eDWPu"
        print("här e ya !")
        dag = {} 
                                                            # "dag" är en dictionary-variabel, vilket är som en list-variabel fast med extra funktionalitet.        
        dag["Datum"] = days.find("span",                             # 
                            class_="dSXwP")    # 
        
        dag["Datum"] = soup.prettify()
        print(dag["Datum"])
        
        dag["Temperatur"] = days.find("div",
                            class_="_2lcnH")
        dag["Temperatur"] = soup.prettify()
        data.append(dag)

    return data


def export_data(data):
    df = pd.DataFrame(data)
    df.to_excel("Väder.xlsx")                                   # .xlsx är filtypen för Windows excel, som inte nödvändigtvis är kompatibels mes alla program
    df.to_csv("SMHI.csv")                                      # .csv är en simplare textformat som är mer cross-compatible

if __name__ == '__main__':
    data = get_data("https://www.smhi.se/q/Stockholm/2673730")
    export_data(data)
    print("Färdigskrapat")
