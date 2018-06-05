from bs4 import BeautifulSoup
import requests
url="https://www.quora.com/topic/Productivity"
source_code=requests.get(url)
plain_text=source_code.text
soup=BeautifulSoup(plain_text,"html.parser")
for link in soup.find_all("img"):
    print(link.get('src'))
    #print("https://www.quora.com"+str(link.get('href')))
