import requests 
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd


#url_list=[]
#reyurl=


URL= "https://starwars.fandom.com/wiki/Rey_Skywalker"
page = requests.get(URL)

soup= BeautifulSoup(page.content, "html.parser")

info = soup.find(id="mw-content-text")

#char_deets = info.find_all("div", class_="pi-data-value pi-font")
#print(char_deets)

deets=info.find_all("div",class_="pi-item pi-data pi-item-spacing pi-border-color")
print(deets)


print("\n")

moredeets=info.find_all("div",class_="pi-item pi-data pi-item-spacing pi-border-color")
print(moredeets)
print("\n")

values=[]
labels=[]
empty=[1,2,3,4,5,5,32,326,]
for moredeets in moredeets:
    ddd=moredeets.find("div", class_="pi-data-value pi-font")
    print(ddd.text)
    values.append(ddd.text)
    label=moredeets.find("h3", class_="pi-data-label pi-secondary-font")
    labels.append(label.text)
    print(label.text)
    #pip for ddd in ddd:
        

plt.bar(labels,values)

#plt.plot(labels,values)
#plt.show()
#data={'a':values,'name2':empty[3]}
#df = pd.DataFrame(values,labels)
#df.plot()
#series= pd.Series(values,index=labels)
#series.plot()





















#df=pd.DataFrame
#print(values)
#sprint(labels)

#df=pd.DataFrame()
#df['name']=value[0]
#df['year born']=value[1]
