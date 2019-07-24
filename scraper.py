
import csv  
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
Url = 'https://karki23.github.io/Weather-Data/Albury.html'
pageHtml = uReq(Url)
soup = soup(pageHtml,"html.parser") 
table = soup.find_all("table", { "class" : "tablepress tablepress-id-10 tablepress-responsive-phone" })
with open('Albury.csv', 'w',newline='') as csvfile:
    f = csv.writer(csvfile)
    f.writerow(['Date', 'Location', 'MinTemp','MaxTemp','Rainfall','Evaporation','Sunshine','WindGustDir','WindGustSpeed','WindDir9am','WindDir3pm','WindSpeed9am','WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am','Pressure3pm','Cloud9am','CLoud3pm','Temp9am','Temp3pm','RainToday','RISK_MM','RainTomorrow'])
    for x in table:
        table_body = x.find('tbody') 
        rows = table_body.find_all('tr') 
        for tr in rows:
            data=[]
            cols = tr.find_all('td') 
            for td in cols:
                data.append(td.text.strip()) 
            f.writerow(data)
            print(data)
                    
        
    
