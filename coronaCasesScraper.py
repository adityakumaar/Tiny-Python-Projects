import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
req = requests.get(url)
src = BeautifulSoup(req.text, "html.parser")
data = src.find_all("div", class_ = "maincounter-number")

print("Total Cases:     ", data[0].text.strip())
print("Total eaths:     ", data[1].text.strip())
print("Total Recovered: ", data[2].text.strip())
