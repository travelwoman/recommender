from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import json
def seasonbasedrcm(season):
        
    url="https://traveltriangle.com/blog/best-places-to-visit-in-india-in-"+season+"/"
    url1="https://traveltriangle.com/blog/places-to-visit-in-"+season+"-in-india/"
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    except:
        req = Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    soup=BeautifulSoup(webpage,'html.parser')
    print(soup.get_text())
    
    k=list(i.get_text() for i in soup.find_all("h3"))
    for j in k[:-2]:
        print(j)
    c=int(input("Enter choice \n"))
    if c==4:
        c=5
    o=k[c-1]
    print(o)
    #print(soup)
    b=soup.find(text=o).parent
    #q=b.find_next_sibling("p")
    q=b.find_next_siblings()
    x=0
    y=[]
    for i in q:
        if i.get_text().lower()=="image source":
            continue
        if (len(i.get_text())==0 and x==0):
            y.append(i.get_text())
            x=x+1
        elif (len(i.get_text())==0 and x>0 or i.get_text().startswith("Suggested Read") or len(i.get_text())<100):
            break
        else:
            y.append(i.get_text())
    return json.dumps(y)

