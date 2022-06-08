from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
def monthbasedrcm(month):
    if month=="april":
        pass
    else:
        url="https://traveltriangle.com/blog/places-to-visit-in-"+month+"-in-india/"
        url1="https://traveltriangle.com/blog/places-to-visit-in-india-in-"+month+"/"
        url2="https://traveltriangle.com/blog/best-places-to-visit-in-"+month+"-in-india/"
        #print(url,url1,url2)
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            '''with urllib.request.urlopen(url) as webpagedata:
                data=webpagedata.read()'''
        except:
            try:
                req = Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
                webpage = urlopen(req).read()
            except:
                req = Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
                webpage = urlopen(req).read()
        soup=BeautifulSoup(webpage,'html.parser')
       # print(soup)
        k=list(i.get_text() for i in soup.find_all("h3"))
        o=k[7]
        for j in k[:-2]:
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
            elif (len(i.get_text())==0 and x>0 or i.get_text().startswith("Suggested Read") or i.get_text()[0:2].isdigit()):
                break
            else:
                print(i.get_text())
        '''for j in w:
            print(j.get_text())
        if len(w)>1:
            print(w.get_text())
        else:
            w=soup.find(text=o).findNext("p").findNext("p")
            print(w.get_text())
        print(q.get_text())'''

