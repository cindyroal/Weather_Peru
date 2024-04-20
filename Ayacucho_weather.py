#!/usr/bin/env python
# coding: utf-8

# In[117]:


#Author: Cindy Rojas
# Purpose: This code scrapes data from the website https://sinia.minam.gob.pe/senamhi


# In[ ]:


import requests
import re
import pandas as pd
import requests, json
from bs4 import BeautifulSoup
from io import StringIO


# In[111]:


r= requests.get("https://sinia.minam.gob.pe/wssenamhi/response.php?method=rec&idEstacion=4729D600&param=PT||101&mes=11&anio=2016")
c= r.content
print(c)
print(type(c))


# In[112]:


get_ipython().run_line_magic('pwd', '')


# In[113]:


s=str(c,'utf-8')
s=s[1:]
s=s[:-1]
print(s)


# In[114]:


lista = s.split(",{")
df_tot = pd.DataFrame()
for x in lista:
    if x[0] != '{':
        x2 = "{" + x
    else:
        x2 = x
    x2 = json.loads(x2)
    x2 = pd.DataFrame(x2, index=[0])
    df_tot = df_tot.append(x2)
df_tot


# In[115]:



Meses=[1,2,3,4,5,6,7,8,9,10,11]
Años=[2018]
Estaciones=['4729D600','00112069','00113021','00112068','00113100','00113022']
Parametros=['PT||101','TM||103']


# In[116]:


