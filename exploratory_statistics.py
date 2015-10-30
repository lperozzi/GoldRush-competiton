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

df2 = df[df['AU_AVG_GT'].notnull() & df['LITHO_CAT']]
# Only notnull values
df1_raw = df_raw[df_raw['CODE_STRUCT'].notnull() & df_raw['AU_AVG_GT'].notnull() & df_raw['LITHO_DESC']]
# Only notnull values except for the code struct
df2_raw = df_raw[df_raw['AU_AVG_GT'].notnull() & df_raw['LITHO_DESC']]

# Plotting some data

#Scatter plot Litho description vs AU_AVG_GT
f, (ax1, ax2) = plt.subplots(2,figsize=(8,8))
sns.stripplot(y="LITHO_DESC", x="AU_AVG_GT", data=df1_raw, jitter=False, size=8,
                    edgecolor="gray", alpha=.5, ax=ax1);
ax1.set_xlim(-100,) 
ax1.set_title('Drop NaN in CODE_STRUCT')                 

sns.stripplot(y="LITHO_DESC", x="AU_AVG_GT", data=df2_raw, jitter=False, size=8,
                    edgecolor="gray", alpha=.5, ax=ax2);
ax2.set_xlim(-100,) 
ax2.set_title('Keep NaN in CODE_STRUCT')
plt.tight_layout()
plt.show()

#Scatter plot Litho description vs CODE_STRUCT
f, (ax1,ax2) = plt.subplots(2,figsize=(8,8))
sns.stripplot(y="LITHO_CAT", x="STRUCT_CAT", data=df1, jitter=False, size=8,
                    edgecolor="gray", alpha=.5, ax=ax1);
#ax1.set_xlim(-100,) 
ax1.set_title('Drop NaN in CODE_STRUCT') 

sns.stripplot(y="LITHO_CAT", x="STRUCT_CAT", data=df2, jitter=False, size=8,
                    edgecolor="gray", alpha=.5, ax=ax2);
#ax1.set_xlim(-100,) 
ax1.set_title('Keep NaN in CODE_STRUCT')    
plt.tight_layout()
plt.show()

#Scatter plot Structural code vs AU_AVG_GT
ax = sns.stripplot(y="CODE_STRUCT", x="AU_AVG_GT", data=df2_raw, jitter=False, size=8,
                    edgecolor="gray", alpha=.5, palette='Blues_d');
axes = ax.axes  
axes.set_xlim(-100,)                  
plt.show()

# Histograms of AU_AVG_GT            
mybins=np.logspace(-3,np.log(20),30)    
ax = sns.distplot(df1_raw['AU_AVG_GT'],bins=mybins, color='k', kde=False)
axes = ax.axes           
axes.set_xscale('log')
axes.set_xticklabels([" ","0.001", "0.01", "0.1","1","10","100","1000"])
plt.show()

