
# coding: utf-8

# for now, I have put all the mac ids between 12-6am ,and with the count of 20 in 5 mins, into the whitelist.
# I have calculated the probabilites but that didnt seem to tell me much, and then I apploed the grouping algorihtm
# The thing is that the grouping algorithm (of 5min slicing) takes care of all the count, and so does the RSSI limit of -70
# The whitelist decreased the final count by 16 (211 to 195)

# In[123]:

import numpy as np
import json
import pandas as pd
import scipy.stats as sm 
import pylab as pl
import collections
import string
import matplotlib.pyplot as pl
c=json.load(open('pui.json'))
pl.rcParams.update(c)
from IPython.display import HTML
get_ipython().magic(u'pylab inline')
import sqlite3


# In[124]:

#Connecting to database using connect
conn = sqlite3.connect('log.db')
#cursor to move through the tables in the database, we have three tables,probes,pircounts and messages
cur = conn.cursor()
#First we will work with probes data
#Generating empty list to store columns for probes data
#There are 5 columns orginally in the probes table but we use only 3 from them,hence creating only 3 lists
dtg_mac = []
mac_mac = []
rssi_mac = []


for row in cur.execute('SELECT * FROM probes;'):
    #print row
    dtg_mac.append(row[0])
    mac_mac.append(row[1])
    rssi_mac.append(row[2])
    #ssid.append(row[3])
    #oui.append(row[4])
    #count.append(row[5])
print 'This is the length of the probes table',len(dtg_mac)        


# In[125]:

d = {'dtg':dtg_mac,'mac':mac_mac,'rssi':rssi_mac}
mac1 = pd.DataFrame(d)
idx = mac1.groupby('mac').count()
idx.index[0]


# In[126]:

mac_row = []
for i in range(len(idx)):
    if idx.dtg[i] >= 67 :
        mac_row.append(idx.index[i])


# In[127]:

for i in range(len(mac_row)):
    
    mac1 = mac1[mac1.mac != mac_row[i]]


# In[128]:

#as we have removed some values,we need to set the index back to right and not with missng values
#if this is not done , the data shows index as 1,3,5,... which is not desired as looping is done on this data further ahead
print len(mac1)
mac1.index = range(len(mac1))
mac1


# In[131]:

mac1['date']=pd.to_datetime(mac1['dtg'])
mac1['hour']=mac1['date'].dt.hour
mac1['minute']=mac1['date'].dt.minute


# In[132]:

r_mac1=[]


for i in range(len(mac1)):
    #print 'ji'
    if str(mac1['date'][i])[0:10]=='2015-09-17': 
        r_mac1.append(i)
        
m_mac1 = mac1['hour'][min(r_mac1):max(r_mac1)]
k_mac1 = list (m_mac1)
print len(m_mac1)        


# In[133]:

#creating a new dataframe so that we work on only that day from the data
day_9_17_mac1 = mac1[min(r_mac1):max(r_mac1)]
#Keeping all mac addresses above -70, low signal strenght,
#This helps to filter out extraneous data before,without even applying any cleaning algorithm
day_9_17_mac1 = day_9_17_mac1[(day_9_17_mac1['rssi']> -70)]
length = len(day_9_17_mac1)

#Having list of all mac addresses for use 
mac_day = list(day_9_17_mac1['mac'])
print min(r_mac1)


# In[134]:

for i in range(len(day_9_17_mac1)):
    if (day_9_17_mac1['rssi'].iloc[i] > -70):
        print i 


# In[135]:

mac_day_set = set(mac_day)
print len(mac_day_set)


# In[136]:

mac_day


# In[137]:

new_dict = dict(counter)
for i in new_dict:
    print i 
    print new_dict[i]*1.0/len(counter)


# In[138]:

new_dict['fc:c2:de:7f:5f:f4']
    
    


# In[139]:


row_mac1 = []
remove_mac = []
for k in range(0,24):
    #24 hours
    #You can do it for the whole day to see if >-70 would remove them or not 
    row_mac1.append(k_mac1.count(i))
    #Getting hourly data depending on k value
    mac1_hour = mac1[min(r_mac1):max(r_mac1)][mac1['hour'][min(r_mac1):max(r_mac1)] == k]
    #pir1_hour = pir1[min(r_pir1):max(r_pir1)][pir1['hour'][min(r_pir1):max(r_pir1)] == k]
    #print mac1_hour['minute'].head()
    for i in range(12):
        #slicing into 5 minutes, range as 12 value as an hour gets divided into 12 equal 5 minutes
        #this loop counts the number of each mac address occurs in each 5 minute of what hour
        #it also compares with the pir count for that hour - just to see how it varies
        mac1_5minute = []
        #pir1_5minute = []
        mac1_5minute = mac1_hour[(mac1['minute'] >= i*5) & (mac1['minute'] <= (i+1)*5)]
        mac = list((mac1_5minute['mac']).astype(str))
        counter = collections.Counter(mac1_5minute['mac'])
        
        #pir1_5minute = pir1_hour[(pir1['minute'] >= i*5) & (mac1['minute'] <= (i+1)*5)]
        
            
        #print mac1_5minute 
        #counter1 = collections.Counter(pir1_5minute['count'])
        prob = []
        macid = []
        print 'hour',k ,'this is minute',i*5 , 'and mac count in this 5min is',len(counter)
        print ''
        #print counter
        new_dict = dict(counter)
        
        for i in new_dict:
            if new_dict[i]>=20:
                remove_mac.append(i)
            macid.append(i)
            a = float("{0:.2f}".format(new_dict[i]*1.0/len(mac))) #Limiting to two decimal points
            prob.append(a)
            
            
        
        print dict(zip(macid, prob))
        
        
        counter_list = list(counter)
        #print counter_list
        print ''
        if k <=5:
            #counter_list = list(counter)
            remove_mac = remove_mac + counter_list
            
            
    counter = collections.Counter(mac1_hour['mac'])
    
   
    


# In[140]:

whitelist = set(remove_mac)


# In[141]:

print len(whitelist)
print len(remove_mac)


# In[159]:

print len(mac_day_set)
whitelist = list(whitelist)


# In[143]:

for i in range(len(whitelist)):
    day_9_17_mac1 = day_9_17_mac1[day_9_17_mac1['mac']!=whitelist[i]]


# In[144]:

mac_set = set(day_9_17_mac1['mac'])
mac_set = list(mac_set)
print len(mac_set)
print type(mac_set)
#generation a zeroes list to store count for mac address
count_mac = [0]*len(mac_set)


# In[145]:

len(day_9_17_mac1)


# In[149]:

print len(day_9_17_mac1)
day_9_17_mac1['index'] = range(len(day_9_17_mac1))


# In[150]:

mac_day_set = set(mac_day)
print len(mac_day_set)


# In[151]:

day_9_17_mac1.head()


# In[152]:

for j in range(len(mac_set)):
    #print j 
    dataframe_permac = day_9_17_mac1[['mac','index']][day_9_17_mac1['mac'] == mac_set[j]]
    #working with lists , on hourly occurrence of an individual mac address
    l_hour = day_9_17_mac1['hour'][day_9_17_mac1['mac'] == mac_set[j]]
    l_minute = day_9_17_mac1['minute'][day_9_17_mac1['mac'] == mac_set[j]]
    l_hour = list (l_hour)
    l_minute = list (l_minute)
    
    occ = len(dataframe_permac)
    #print occ,'occ' , was just wile testing 
    occ1 = occ - 1
    #print occ1,'occ1'
    if occ!= 1 :
        #print 'occ loop'
        for i in range(occ):
            #print 'for loop'
            if (i != occ1):
                #we need to check for mac addresses occurring in an hour
                #see if they are consecutive in minutes-if yes- group them as one
                #i.e. remove all but one,but we check through all the minutes,
                #hence the minute segregation at the start of this ipynb comes handy 
                #print 'for occ1'
                if (l_hour[i] == l_hour[i+1]):
                    #print 'T in hour'
                    #print dataframe_permac['mac']
                    if (l_minute[i] == l_minute[i+1]):
                        #print 't in 1min'
                        day_9_17_mac1 = day_9_17_mac1 [day_9_17_mac1['index']!=(dataframe_permac['index'].iloc[i+1]) ]
                    elif (int(l_minute[i+1] - l_minute[i]) < 15) :
                        #print i 
                        #from the data that I had observed on printing, mac addresses usually grouped around 10-15 minutes 
                        #for an hour ,and would be present in different hours
                        #this might be because we had cleaned the dataset above >-70
                        #we can experiment with the numbers
                        day_9_17_mac1 = day_9_17_mac1[day_9_17_mac1['index'] != (dataframe_permac['index'].iloc[i+1]) ]





# In[153]:

#day_9_17_mac1[day_9_17_mac1['mac'] == mac_set[112] ]
print len(day_9_17_mac1)
#Checking reduced length again
#Just to keep a track, we had started with 18080, then dropped ot 858(after removeing >-70), and now 219.


# In[154]:

day_9_17_mac1


# In[155]:

#plotting between 6am to 12 pm
hour_mac_final = list(day_9_17_mac1['hour'])

k = []
for i in range (6,23):
    k.append(hour_mac_final.count(i))
print (k)    


# In[156]:

l=range(6,24)
print l


# In[158]:

fig, ax = plt.subplots(1, 1)
ax.hist(hour_mac_final,l,color='b',alpha=0.7,label='Mac Counts with Highest Value as =%i'%max(k))
ax.set_xlabel('In 18 hours')
ax.set_ylabel('Count')
xticks(range(6,24)) 
#yticks(range(0,32,1))
#ax.hist(k_pir1 ,l,color='g',alpha=0.7,label='Pir Counts with Highest Value as =%i'%max(k_pir1))
ax.set_ylim
pl.grid(True)
ax.legend()
pl.show()


# In[ ]:



