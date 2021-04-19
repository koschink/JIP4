# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:18:07 2020

@author: user
"""

from __future__ import division

from pandas import *
import pandas as pd
from math import *
import matplotlib.pyplot as plt
import numpy
import glob
import os

   
datapath = os.path.dirname(__file__)
dir_name = os.path.basename(datapath)
#print(dir_name)
#print(datapath)
#splits = dir_name.split('_')
#print(splits[0])
#print(splits[1])
#savepath = datapath + "/Measurements"

basepath = "G:/old_drive/Kia_Wee_Work/Jip4/Lineplots/RPE_Phafin1_2_JIP3_rawlineplots/"
genotype = "Phafin1"
savepath = basepath+genotype+"/"
Channel_1 = []
Channel_2 = []
files = glob.glob(savepath+"Ch1/*.csv")
files2 = glob.glob(savepath+"Ch2/*.csv")

#files = files[1:29]

print(files)

f = lambda x: ((x-x.min())/(x.max()-x.min())*100)
f2 = lambda x: (x/x.max()*100)
f3 = lambda x: (x/x.min())
f4 = lambda x: (x-x.min())
f5 = lambda x: (x/x.mean())

normalisation = f

for csvfiles in files:
    df = pd.read_csv(csvfiles, sep=',', decimal='.', index_col=0)
    df_Channel1= df["Value"]
    #df_Channel2 = df["Channel 2"]
    #df11 = df2.apply(f2)
 #   df1["Norm"] = df1["Mean_Intensity"] - df1["Center_Intensity_Channel1"]
#    df1["Norm2"] = df11["Mean_Intensity_Perimeter"]
#    df1["Norm3"] = df11["Center_Intensity_Channel1"]
#        
    #print df1["Mean_Intensity"]    
    Channel_1.append(df_Channel1)
    #Channel_2.append(df_Channel2)
    
    #list2.append(df11)

df3 = pd.concat(Channel_1, axis=1)
#df4 = pd.concat(Channel_2, axis=1)

df3.to_csv(savepath+genotype+"_Ch1_consol.csv")
df3.to_excel(savepath+genotype+"_Ch1_consol.xls")
print(files2)
for csvfiles2 in files2:
    df = pd.read_csv(csvfiles2, sep=',', decimal='.', index_col=0)
    df_Channel2= df["Value"]
    #df_Channel2 = df["Channel 2"]
    #df11 = df2.apply(f2)
 #   df1["Norm"] = df1["Mean_Intensity"] - df1["Center_Intensity_Channel1"]
#    df1["Norm2"] = df11["Mean_Intensity_Perimeter"]
#    df1["Norm3"] = df11["Center_Intensity_Channel1"]
#        
    #print df1["Mean_Intensity"]    
    Channel_2.append(df_Channel2)
    #Channel_2.append(df_Channel2)
    
    #list2.append(df11)

#df3 = pd.concat(Channel_1, axis=1)
df4 = pd.concat(Channel_2, axis=1)

df4.to_csv(savepath+genotype+"_Ch2_consol.csv")
df4.to_excel(savepath+genotype+"_Ch2_consol.xls")




#SHIFTING SECTION




df5 = df4.copy()

#print df4.head()
#shifting_Matrix = [5,1,9,7,5,4,10,2,1,6,2,9,11,-1,15,21,22,16,3,7]
#shifting_Matrix = [4,11,9,9,10,6,15,]
shifting_matrix = df5[:80].idxmax().tolist()
print(shifting_matrix)
#shifting_matrix[:] = [5 - x for x in shifting_matrix]
#print shifting_matrix
headings = range(1, (len(shifting_matrix)+1))
df5.columns = headings
for position, movement in enumerate(shifting_matrix):
    print(position) 
    print(movement)
    df5.iloc[:, position] = df5.iloc[:,position].shift(25-movement)
#
df6 = df3.copy()
#print df4.head()
#shifting_Matrix = [5,1,9,7,5,4,10,2,1,6,2,9,11,-1,15,21,22,16,3,7]
#shifting_Matrix = [4,11,9,9,10,6,15,]
headings = range(1, (len(shifting_matrix)+1))
df6.columns = headings

for position, movement in enumerate(shifting_matrix):
    print(position) 
    print(movement)
    df6.iloc[:, position] = df6.iloc[:,position].shift(25-movement)
    
    
df6.to_csv(savepath+genotype+"_Ch1_consol_shifted.csv")
df6.to_excel(savepath+genotype+"_Ch1_consol_shifted.xls")   

df5.to_csv(savepath+genotype+"_Ch2_consol_shifted.csv")
df5.to_excel(savepath+genotype+"_Ch2_consol_shifted.xls")
    