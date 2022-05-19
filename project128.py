from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(START_URL)
soup=BeautifulSoup(page.text,"html.parser")
star_table=soup.find("table")
tlist=[]
table_rows=star_table.find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip()for i in td]
    tlist.append(row)
star_name=[]
Distance=[]
Mass=[]
Radius=[]
for i in range(1,len(tlist)):
    star_name.append(tlist[i][0])
    Distance.append(tlist[i][5])
    Mass.append(tlist[i][7])
    Radius.append(tlist[i][8])
df2=pd.DataFrame(list(zip(star_name,Distance,Mass,Radius)),columns=["star_name","Distance","Mass","Radius"])
df2.to_csv("dwarfstars.csv")