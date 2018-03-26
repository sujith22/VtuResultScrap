import requests
from bs4 import BeautifulSoup
url1 = "http://results.vtu.ac.in/vitaviresultcbcs/resultpage.php"
# usn=raw_input("Enter USN");
ia=60; #start usn
lis=[63,64,70,74,75,97,102] #usn to be omitted
for ia in range(116,117,1): #give the range of usn which need to extracted
    if(ia in lis):
        continue;  #skipping usn
    usn="1AT15IS"+str(ia)
    r = requests.post(url1,data={'lns':usn });
    r.close();
    f=open("atria.csv","a");
    #uncomment the following line when u run for first USN
# f.write("USN,ME-internals,ME-externals,ME-total,CN-internals,CN-externals,CN-Total,Adv.JAVA-internals,Adv.JAVA-externals,Adv.JAVA-total,DBMS-internals,DBMS-externals,DBMS-total,FLAT-internals,FLAT-externals,FLAT-total,CC-internals,CC-externals,CC-total,CN Lab-internals,CN Lab-externals,CN Lab-total,DBMS Lab-internals,DBMS Lab-externals,DBMS Lab-total\n")
    page_html=r.text
    page_soup = BeautifulSoup(page_html,"html.parser")
    names=page_soup.findAll("div",{"class","divTableCell"})
    count=0;    
    data=usn+","
    i=8; #skipping first 8 divs
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