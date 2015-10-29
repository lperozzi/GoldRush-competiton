# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:14:08 2015

@author: lorenzoperozzi
"""

import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
#sns.set_style("whitegrid")
sns.set_color_codes()
from sklearn.preprocessing import MinMaxScaler
from matplotlib.ticker import ScalarFormatter


folder = 'data'
df = pd.read_csv(folder+'/database_processed.csv')
df_raw = pd.read_csv(folder+'/database.csv')

df = df.set_index(list(df)[0])


df1 = df[df['STRUCT_CAT'].notnull() & df['AU_AVG_GT'].notnull() & df['LITHO_CAT']]

df1_raw = df_raw[df_raw['CODE_STRUCT'].notnull() & df_raw['AU_AVG_GT'].notnull() & df_raw['LITHO_DESC']]


# Plotting some data

#Scatter plot Litho description vs AU_AVG_GT
ax = sns.stripplot(y="LITHO_DESC", x="AU_AVG_GT", data=df1_raw, jitter=False, size=8,
                    edgecolor="gray", alpha=.5);
axes = ax.axes  
axes.set_xlim(-100,)                  
plt.show()

#Scatter plot Structural code vs AU_AVG_GT
ax = sns.stripplot(y="CODE_STRUCT", x="AU_AVG_GT", data=df1_raw, jitter=False, size=8,
                    edgecolor="gray", alpha=.5, palette='Blues_d');
axes = ax.axes  
axes.set_xlim(-100,)                  
plt.show()

# Histograms of AU_AVG_GT            
mybins=np.logspace(-3,np.log(20),30)    
ax = sns.distplot(df1['AU_AVG_GT'],bins=mybins, color='k', kde=False)
axes = ax.axes           
axes.set_xscale('log')
axes.set_xticklabels([" ","0.001", "0.01", "0.1","1","10","100","1000"])
plt.show()

