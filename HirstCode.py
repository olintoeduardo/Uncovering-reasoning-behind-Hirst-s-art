from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd

score =0
final_score = 0
work_number = int(input('Input the artwork number: '))
link = 'https://currency.nft.heni.com/item/9236'
options = Options()
options.add_argument('---headless')
navegador = webdriver.Chrome(options=options)
navegador.get(link)
sleep(5)
soup = BeautifulSoup(navegador.page_source, 'html.parser')

rankings = soup.find_all('span', class_='')

array_r = []

for el in rankings:
    r = el.text.replace(',','')
    array_r.append(r)

i = 3
while i >0:
    array_r.pop()
    i-=1

for i in range(len(array_r)):
    array_r[i]=int(array_r[i])   
 
    if array_r[i]<=4500 or array_r[i]>=5500:
        score+=2
        if array_r[i] <= 4000 or array_r[i] >= 6000:
            score+=1
            if array_r[i]<=3500 or array_r[i]>= 6500:
                score +=1
                if array_r[i] <= 3000 or array_r[i] >= 7000:
                    score+=1
                    if array_r[i]<=2500 or array_r[i]>=7500:
                        score+=1
                        if array_r[i] <=2000 or array_r[i] >= 8000:
                            score+=1
                            if array_r[i]<=1500 or array_r[i]>=8500:
                                score+=1
                                if array_r[i] <=1000 or array_r[i]>=9000:
                                    score+=1
                                    if array_r[i] <=500 or array_r[i]>=9500:
                                        score+=1
    else:
        score+=1   

final_score = score*(100/120)
print('Score out of 100: ',final_score)
