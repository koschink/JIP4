# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:51:35 2020

@author: kaysch
"""
#Normalize line plots

import pandas as pd
import glob
print("check")
files3 = glob.glob("G:/old_drive/Kia_Wee_Work/Jip4/Lineplots/RPE_Phafin1_2_JIP3_rawlineplots/Phafin1"+"/*.csv")
print(files3)

for i in files3:
    
    filename = i
    savename =  filename[:-4]+"_normalized.xlsx"
    
    
    df1 = pd.read_csv(filename, index_col=0)
    
    
    # Generate the mean of rows 0-17 and rows 33-end
    df_upper = df1.iloc[0:20] 
    df1_norm = df1.div(df_upper.mean())
    df1_norm.to_excel(savename)








