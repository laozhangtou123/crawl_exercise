import requests
import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
url="#####"   #ÅÀÈ¡Ä³Æ±·¿ÍøÕ¾
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
movies=soup.select('table[class="date date01"] tr')
del movies[0]
names=[]
hrefs=[]
types=[]
tols=[]
for movie in movies:
    movie_name=movie.select('td[class="one"] a')[0].get('title')
    movie_href=movie.select('td[class="one"] a')[0].get('href')
    movie_type=movie.select('td')[1].get_text()
    movie_tol=int(movie.select('td')[2].get_text())
    names.append(movie_name)
    hrefs.append(movie_href)
    types.append(movie_type)
    tols.append(movie_tol)

df=pd.DataFrame({

    'name':names,
    'href':hrefs,
    'type':types,
    'tol':tols
})
# print(df)
df.to_csv('movies.csv')