from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
def mustvisitrcm(mustvisit):
        
    url="https://traveltriangle.com/blog/places-to-visit-in-india-before-you-turn-30/"
    url1="https://traveltriangle.com/blog/best-family-holiday-destinations-in-india/"
    url2="https://traveltriangle.com/blog/solo-female-travel-destinations-in-india/"
    
    if mustvisit==1:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
    elif mustvisit==2:
        req = Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    else:
        req = Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
    
    
    soup=BeautifulSoup(webpage,'html.parser')
    #print(soup)
    
    k=list(i.get_text() for i in soup.find_all("h3"))
    for j in k[:-3]:
        print(j)
    c=int(input("Enter choice \n"))
    o=k[c-1]
    print(o)
    #print(soup)
    b=soup.find(text=o).parent
    #q=b.find_next_sibling("p")
    q=b.find_next_siblings()
    x=0
    for i in q:
        if i.get_text().lower()=="image source":
            continue
        if (len(i.get_text())==0 and x==0):
            print(i.get_text())
            x=x+1
        elif (len(i.get_text())==0 and x>0 or i.get_text().startswith("Suggested Read") or len(i.get_text())<28):
            break
        else:
            print(i.get_text())


#1 - must visit before 30
#2 - must visit family destinations
#3 - must visit solo safe destinations