# MODULO DE CONEXIONES A LA BASE

import pandas as pd
import os
from pymongo import MongoClient # instalar pymongo

def read_mongo(collection, query={}):
    """ Make a query to the specific DB and Collection and get a dataframe"""

     #es necesario python 3.6 o mayor 
    mongo_uri = 'mongodb+srv://rikigerman:Q34UGooQa74zviWb@cluster1.m0ifpk2.mongodb.net/?retryWrites=true&w=majority'
    conn = MongoClient(mongo_uri)
    db = conn['test']
    cursor = db[collection].find(query)
    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))
    df.index = df['_id'].apply(lambda x: str(x))
    df.drop('_id',errors='ignore',inplace=True, axis=1)
    df.index.name = None   
    conn.close()
    return df   # Read from Mongo and Store into DataFrame 
 
#def save_tranformation(df, name):
#    """ save df to transformations folder with name assigned"""
#    df.to_csv(f'transformations/{name}.csv',index=False)

def save_tranformation(df, name):
    """ save df to transformations folder with name assigned"""
    # Verifica si la carpeta transformations existe
    if not os.path.exists('transformations'):
        # Si no existe, crea la carpeta
        os.makedirs('transformations')
        
    # Guarda el archivo en la carpeta transformations
    df.to_csv(f'transformations/{name}.csv', index=False)