# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:51:35 2020

@author: kaysch
"""
#Normalize line plots

import pandas as pd
import glob

files = glob.glob("d:/kiawee2/*.csv")

for i in files:
    
    filename = i
    savename =  filename[:-4]+"_normalized.xlsx"
    
    
    df1 = pd.read_csv(filename, index_col=0)
    
    
    # Generate the mean of rows 0-17 and rows 33-end
    df_upper = df1.iloc[0:17] 
    df_lower = df1.iloc[33:]
    df_combined=pd.concat((df_upper,df_lower), axis=0)
    df1_norm = df1.div(df_combined.mean())
    df1_norm.to_excel(savename)








