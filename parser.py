from bs4 import BeautifulSoup
import requests

url = "https://uaserials.pro/films/"
r = requests.get(url)

soup = BeautifulSoup(r.text, features="html.parser")

soup_list_href = soup.find_all('a',{"class":"short-img img-fit"})
f = open('link.txt',"w", encoding='utf-8')
for href in soup_list_href:
    print(href.text)
    f.write(f"{href.text}\n")

f.close()