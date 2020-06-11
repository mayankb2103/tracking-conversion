#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json


# In[2]:


df=pd.read_csv("data.csv")


# In[3]:


frames=df.Frame.unique()


# In[4]:


resdct=[]
for frame in frames:
    framedct={"frame":int(frame),"objects":[]}

    df_frame = df[df.Frame==frame]
    for object_id in df_frame["Object ID"]:
        dfid=df[df["Object ID"]==object_id]
        
        df2=dfid[dfid.Frame<=frame][["X1","Y1"]]
        framedct["objects"].append({"id":int(object_id), "pos":df2.values.tolist()})
    resdct.append(framedct)
# print(resdct)
with open("name.json","w") as f:
    json.dump(resdct,f,indent=4)


# In[ ]:




