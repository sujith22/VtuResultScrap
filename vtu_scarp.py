import requests
from bs4 import BeautifulSoup
url1 = "http://results.vtu.ac.in/vitaviresultcbcs/resultpage.php"
usn=raw_input("Enter USN");
r = requests.post(url1,data={'lns':usn });
r.close();
f=open("atria.csv","a");
f.write("USN,ME-internals,ME-externals,ME-total,CN-internals,CN-externals,CN-Total,Adv.JAVA-internals,Adv.JAVA-externals,Adv.JAVA-total,DBMS-internals,DBMS-externals,DBMS-total,FLAT-internals,FLAT-externals,FLAT-total,CC-internals,CC-externals,CC-total,CN Lab-internals,CN Lab-externals,CN Lab-total,DBMS Lab-internals,DBMS Lab-externals,DBMS Lab-total\n")
page_html=r.text
page_soup = BeautifulSoup(page_html,"html.parser")
names=page_soup.findAll("div",{"class","divTableCell"})
count=0;
data=usn+","
i=8;
while(i<len(names)):
    count+=1;
    data+=names[i].text+","+ names[i+1].text+","+names[i+2].text+","
    
    if(count==8):
        data+="\n"
        count=0;
    i+=6
    if(i>=53):
        f.write(data)
        break;

f.close();