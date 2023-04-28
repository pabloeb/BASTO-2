from .conexiones import bson_to_dataframe
import bson
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


def read_ith():
    df_ith = bson_to_dataframe('settlementithcounts.bson')
    return df_ith

def read_settlements():
    df_settlements = bson_to_dataframe('settlements.bson')
    return df_settlements

def get_clean_ith():
    """get ith table and drop nulls"""
    df = read_ith()
    df.dropna(inplace=True)
    return df
    
def merge_settlements_and_ith_tables(df_ith,df_settlements):
    """merge settlements and ith tables to return a specific set of columns"""
    df = df_ith.merge(df_settlements, left_on='settlementId', right_on='_id')
    return df[['ITH','createdAt_x','name']]

def get_clean_settlements():
    """get settlements table and drop unvaluable data"""
    df = read_settlements()
    df = df[df.name.isin(['La Florida','MACSA'])]
    return df

def add_date_and_time_to_ith(df):
    """add date and time columns to table"""
    ith = df[['ITH','createdAt_x','name']]
    ith['timestamp'] = pd.to_datetime(ith.createdAt_x)
    ith['fecha'] = ith.timestamp.apply(lambda x: x.strftime('%Y-%m-%d'))
    ith['hora'] = ith.timestamp.apply(lambda x: x.strftime('%H:00:00'))
    ith.drop(['createdAt_x'], errors='ignore', inplace=True,axis=1)
    return ith

def set_granularity_to_hour(ith):
    """filter only rows with max values by hour and settlement in order to avoid rows with same settlement, day and hour"""
    ith = ith.groupby(['name','fecha','hora']).max()
    ith.reset_index(inplace=True)
    return ith

def add_flags_to_ith(ith):
    """add flags alerta, peligro and more to ith table"""
    ith['alerta'] = ith.ITH.apply(lambda x : 1 if x >= 75 else 0)
    ith['peligro'] = ith.ITH.apply(lambda x : 1 if x >= 79 else 0)
    ith['emergencia'] = ith.ITH.apply(lambda x : 1 if x >= 84 else 0)
    dias_peligro = ith.groupby(['name','fecha']).sum()['peligro']
    dias_peligro = dias_peligro.reset_index()

    # dias_peligro = pd.DataFrame(data={'valores':dias_peligro.values, 'fecha':dias_peligro.index})
    dias_peligro['peligroso'] = dias_peligro.peligro.apply(lambda x : True if x > 1 else False)
    names = dias_peligro.name.unique()
    # import pandas as pd
    dfs = []
    for name in names:
        df = dias_peligro[dias_peligro.name == name]    
        df['cant_peligroso'] = df.peligroso.rolling(3).sum()
        dfs.append(df)
    dias_peligro = pd.concat(dfs)
    

    dias_peligro['ola_calor'] = dias_peligro.cant_peligroso.apply(lambda x : 1 if x > 2 else 0)
    dias_peligro.drop(['createAt_x','peligroso','peligro','cant_peligroso','valores'],axis=1, inplace=True,errors='ignore')

    tabla_ith = ith.merge(dias_peligro,on=['name','fecha'])

    return tabla_ith

def get_ith_with_settlements_names_and_flags():
    """get and merge ith and settlements tables to create a clean resulting table with additional info"""
    df_ith = get_clean_ith()
    df_sett = get_clean_settlements()
    df_merge = merge_settlements_and_ith_tables(df_ith, df_sett)
    df = add_date_and_time_to_ith(df_merge)
    ith = set_granularity_to_hour(df)
    tabla_ith = add_flags_to_ith(ith)
    return tabla_ith





