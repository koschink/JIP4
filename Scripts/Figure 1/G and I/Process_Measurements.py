# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 13:42:59 2015

@author: kaysch
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
print(dir_name)
print(datapath)
splits = dir_name.split('_')
#print splits[0]
#print splits[1]
savepath = datapath + "/Measurements"


Channel_1 = []
Channel_2 = []
files = glob.glob(savepath+"/*.csv")

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
    df_Channel1= df["Channel 1"]
    df_Channel2 = df["Channel 2"]
    #df11 = df2.apply(f2)
 #   df1["Norm"] = df1["Mean_Intensity"] - df1["Center_Intensity_Channel1"]
#    df1["Norm2"] = df11["Mean_Intensity_Perimeter"]
#    df1["Norm3"] = df11["Center_Intensity_Channel1"]
#        
    #print df1["Mean_Intensity"]    
    Channel_1.append(df_Channel1)
    Channel_2.append(df_Channel2)
    
    #list2.append(df11)

df3 = pd.concat(Channel_1, axis=1)
df4 = pd.concat(Channel_2, axis=1)

df5 = df3.copy()


#
df6 = df4.copy()

#
#
##df12 = df3.apply(f2)
df5[:60].apply(normalisation).mean(axis=1).plot()
df6[:60].apply(normalisation).mean(axis=1).plot()


save_plot = datapath + "/Plots/plot1.png"
plt.savefig(save_plot)

df5[:40].apply(normalisation).plot(legend = False)
save_plot = datapath + "/Plots/plot2.png"
plt.savefig(save_plot)
df6[:40].apply(normalisation).plot(legend = False)
save_plot = datapath + "/Plots/plot3.png"
plt.savefig(save_plot)

print("Analysed tracks: " + str(len(df6.columns)))

save_excel = datapath +"/excel/" + splits[0]+ ".xls"
print(save_excel)
df5[:60].apply(normalisation).to_excel(save_excel)
save_excel = datapath +"/excel/" + splits[1]+ ".xls"
print(save_excel)
df6[:60].apply(normalisation).to_excel(save_excel)

