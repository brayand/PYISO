# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pyiso import client_factory
import pandas as pd
import os

#get logins
with open('secrets.txt') as f:
    lines = f.readlines()
    for line in lines:
        (key,val) = line.split(":")
        os.environ[key] = str(val).rstrip("\n")

#Get hook
isone = client_factory('ISONE', timeout_seconds=60)

print(isone)

data = isone.get_load(latest=True)

df = pd.DataFrame(data)

print(df)



