
# coding: utf-8

# In[1]:

#Importing packages needed
import numpy as np
import json
import pandas as pd
import scipy.stats as sm 
import pylab as pl
import collections
import string
import matplotlib.pyplot as pl
import datetime
#c=json.load(open('pui.json'))
#pl.rcParams.update(c)
from IPython.display import HTML
from datetime import datetime, timedelta
get_ipython().magic(u'pylab inline')
import math
import sqlite3


# In[2]:

start_minute_interval = 15
current_time = datetime.datetime.now()
start_time = datetime.datetime.now() + timedelta(minutes=start_minute_interval)
print 'This is the current time',current_time
print 'This is the time when the whitelist script should start working',start_time


# In[3]:

per = 0.05


# In[4]:

while(Tr):
    if datetime.datetime.now() == start_time:
        break


# In[4]:

import os
os.system("hi.py 1")


# In[5]:

pir1=pd.read_csv('pir1.csv')
mac1 = pd.read_csv('mac1.csv')
print len(mac1)


# In[6]:

mac1['date']=pd.to_datetime(mac1['dtg'])
mac1['hour']=mac1['date'].dt.hour
mac1['minute']=mac1['date'].dt.minute


# In[7]:

r_mac1=[]


for i in range(len(mac1)):
    #print 'ji'
    if str(mac1['date'][i])[0:10]=='2015-09-17': 
        r_mac1.append(i)
        
print min(r_mac1)   


# In[8]:

day = mac1[min(r_mac1):max(r_mac1)]
day = day[day['hour']>5]
b = 15


# In[9]:

iterations_in_day = 0
if day['hour']>6:
    if iterations_in_day!=0:
        upgraded_time = datetime.datetime.now() + timedelta(minutes=start_minute_interval)
    if datetime.datetime.now()==upgraded_time:
        row_mac1 = []
#remove_mac = []
        for k in range(6,7):

            row_mac1.append(k_mac1.count(i))
            mac1_hour = mac1[min(r_mac1):max(r_mac1)][mac1['hour'][min(r_mac1):max(r_mac1)] == k]
            #pir1_hour = pir1[min(r_pir1):max(r_pir1)][pir1['hour'][min(r_pir1):max(r_pir1)] == k]
            #print mac1_hour['minute'].head()
            for i in range(4):
                mac1_15minute = []
                #pir1_5minute = []
                mac1_15minute = mac1_hour[(mac1['minute'] >= i*15) & (mac1['minute'] <= (i+1)*15)]
                #pir1_5minute = pir1_hour[(pir1['minute'] >= i*5) & (mac1['minute'] <= (i+1)*5)]
                counter = collections.Counter(mac1_5minute['mac'])
                #print mac1_5minute 
                #counter1 = collections.Counter(pir1_5minute['count'])
                print 'hour',k ,'this is ',i*5 , 'and mac count in this 5min is',len(counter)
                print ''
                print counter

                counter_list = list(counter)
                print counter_list
                print ''


# In[15]:

row_mac1 = []
l = []
wl_list = []
wl_count = []
occ=1
#iterations=0
wl = {}
wl_f = {}
for p in range(6,24):
    c=0
    d=1
    sub_wl = []
    #row_mac1.append(k_mac1.count(i))
    mac1_hour = mac1[min(r_mac1):max(r_mac1)][mac1['hour'][min(r_mac1):max(r_mac1)] == p]
    #pir1_hour = pir1[min(r_pir1):max(r_pir1)][pir1['hour'][min(r_pir1):max(r_pir1)] == k]
    #print mac1_hour['minute'].head()
    for i in range(6):
        #print c,d
        mac1_15minute = []
        
        #pir1_5minute = []
        mac1_15minute = mac1_hour[(mac1['minute'] >= i*10) & (mac1['minute'] <= (i+1)*10)]
        #pir1_5minute = pir1_hour[(pir1['minute'] >= i*5) & (mac1['minute'] <= (i+1)*5)]
        counter = collections.Counter(mac1_15minute['mac'])
        #print mac1_5minute 
        #counter1 = collections.Counter(pir1_5minute['count'])
        dict_counter = dict(counter)
        if c!=0:
            dup_list = wl_list
            #print dup_list
            
        
        print 'hour',p,'this is ',i*10 , 'and mac count in this 10min is',len(counter)
        print ''
        print counter
        mac_collected = len(counter)
        print mac_collected
        l.append(mac_collected)
        wl_len = 0.3*mac_collected
        wl_len = int(math.ceil(wl_len))
        sub = wl_len
        print wl_len
        
        for w in sorted(dict_counter, key=dict_counter.get, reverse=True):
            #print w, dict_counter[w]
            #wl[w] = dict_counter[w]
             if sub!=0:
                    
                    #wl[w] = dict_counter[w]
                    wl_list.append(w)
                    sub_wl.append(w)
                    wl_count.append(dict_counter[w])
                    
                    sub = sub - 1
                
        
        
        if c==0:
            dup_list = wl_list
            
            
            
        if c == 0:
            for k in wl_list:         
                    #print k,v,'zero'
                wl[k]=occ
                    
        if c>0:
            for k in wl_list:
                #print k 
                
                if k in dup_list:
                    #print wl[k]
                    wl[k]=dup_list.count(k)
                    
                else:
                    wl[k]=occ
                    
                    
        
            
        
        
                    
                
     
        
        if c!=5:
            c,d = c+1,d+1

        
        #counter_list = list(counter)
    
        #print 'here'
    #print counter_list
    #print 'here'
    
    
    


# In[16]:

wl['a8:a6:68:d5:2a:5e']


# In[ ]:



