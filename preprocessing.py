# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:29:08 2015

@author: lorenzoperozzi
"""
import numpy as np
import pandas as pd



folder = 'data'
df = pd.read_csv(folder+'/database.csv')

df = df.set_index(list(df)[3])


#Lithology description: 
litho = pd.unique(df.LITHO_DESC.ravel())
litho_dict = {value: key for (key, value) in enumerate(litho)}

df['LITHO_CAT'] = df['LITHO_DESC'].apply(lambda x: litho_dict[x])
df['LITHO_CAT'] = df.LITHO_CAT.replace([9,7], np.nan)


##Structure categroy: CIS (cisaillement) & FAI (faille)
struct = pd.unique(df.CODE_STRUCT.ravel()) 
struct_dict = {value: key for (key, value) in enumerate(struct)}

df['STRUCT_CAT'] = df['CODE_STRUCT'].apply(lambda x: struct_dict[x])
df['STRUCT_CAT'] = df.STRUCT_CAT.replace(0, np.nan)


df.to_csv('data/database_processed.csv',columns=['X','Y','Z','LITHO_CAT','STRUCT_CAT','AU_AVG_GT'])

#df_test = df.head(1000)
#
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(df_test.X, df_test.Y, df_test.Z, c=df_test.AU_AVG_GT)




