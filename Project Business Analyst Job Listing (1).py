#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

industry=input("What is your industry?")
pref_rating=float(input('What rating woud company would you like'))


df=pd.read_csv(r"C:\Users\TLS\OneDrive\Desktop\BusinessAnalyst.csv")

df.columns
df=df.drop(["Unnamed: 0","index","Job Description","Type of ownership"],axis=1)
# df.isna().sum()

avg_TE=df["Total Employees"].mean()
avg_MinR=df["Minimum Revenue"].mean()
avg_MaxR=df["Maximum Revenue"].mean()
MaxRev=max(df["Minimum Revenue"])


df1=df.fillna({"Total Employees":avg_TE,"Minimum Revenue":avg_MinR,"Maximum Revenue":avg_MaxR})


# In[4]:


df_ea= df1[df1['Easy Apply']!=-1]
df_ea.shape
df_ea["Should Apply"]=np.where(df_ea["Rating"]>=pref_rating,"Apply","Dont Apply")
df_ea["Have industry experience?"]=np.where(df_ea["Sector"]==industry,"Yes","No")
df_ea["Is company profitable"]=np.where(df_ea["Maximum Revenue"]>=MaxRev,"Yes","No")


# In[32]:


from sklearn.preprocessing import LabelEncoder,OneHotEncoder

le = LabelEncoder()
df_ea['Should Apply TF'] = le.fit_transform(df_ea["Should Apply"])
df_ea['Have Industry experience TF'] = le.fit_transform(df_ea["Have industry experience?"])
df_ea["Is company profitable TF"] = le.fit_transform(df_ea["Is company profitable"])
df_ea["Company name for ML"] = le.fit_transform(df_ea["Company Name"])
df_ea["Job Title for ML"] = le.fit_transform(df_ea["Job Title"])


# In[33]:


df_ea.head(5)


# In[ ]:




