#!/usr/bin/env python
# coding: utf-8

# In[15]:


# import required libraries
import pandas as pd
from sqlalchemy import create_engine, text, exc
import sqlalchemy.types
from sqlalchemy.orm import sessionmaker
from pathlib import Path
import psycopg2
from psycopg2 import connect
from psycopg2.extras import DictConnection
from configparser import ConfigParser
import csv
import os
import sys


# In[ ]:


Data Extraction processes


# In[18]:


# define file paths 

os.chdir(r"C:\Users\PC\Documents\ACC 2023\DET Program\Capstone Project")

# import PCF data
file = r"C:\Users\PC\Documents\ACC 2023\DET Program\Capstone Project/CarbonCatalogueData.csv"


# In[19]:


# read csv file

PCF_data = pd.read_csv(file, encoding = 'unicode_escape')


# In[ ]:


Data transformation processes


# In[ ]:





# In[ ]:




