import re
import requests

urles = 'www.mosigra.ru'



Regular1 = re.compile(urles+'[/\w_\-.]+')
Regular2 = re.compile('\w[\w_\-.]+\w@[\w.]+.[\w]+')

SiteSpis = [urles]
SearchSite = []
Perehod = 0
perehodSchet = 10

for urles2 in SiteSpis :

    if Perehod > perehodSchet : breaPerehod
    Request = requests.get('http://' + urles2)
    Xtext = Request.text
   
    Sites = Regular1.findall(Xtext)
    Sites = list(set(Sites))
   
    for i in Sites :
        if i not in SiteSpis :
            SiteSpis.append(i)
    
    Mail = Regular2.findall(Xtext)
    Mail = list(set(Mail))
    
    for i in Mail :
        if i not in SearchSite :
            SearchSite.append(i)
    
    Perehod = Perehod + 1

SearchSite = list(set(SearchSite))
for i in SearchSite : print(i)
