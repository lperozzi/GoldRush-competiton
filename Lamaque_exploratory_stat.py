# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:14:08 2015

@author: lorenzoperozzi
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set_style("whitegrid")
sns.set_color_codes()
sns.set_palette('RdYlBu')

data = 'data'
img = 'img'
# Original dataset
lamaque = pd.read_csv(data+'/lamaque_processed_description.csv')

#Scatter plot Litho description vs AU_AVG_GT
f, (ax) = plt.subplots(1,figsize=(8,4))            
sns.stripplot(y="LITHO_DESC", x="AU_AVG_GT", data=lamaque, jitter=False, size=8,
              edgecolor="gray", alpha=.5, ax=ax);
ax.set_xlim(-100,) 
plt.tight_layout()
f.savefig('img/Lamaque_lithoVSgld.png',dpi=300)

f, (ax) = plt.subplots(1,figsize=(8,4))            
sns.stripplot(y="CODE_STRUCT", x="AU_AVG_GT", data=lamaque, jitter=False, size=8,
              edgecolor="gray", alpha=.5, ax=ax);
ax.set_xlim(-100,) 
plt.tight_layout()
f.savefig('img/Lamaque_lithoVSgld.png',dpi=300)
#


#Scatter plot DISTANCE_TO_FAULT  vs AU_AVG_GT
sns.set_style("whitegrid")
g = sns.lmplot(x="DISTANCE_TO_FAULT", y="AU_AVG_GT", hue="LITHO_DESC", col="LITHO_DESC", 
               fit_reg=False, size=3,col_wrap=4,palette="RdYlBu",data=lamaque)
g.savefig('img/Lamaque_distfaultVSgld.png', transparent=True, bbox_inches='tight', pad_inches=0)
             
#Scatter plot DISTANCE_TO_FAULT  vs DISTANCE_TO_GLD
sns.set_style("whitegrid")
g = sns.lmplot(x="DISTANCE_TO_GLD", y="DISTANCE_TO_FAULT", hue="LITHO_DESC", col="LITHO_DESC", 
               fit_reg=False, size=3,col_wrap=4,palette="RdYlBu",data=lamaque)
g.savefig('img/Lamaque_distfaultVSdistgld.png', transparent=True, bbox_inches='tight', pad_inches=0)
