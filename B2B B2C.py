#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os


# In[ ]:





# In[ ]:


data = pd.read_csv('company_salesdata.csv')


# In[ ]:





# In[ ]:


words = data.values.tolist()


# In[ ]:


#find common words used in business names to separate B2B and B2C customers

firstlist = ["The","Home","Depot","Amazon","USA","Inc","LLC","Walmart.com","Companies","Custom","Woodworking","Cabinets","Construction","amish","Furniture","Lowes","Wayfair","Products","eBay","Woodworks","Cabinetry","Company","Cabinet","Design","Inc.","Acquisition","Restorers","Builders","J&P","Carpentry","Shop","Co","Homes","Country","Lowe's","Industries","Manufacturing","Supply","Acquisitions","Limited","Industrial","store","plumbing","menards","menard's","woodcraft","stores","wal-mart","group","designs","hardware","enterprises","building","ltd","services","kitchen","millwork","of","contracting","kitchens","brothers","security","door","doors","advanced","molding","moldings","energy","engineering","international","exports","business","college","church","landscape","production","services","systems,","systems","electric","electrical","solutions","woodwork","remodeling","claims","works","woodshop","school","library","properties","furnishings","woodcrafters","creations","lumber","millworks","fedex","doors","hayneedle","sales","interiors","HOMECRESTCABINETRY/MASTERBRAND","corporation","heritage","associates","solutions","new","freight","crafts","sons","for","by","craft","view","closets","specialties","mountain","co.","mfg","resurfacing","painting","college","service","development","state","health","woodcrafts","renovations","cellars","refinishing","american","rustic","contractors","unlimited","restoration","valley","interior","rustics","package","closet","studio","lakeshore","in","granite","systems","specialty","handyman","district","distribution","university","church","joe's","residential","cabinetcraft","midwest","workshop","creative","cutting","restorations","decorating","finishing","woodcrafting","city","dba","antiques","downtown","us","ups","llp","creation","property","concepts","precision","works","shapes","expansion","son","sawdust","heavenly","cabinetmaker","great","log","llc.","creek","quality","productions","countertops","architecture","management","ARCHITECTURAL","marketing","community","pivotal","enterprise","improvements","maintenance","medical","studios","county","craftsmen","northern","spectrum","investments","hospitals","metal","integrity","yacht","laminators","cw","built","made","floors","factory","flooring","time","southern","kansas","garden","contractor","making","general","DESIGN'S","working","contr","hardwoods","fabrication","const.","remodel","center","corp.","warehouse","dci","imports","cd","sawmill","joinery","builder","realty","milling"]
secondlist = ["lending","amusement","tech","authority","mechani","carpet","corp","landmark"," solar","solar ","colony","lawnworks","tools","innova","componen","colonial","signatu","kabinet","bcr","woodworx","poseidon","bourbon","rustbelt","reclamat","hospital","clinic","material","plast","homework","global","landmark","retail","environ","showroom","ideal","surface","colonia","homestead","heirlo","contructi","operation","ology"," tech","legacy","ADIRONDACK","'s","polyte","transportation","carpenter","society","wdwrkg", "master", "constructio","studio","booty","optex","horst & horst","electronics","mindpath","costume","photo","assurance","architect","aluminum","central","techno","entertain","Depot","Amazon","LLC","incorp","Walmart","Custom","Woodwork","Cabinet","Construct","Furniture","Lowes","Wayfair","Product","eBay","Woodwork","Company","Compani","Cabinet","Design","Acquisition","Restore","Builder","J&P","Carpent","Country","Lowe's","Industri","industry","manufactur","Supply","Limited","Industri","plumbing","menards","menard's","woodcraft","wal-mart","group","design","hardware","enterprise","building","ltd","service","kitchen","millwork","contract","brother","security","advance","molding","energy","engineering","international","export","business","college","church","landscape","production","service","system","electric","solutions","remodel","woodshop","school","library","propert","furnish","creation","lumber","millworks","fedex","hayneedle","interior","corporation","heritage","associate","solution","freight","closets","specialties","mountain","co.","mfg","resurfacing","painting","college","service","development","health","renovations","cellars","refinishing","american","rustic","contractors","unlimited","restoration","valley","interior","rustics","package","closet","studio","lakeshore","inc.","granite","systems","specialty","handyman","district","distribution","university","church","residential","cabinetcraft","midwest","workshop","creative","cutting","restoration","decorating","finishing","woodcrafting","city","antiques","downtown","llp","creation","property","concepts","precision","shapes","expansion","sawdust","heavenly","cabinetmaker","great","llc.","creek","quality","productions","countertop","architect","management","marketing","community","pivotal","enterprise","improvements","maintenance","medical","studios","county","craftsmen","northern","spectrum","investments","hospitals","metal","integrity","yacht","laminator","built","floors","factory","flooring","southern","kansas","garden","contractor","making","general","DESIGN'S","working","hardwood","fabrication","const.","remodel","center","corp.","warehouse","import","sawmill","lending","transportation","carpenter","society","wdwrkg", "master", "constructio","studio","booty","optex","horst & horst","electronic","mindpath","costume","photo","assurance","aluminum","central","techno","entertain"]
thirdlist = ["ROBERT R TECHNIK","LEN TECHLIN","GERALD WIETECHA","JOE STECHER","SHANE STECHSCHULTE","DAN STECHSCHULTE","KATE UTTECH","MELISSA STECHER","DALILA CORPORAN","MARKUS SOLARES","MARK PLASTERS","ED PLASTER",]
for i in range(len(firstlist)):
    firstlist[i] = firstlist[i].upper()
for i in range(len(secondlist)):
    secondlist[i] = secondlist[i].upper()
B2B = []
B2C = []
for i in range(len(words)):
    words[i][1] = str(words[i][1]).upper()
    count = 0
    for j in range(len(firstlist)):
        if firstlist[j] in words[i][1].split():
            count+=1
    for j in range(len(secondlist)):
        if words[i][1] not in thirdlist:        
            if words[i][1].find(str(secondlist[j])) != -1:
                count += 1
    if count > 0:
        B2B.append(words[i])
    else:
        B2C.append(words[i])
B2C
    


# In[ ]:





# In[ ]:


wordlist = []
for i in range(len(B2C)):
    words[i][1] = str(B2C[i][1])
    abc = (B2C[i][1].split())
    for j in abc:
        wordlist.append(j)
wordlist


# In[ ]:


countlist = list([[x,wordlist.count(x)] for x in set(wordlist)])


# In[ ]:


countlistpd = pd.DataFrame(countlist)


# In[ ]:


countlistpd.columns = ["word","count"]
countlistpd
sortedlist = countlistpd.sort_values(by = ["count"], ascending = False, axis = 0)


# In[ ]:


sortedlist[::60]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


B2Bpd = pd.DataFrame(B2B)
B2Cpd = pd.DataFrame(B2C)


# In[ ]:


B2Bpd.to_csv("B2B.csv")
B2Cpd.to_csv("B2C.csv")


# In[ ]:


sortedlist.to_csv("SortedList.csv")


# In[ ]:




