
# coding: utf-8

# In[2]:

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


# In[53]:

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


# In[54]:

#Doing the same for pircounts table, with date(date+time actually timestamp) and pircount as two columns
dtg_pir = []
count_pir = []
for row in cur.execute('SELECT * FROM pircounts;'):
    dtg_pir.append(row[0])
    count_pir.append(row[1])
    


# In[55]:

#creating dictionary out of it 
d = {'dtg':dtg_mac,'mac':mac_mac,'rssi':rssi_mac}
e = {'dtg':dtg_pir,'count':count_pir}


# In[56]:

#creating pandas dataframe from it
mac1 = pd.DataFrame(d)
pir1 = pd.DataFrame(e)
#probes = pd.read_csv('C:\Users\PRIYA  SINGH\sqlite\Data\Data\First\probes.csv')


# In[57]:

idx = mac1.groupby('mac').count()


# In[58]:

idx.index[0]


# In[59]:

mac_row = []
for i in range(len(idx)):
    if idx.dtg[i] >= 67 :
        mac_row.append(idx.index[i])


# In[60]:

for i in range(len(mac_row)):
    
    mac1 = mac1[mac1.mac != mac_row[i]]


# In[61]:

#as we have removed some values,we need to set the index back to right and not with missng values
#if this is not done , the data shows index as 1,3,5,... which is not desired as looping is done on this data further ahead
print len(mac1)
mac1.index = range(len(mac1))
mac1


# In[12]:

print 'Pir data',len(pir1)
pir1


# In[62]:

#Adding more fields like hour and minute as cleaning is done via slicing on minutes and mac count is observed on an hourly basis
mac1['date']=pd.to_datetime(mac1['dtg'])
mac1['hour']=mac1['date'].dt.hour
mac1['minute']=mac1['date'].dt.minute
pir1['date']= pd.to_datetime(pir1['dtg'])
pir1['hour']= pir1['date'].dt.hour
pir1['minute'] = pir1['date'].dt.minute


# In[14]:

#I took the data 9th September,2015-Thursday as data for this was avalaible all throughout 
r_pir1=[]
for i in range(len(pir1)):
    
    if str(pir1['date'][i])[0:10]=='2015-09-17': 
        r_pir1.append(i)
        
#This gives the index range of this date        
print min(r_pir1)
print max(r_pir1)
      


# In[15]:

print len(r_pir1)
#Did it to have a handy list for plotting,dataframe doesnt get plotted
m_pir1 = pir1['hour'][min(r_pir1):max(r_pir1)]
k_pir1 = list (m_pir1)
print m_pir1


# In[16]:

row_pir1=[]

for i in range(0,24):
    
    row_pir1.append(k_pir1.count(i))
        

#Count in each hour is stored in the list    
print row_pir1
print len(row_pir1)
print max(row_pir1)
l = range(0,24)


# In[18]:

#Plotting from 6AM to 12AM
fig, ax = plt.subplots(1, 1)
plt.hist(k_pir1[6:],l[6:],color='g',alpha=0.7,label='Counts with Highest Value as =%i'%max(row_pir1))
ax.set_xlabel('In 24 hours')
ax.set_ylabel('Count')
xticks(range(6,24)) 
yticks(range(0,max(row_pir1),100))

ax.set_ylim(0,30)

ax.legend()
pl.show()


# In[19]:

#Seeing the dates in the mac data- probes table after cleaning 
#Date chosen here also would be same as above - 9th September
mac1['date']


# In[63]:

#Getting hourly count as was done for pircounts,same method
r_mac1=[]


for i in range(len(mac1)):
    #print 'ji'
    if str(mac1['date'][i])[0:10]=='2015-09-17': 
        r_mac1.append(i)
        
        


# In[64]:

m_mac1 = mac1['hour'][min(r_mac1):max(r_mac1)]
k_mac1 = list (m_mac1)
print len(m_mac1)


# In[65]:

#creating a new dataframe so that we work on only that day from the data
day_9_17_mac1 = mac1[min(r_mac1):max(r_mac1)]
#Keeping all mac addresses above -70, low signal strenght,
#This helps to filter out extraneous data before,without even applying any cleaning algorithm
day_9_17_mac1 = day_9_17_mac1[(day_9_17_mac1['rssi']> -70)]
length = len(day_9_17_mac1)
#Keeping a pir data for that date also
day_9_17_pir1 = pir1[min(r_pir1):max(r_pir1)]
#Having list of all mac addresses for use 
mac_day = list(day_9_17_mac1['mac'])
print min(r_mac1)


# In[66]:

#I think I wanted to check the index which was not necessary as a new data frame is what I created which always has correct 
#Index- clearing the output for this 
for i in range(len(day_9_17_mac1)):
    if (day_9_17_mac1['rssi'].iloc[i] > -70):
        print i 


# In[67]:

#to get distinct mac addresses in a day after some intial cleaning, to get an idea of average unique mac adddress in a day
mac_day_set = set(mac_day)
print len(mac_day_set)


# In[68]:

counter=collections.Counter(mac_day)
print len(counter)

#HTML("<i>Italic text</i>")

print 'asdf' 
HTML("<i>Italic text</i>")


# In[69]:

row_mac1 = []
remove_mac = []
for k in range(0,24):
    #24 hours
    #I didnt do it from 6am to 12 am as I wanted too see if >-70 would remove them or not 
    row_mac1.append(k_mac1.count(i))
    #Getting hourly data depending on k value
    mac1_hour = mac1[min(r_mac1):max(r_mac1)][mac1['hour'][min(r_mac1):max(r_mac1)] == k]
    pir1_hour = pir1[min(r_pir1):max(r_pir1)][pir1['hour'][min(r_pir1):max(r_pir1)] == k]
    #print mac1_hour['minute'].head()
    for i in range(12):
        #slicing into 5 minutes, range as 12 value as an hour gets divided into 12 equal 5 minutes
        #this loop counts the number of each mac address occurs in each 5 minute of what hour
        #it also compares with the pir count for that hour - just to see how it varies
        mac1_5minute = []
        pir1_5minute = []
        mac1_5minute = mac1_hour[(mac1['minute'] >= i*5) & (mac1['minute'] <= (i+1)*5)]
        pir1_5minute = pir1_hour[(pir1['minute'] >= i*5) & (mac1['minute'] <= (i+1)*5)]
        counter = collections.Counter(mac1_5minute['mac'])
        #print mac1_5minute 
        #counter1 = collections.Counter(pir1_5minute['count'])
        print 'hour',k ,'this is ',i*5 , 'minute with pir as', len(pir1_5minute),'and mac count in this 5min is',len(counter)
        print ''
        print counter
        
        counter_list = list(counter)
        print counter_list
        print ''
        if k <=5:
            #counter_list = list(counter)
            remove_mac = remove_mac + counter_list
            
            
    counter = collections.Counter(mac1_hour['mac'])
   
    
    


# In[70]:

#to see the reduction in length we got
len(day_9_17_mac1)


# In[91]:

#length of mac dataset we are planning to remove 
remove_mac_set = set(remove_mac)
(remove_mac_set)


# In[80]:

day_9_17_mac1.head()


# In[98]:

#Removing all the mac addresses collected above for time 12am to 6am
import string
for i in (remove_mac_set):
    #print type(str(i))
    day_9_17_mac1 = day_9_17_mac1[day_9_17_mac1.mac != str(i)]


# In[99]:

len(day_9_17_mac1)


# In[101]:

print len(day_9_17_mac1)
day_9_17_mac1['index'] = range(len(day_9_17_mac1))


# In[114]:

mac_set = set(day_9_17_mac1['mac'])
mac_set = list(mac_set)
print len(mac_set)
print type(mac_set)
#generation a zeroes list to store count for mac address
count_mac = [0]*len(mac_set)


# In[121]:

day_9_17_mac1


# In[127]:

day_9_17_mac1[day_9_17_mac1['mac']=='04:15:52:4e:78:4d']


# In[125]:

day_9_17_mac1.groupby(day_9_17_mac1.mac).count()


# In[128]:

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
                        day_9_17_mac1 = day_9_17_mac1[day_9_17_mac1['index'] != (dataframe_permac['index'].iloc[i+1]) ]
                    elif (int(l_minute[i+1] - l_minute[i]) < 15) :
                        #print i 
                        #from the data that I had observed oon printing, mac addresses usually grouped around 10-15 minutes 
                        #for an hour ,and would be present in different hours
                        #this might be because we had cleaned the dataset above >-70
                        #we can experiment with the numbers
                        day_9_17_mac1 = day_9_17_mac1[day_9_17_mac1['index'] != (dataframe_permac['index'].iloc[i+1]) ]




                


# In[130]:

#day_9_17_mac1[day_9_17_mac1['mac'] == mac_set[112] ]
print len(day_9_17_mac1)
#Checking reduced length again
#Just to keep a track, we had started with 18080, then dropped ot 858(after removeing >-70), and now 219.


# In[131]:

day_9_17_mac1


# In[132]:

#plotting between 6am to 12 pm
hour_mac_final = list(day_9_17_mac1['hour'])

k = []
for i in range (6,23):
    k.append(hour_mac_final.count(i))
print (k)    


# In[133]:

l=range(6,24)
print l


# In[137]:

fig, ax = plt.subplots(1, 1)
ax.hist(hour_mac_final,l,color='b',alpha=0.7,label='Mac Counts with Highest Value as =%i'%max(k))
ax.set_xlabel('In 18 hours')
ax.set_ylabel('Count')
xticks(range(6,24)) 
#yticks(range(0,32,1))
ax.hist(k_pir1 ,l,color='g',alpha=0.7,label='Pir Counts with Highest Value as =%i'%max(k_pir1))
ax.set_ylim
pl.grid(True)
ax.legend()
pl.show()


# In[ ]:

#I changed the value of 15 minutes, to 7 and 10 and on plotting usually there is a 
#difference in the peak value of mac in this plot 


# In[ ]:



