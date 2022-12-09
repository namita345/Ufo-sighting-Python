#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv

with open('ufo-sightings.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    print(type(reader))
    print(reader.fieldnames)


# In[7]:


import csv

filepath = "ufo-sightings.csv"

ufosightings = [] 



with open(filepath, 'r') as csvfile: #open with a with statement

  reader = csv.DictReader(csvfile) #load and read into a DictReader

   

  print(type(reader))

   

  for row in reader:

    ufosightings.append(row)

     

    ufosightings_count = len(ufosightings)

     

print(ufosightings_count)


# In[8]:


import csv

filepath = "ufo-sightings.csv"



with open(filepath, 'r') as csvfile: #open with a with statement

  reader = csv.DictReader(csvfile) #load and read into a DictReader

   

  ufosightings = []

  for row in reader:

    ufosightings.append(row)

     

  #print(len(ufosightings))

   

sightings_us = [row for row in ufosightings if row['country'] == 'us']



print(len(sightings_us))


# In[12]:


def is_valid_duration(duration_as_string): #eliminate duration values that don't have a valid duration

# your code here

  try:

    duration = float(duration_as_string)

  

  except ValueError:

   

    return False

  else:

      return duration



fball = [] 



# iterate through the sightings_us



fball = [row for row in sightings_us if is_valid_duration(row["duration (seconds)"]) > 10 and row["shape"] == "fireball"]
for row in fball:

  print(row['datetime'], row['state'])


# In[13]:


fballsorted = sorted(fball, key = lambda x: float(x['duration (seconds)']), reverse=True)





for row in fballsorted:

   

  print((row['datetime'], row['duration (seconds)']))


# In[14]:


#confirmfireball = [row for row in sightings_us if is_valid_duration(row["duration (seconds)"]) and row["shape"] == "fireball"]



for row in sightings_us:

   

   # get the data for shape='fireball' having float of 'duration (seconds)' > 10

  if row["shape"] == "fireball":



    #confirmfireball = [row for row in sightings_us if row["shape"] == "fireball"]

    valid_duration = [row for row in sightings_us if is_valid_duration(row["duration (seconds)"])]



    state = max(valid_duration, key = lambda x: float(x["duration (seconds)"]))

  



    print(state['duration (seconds)'], state['state'])       


# In[ ]:




