# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:29:08 2015

@author: lorenzoperozzi
"""
import pandas as pd
import glob
folder = 'Raw Data 3/Drill Hole Database'


#drillhole = glob.glob(folder+'/*.txt') # ["all the .txt files in the folder", ]
#for i, test in enumerate(drillhole):
#    print test

# reading drilling txt files    
df_assays = pd.read_csv(folder+'/Assays.txt')
df_doubtful = pd.read_csv(folder+'/Doubtful_collar_list_20150910.txt')
df_header = pd.read_csv(folder+'/Header.txt')
df_litho = pd.read_csv(folder+'/Litho.txt')
df_noLithoAssays = pd.read_csv(folder+'/No_lithoAssay_drillhole_list_20150910.txt') 
df_structure = pd.read_csv(folder+'/Structure.txt')
df_survey = pd.read_csv(folder+'/Survey.txt')

# merge the test together
database = pd.merge(df_assays, df_litho, on=['HOLE-ID','FROM_M','TO_M'], how='outer')
database = pd.merge(database,df_structure, on=['HOLE-ID','FROM_M','TO_M'], how='outer' )
database = pd.merge(database,df_survey, on=['HOLE-ID'], how='outer' )

# grouping all entry by hole id numebr
database_grouped = database.groupby('HOLE-ID')

# writing to disk
database.to_csv(folder+'/drillhole_database.csv')
database_grouped.to_csv(folder+'/drillhole_database_grouped.csv')

