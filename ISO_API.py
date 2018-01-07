# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pyiso import client_factory
import pandas as pd
import os

#get logins
#Seperate file which git ignores in .gitignore called secrets.txt
#contains ISONE_USERNAME=username
#         ISONE_PASSWORD=password
with open('secrets.txt') as f:
    lines = f.readlines()
    for line in lines:
        (key,val) = line.split(":")
        os.environ[key] = str(val).rstrip("\n")

#Get NE hook
isone = client_factory('ISONE', timeout_seconds=60)
data = isone.get_load(latest=True)
df = pd.DataFrame(data)

#print(df)

#Get CAISO hook
caiso = client_factory('CAISO')
caiso_load = isone.get_load(latest=True)
caiso_generation = isone.get_generation(latest=True)
#caiso_trade = isone.get_trade(latest=True)
caiso_load_df = pd.DataFrame(caiso_load)
print(caiso_load_df)
caiso_generation_df = pd.DataFrame(caiso_generation)
#caiso_trade_df = pd.DataFrame(caiso_trade)


