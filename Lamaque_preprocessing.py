# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:29:08 2015

@author: lorenzoperozzi
"""
import numpy as np
#import scipy.spatial
import pandas as pd
#import timeit
from sklearn.metrics.pairwise import euclidean_distances


folder = 'data'
df = pd.read_csv(folder+'/database.csv')

df = df.set_index(list(df)[3])

#Lamaque site
limitl_x = [293500,295000]
limitl_y = [5320950,5331000]

lamaque = df[(df['X'] < limitl_x[1]) & (df['X'] > limitl_x[0])]
lamaque = lamaque[(lamaque['Y'] < limitl_y[1]) & (lamaque['Y'] > limitl_y[0])]
df = lamaque

#Lithology description: 
litho = pd.unique(df.LITHO_DESC.ravel())
litho_dict = {value: key for (key, value) in enumerate(litho)}

df['LITHO_CAT'] = df['LITHO_DESC'].apply(lambda x: litho_dict[x])
df['LITHO_CAT'] = df.LITHO_CAT.replace([9,7], np.nan)


##Structure category: CIS (cisaillement) & FAI (faille)
struct = pd.unique(df.CODE_STRUCT.ravel()) 
struct_dict = {value: key for (key, value) in enumerate(struct)}

df['STRUCT_CAT'] = df['CODE_STRUCT'].apply(lambda x: struct_dict[x])
df['STRUCT_CAT'] = df.STRUCT_CAT.replace(0, np.nan)




points = df[['X','Y','Z']]
points = points.as_matrix()
points_test = points[0:1000,:]

######  VARIABLE DISTANCE TO FAULT (OR SHEAR)  ########################

fault = df[df['CODE_STRUCT'] == 'FAI']
fault = fault[['X','Y','Z']]
fault_array = fault.as_matrix()

shear = df[df['CODE_STRUCT'] == 'CIS']
shear = shear[['X','Y','Z']]
shear_array = shear.as_matrix()

ShearFault = np.vstack((fault_array,shear_array))



dist_fault = []
for c in points:
    d = euclidean_distances(c, ShearFault)
    d = np.min(d)
    dist_fault.append(d)
    
df.loc[:,'DISTANCE_TO_FAULT'] = pd.Series(dist_fault, index=df.index)
df['DISTANCE_TO_FAULT'] = df['DISTANCE_TO_FAULT'].astype(float)

######  VARIABLE DISTANCE TO Quartz-tourmaline veins   ########################


qtz_vein = df[df['LITHO_DESC'] == 'Quartz-Tourmaline Veins']
qtz_vein = qtz_vein[['X','Y','Z']]
qtz_vein = qtz_vein.as_matrix()

dist_qtz = []
for c in points:
    d = euclidean_distances(c, qtz_vein)
    d = np.min(d)
    dist_qtz.append(d)
    

df.loc[:,'DISTANCE_TO_QTZVEINS'] = pd.Series(dist_qtz, index=df.index)
df['DISTANCE_TO_QTZVEINS'] = df['DISTANCE_TO_QTZVEINS'].astype(float)

######  VARIABLE DISTANCE TO Diorite   ########################


diorite = df[df['LITHO_DESC'] == 'Diorite']
diorite = diorite[['X','Y','Z']]
diorite = diorite.as_matrix()

dist_diorite = []
for c in points:
    d = euclidean_distances(c, diorite)
    d = np.min(d)
    dist_diorite.append(d)
    

df.loc[:,'DISTANCE_TO_DIORITE'] = pd.Series(dist_diorite, index=df.index)
df['DISTANCE_TO_DIORITE'] = df['DISTANCE_TO_DIORITE'].astype(float)

######  VARIABLE DISTANCE TO Granodiorite   ########################


granodiorite = df[df['LITHO_DESC'] == 'Granodiorite']
granodiorite = granodiorite[['X','Y','Z']]
granodiorite = granodiorite.as_matrix()

dist_granodiorite = []
for c in points:
    d = euclidean_distances(c, granodiorite)
    d = np.min(d)
    dist_granodiorite.append(d)
    

df.loc[:,'DISTANCE_TO_GRANODIORITE'] = pd.Series(dist_granodiorite, index=df.index)
df['DISTANCE_TO_GRANODIORITE'] = df['DISTANCE_TO_GRANODIORITE'].astype(float)

######  VARIABLE DISTANCE TO EARLY QUARTZ DIORITE   ########################

earlyquartzdiorite = df[df['LITHO_DESC'] == 'Early Quartz Diorite']
earlyquartzdiorite = earlyquartzdiorite[['X','Y','Z']]
earlyquartzdiorite = earlyquartzdiorite.as_matrix()

dist_earlyquartzdiorite = []
for c in points:
    d = euclidean_distances(c, earlyquartzdiorite)
    d = np.min(d)
    dist_earlyquartzdiorite.append(d)
    

df.loc[:,'DISTANCE_TO_EQDIORITE'] = pd.Series(dist_earlyquartzdiorite, index=df.index)
df['DISTANCE_TO_EQDIORITE'] = df['DISTANCE_TO_EQDIORITE'].astype(float)

######  VARIABLE DISTANCE TO Gold   ########################


gold = df[df['AU_AVG_GT'] >= 5]
gold = gold[['X','Y','Z']]
gold = gold.as_matrix()

dist_gld = []
for c in points:
    d = euclidean_distances(c, gold)
    d = np.min(d)
    dist_gld.append(d)
    

df.loc[:,'DISTANCE_TO_GLD'] = pd.Series(dist_gld, index=df.index)
df['DISTANCE_TO_GLD'] = df['DISTANCE_TO_GLD'].astype(float)

######  VARIABLE GOLD class   ########################
# selecto only AU_AVG_GT that are notnull
df = df[df['AU_AVG_GT'].notnull() & df['AU_AVG_GT'] != 0]

mybins = np.array([0.0,0.1,1,5,50,26314])
#mybins = np.array([np.min(df.AU_AVG_GT),1,np.max(df.AU_AVG_GT)])

# separate AU_AVG_GT into 5 classes
df['AU_CLASS'] = pd.cut(df['AU_AVG_GT'], mybins, labels=["very poor","poor","medium","rich","very rich"])
#df.loc[:,'AU_CLASS'] = pd.cut(df['AU_AVG_GT'], mybins, labels=["poor","rich"])

df['AU_CLASS_CAT'] = pd.cut(df['AU_AVG_GT'], mybins, labels=[1,2,3,4,5])
#df1.loc[:,'AU_CLASS_CAT'] = pd.cut(df1['AU_AVG_GT'], mybins, labels=[0,1])
df['AU_CLASS_CAT'] = df['AU_CLASS_CAT'].astype(int)

######  SAVING TO DISK  ########################

df.to_csv('data/lamaque_processed_description.csv',columns=['X','Y','Z','LITHO_DESC','AU_AVG_GT','DISTANCE_TO_FAULT','DISTANCE_TO_QTZVEINS','DISTANCE_TO_DIORITE','DISTANCE_TO_GRANODIORITE','DISTANCE_TO_EQDIORITE','DISTANCE_TO_GLD','AU_CLASS' ])
df.to_csv('data/lamaque_processed_categories.csv',columns=['X','Y','Z','LITHO_CAT','AU_AVG_GT','DISTANCE_TO_FAULT','DISTANCE_TO_QTZVEINS','DISTANCE_TO_DIORITE','DISTANCE_TO_GRANODIORITE','DISTANCE_TO_EQDIORITE','DISTANCE_TO_GLD','AU_CLASS_CAT'])

