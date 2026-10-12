import requests, csv
from bs4 import BeautifulSoup

url = "https://example.com"
soup = BeautifulSoup(requests.get(url,timeout=10).text,"html.parser")
titles = [h.get_text(strip=True) for h in soup.find_all(["h1","h2","h3"])]

with open("data.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["Title"])
    w.writerows([[t] for t in titles])