for estac in Estaciones:
    if estac=='4729D600':
        Estacion="Cangallo"
            
        for param in Parametros:
            if param=='PT||101':
                Param="Precipitacion"
            if param=='TM||103':
                Param="Temp_Min"
          

            for año in Años:
                for mes in Meses:
                    ab="https://sinia.minam.gob.pe/wssenamhi/response.php?method=rec"
                    url_1=ab+'&idEstacion='+str(estac)+'&param='+str(param)+'&mes='+str(mes)+'&anio='+str(año)
                    print(url_1)
                    r = requests.get(url_1, timeout=20)
                    c= r.content
                    print(c)
                    print(type(c))
                    
                    s=str(c,'utf-8')
                    s=s[1:]
                    s=s[:-1]
                    print(s)
                    
                    try:
                        lista = s.split(",{")
                        df_tot = pd.DataFrame()
                        for x in lista:
                            if x[0] != '{':
                                x2 = "{" + x
                            else:
                                x2 = x
                            x2 = json.loads(x2)
                            x2 = pd.DataFrame(x2, index=[0])
                            df_tot = df_tot.append(x2)
                        df_tot
                        df_tot.to_excel(excel_writer='Excel_' + str(Estacion) + '_' + str(mes) + '_' + str(año) + '_param' + str(Param) +'.xlsx', index=False)  

                    except:
                        continue  
                        
    if estac=='00112069':
        Estacion="Huamanga-Wayllapampa"
            
        for param in Parametros:
            if param=='PT||101': 
                Param="Precipitacion"
            if param=='TM||103':
                Param="Temp_Min"

            for año in Años:
                for mes in Meses:
                    ab="https://sinia.minam.gob.pe/wssenamhi/response.php?method=rec"
                    url_1=ab+'&idEstacion=' + str(estac) + '&param=' + str(param)+ '&mes=' +str(mes)+ '&anio=' +str(año)
                    print(url_1)
                    r = requests.get(url_1, timeout=20)
                    c= r.content
                    print(c)
                    print(type(c))
                    
                    s=str(c,'utf-8')
                    s=s[1:]
                    s=s[:-1]
                    print(s)
                    
                    try:
                        lista = s.split(",{")
                        df_tot = pd.DataFrame()
                        for x in lista:
                            if x[0] != '{':
                                x2 = "{" + x
                            else:
                                x2 = x
                            x2 = json.loads(x2)
                            x2 = pd.DataFrame(x2, index=[0])
                            df_tot = df_tot.append(x2)
                        df_tot
                        df_tot.to_excel(excel_writer='Excel_' + str(Estacion) + '_' + str(mes) + '_' + str(año) + '_param' + str(Param) +'.xlsx', index=False)  

                    except:
                        continue  
                        
    if estac=='00113021':
        Estacion="Huamanga-La Quinua"
            
        for param in Parametros:
            if param=='PT||101': 
                Param="Precipitacion"
            if param=='TM||103':
                Param="Temp_Min"

            for año in Años:
                for mes in Meses:
                    ab="https://sinia.minam.gob.pe/wssenamhi/response.php?method=rec"
                    url_1=ab+'&idEstacion='+str(estac)+'&param='+str(param)+'&mes='+str(mes)+'&anio='+str(año)
                    print(url_1)
                    r = requests.get(url_1, timeout=20)
                    c= r.content
                    print(c)
                    print(type(c))
                    
                    s=str(c,'utf-8')
                    s=s[1:]
                    s=s[:-1]
                    print(s)
                    
                    try:
                        lista = s.split(",{")
                        df_tot = pd.DataFrame()
                        for x in lista:
                            if x[0] != '{':
                                x2 = "{" + x
                            else:
                                x2 = x
                            x2 = json.loads(x2)
                            x2 = pd.DataFrame(x2, index=[0])
                            df_tot = df_tot.append(x2)
                        df_tot
                        df_tot.to_excel(excel_writer='Excel_' + str(Estacion) + '_' + str(mes) + '_' + str(año) + '_param' + str(Param) +'.xlsx', index=False)  

                    except:
                        continue  

    if estac=='00112068':
        Estacion="Huanta"
            
        for param in Parametros:
            if param=='PT||101': 
                Param="Precipitacion"
            if param=='TM||103':
                Param="Temp_Min"

            for año in Años:
                for mes in Meses:
                    ab="https://sinia.minam.gob.pe/wssenamhi/response.php?method=rec"
                    url_1=ab+'&idEstacion='+str(estac)+'&param='+str(param)+'&mes='+str(mes)+'&anio='+str(año)
                    print(url_1)
                    r = requests.get(url_1, timeout=20)
                    c= r.content
                    print(c)
                    print(type(c))
                    
                    s=str(c,'utf-8')
                    s=s[1:]
                    s=s[:-1]
                    print(s)
                    
                    try:
                        lista = s.split(",{")
                        df_tot = pd.DataFrame()
                        for x in lista:
                            if x[0] != '{':
                                x2 = "{" + x
                            else:
                                x2 = x
                            x2 = json.loads(x2)
                            x2 = pd.DataFrame(x2, index=[0])
                            df_tot = df_tot.append(x2)
                        df_tot
                        df_tot.to_excel(excel_writer='Excel_' + str(Estacion) + '_' + str(mes) + '_' + str(año) + '_param' + str(Param) +'.xlsx', index=False)  

                    except:
                        continue  
                        
    if estac=='00113100':
        Estacion="Vilcashuaman"
            
        for param in Parametros:
            if param=='PT||101': 
                Param="Precipitacion"
            if param=='TM||103':
                Param="Temp_Min"

            for año in Años:
                for mes in Meses:
                    ab="https://sinia.minam.gob.pe/wssenamhi/response.php?method=rec"
                    url_1=ab+'&idEstacion='+str(estac)+'&param='+str(param)+'&mes='+str(mes)+'&anio='+str(año)
                    print(url_1)
                    r = requests.get(url_1, timeout=20)
                    c= r.content
                    print(c)
                    print(type(c))
                    
                    s=str(c,'utf-8')
                    s=s[1:]
                    s=s[:-1]
                    print(s)
                    
                    try:
                        lista = s.split(",{")
                        df_tot = pd.DataFrame()
                        for x in lista:
                            if x[0] != '{':
                                x2 = "{" + x
                            else:
                                x2 = x
                            x2 = json.loads(x2)
                            x2 = pd.DataFrame(x2, index=[0])
                            df_tot = df_tot.append(x2)
                            df_tot
                            
                            df_tot.to_excel(excel_writer='Excel_' + str(Estacion) + '_' + str(mes) + '_' + str(año) + '_param' + str(Param) +'.xlsx', index=False)  

                    except:
                        continue  
                        
                        
    if estac=='00113022':
        Estacion="VF-Huancapi"
            
        for param in Parametros:
            if param=='PT||101': 
                Param="Precipitacion"
            if param=='TM||103':
                Param="Temp_Min"

            for año in Años:
                for mes in Meses:
                    ab="https://sinia.minam.gob.pe/wssenamhi/response.php?method=rec"
                    url_1=ab+'&idEstacion='+str(estac)+'&param='+str(param)+'&mes='+str(mes)+'&anio='+str(año)
                    print(url_1)
                    r = requests.get(url_1, timeout=20)
                    c= r.content
                    print(c)
                    print(type(c))
                    
                    s=str(c,'utf-8')
                    s=s[1:]
                    s=s[:-1]
                    print(s)
                    
                    try:
                        lista = s.split(",{")
                        df_tot = pd.DataFrame()
                        for x in lista:
                            if x[0] != '{':
                                x2 = "{" + x
                            else:
                                x2 = x
                            x2 = json.loads(x2)
                            x2 = pd.DataFrame(x2, index=[0])
                            df_tot = df_tot.append(x2)
                        df_tot
                        
                        
                        df_tot.to_excel(excel_writer='Excel_' + str(Estacion) + '_' + str(mes) + '_' + str(año) + '_param' + str(Param)  +'.xlsx', index=False)  

                    except:
                        continue  


# In[ ]:





# In[ ]:




