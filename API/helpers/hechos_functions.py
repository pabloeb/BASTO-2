import pandas as pd

#auxiliares

## ========= TEMPORAL ===================
def get_hechos_df():
    return pd.read_csv('../ETL/transformations/tabla_hechos_final.csv')
#========================================


def get_filtered_df_by_day_sett_id(df, day, settlement, deviceId):
    """filtra el dataset por dia, establecimiento y id de dispositivo"""
    sel_by_gps = df[df.UUID == deviceId]
    if sel_by_gps.empty:
        return pd.DataFrame()
    sel_by_settlement = sel_by_gps[sel_by_gps.name == settlement]
    if sel_by_settlement.empty:
        return pd.DataFrame()
    sel_by_day = sel_by_settlement[sel_by_settlement.Fecha == day]
    return sel_by_day

def get_filtered_df_by_day_sett(df,day, settlement):
    """filtra el dataset por dia, establecimiento"""
    sel_by_settlement = df[df.name == settlement]
    if sel_by_settlement.empty:
        return pd.DataFrame()
    sel_by_day = sel_by_settlement[sel_by_settlement.Fecha == day]
    return sel_by_day

def gps_positions_by_day(df, day, settlement, gpsId):
    """devuelve horas y sus respectivas posiciones en un establecimiento durante una fecha"""
    filtered_df = get_filtered_df_by_day_sett_id(df,day, settlement, gpsId)
    if filtered_df.empty:
        return None    
    only_gps = filtered_df[filtered_df.dataRowType == 'GPS']
    hour_and_positions = only_gps[['Hora','Latitud','Longitud']]
    dict_hour_pos = {hour.split('.')[0]: {'lat':lat,'long':long} for (hour,lat,long) in zip(hour_and_positions.Hora,hour_and_positions.Latitud,hour_and_positions.Longitud)}
    return dict_hour_pos

def gps_ids_by_day(df, day, settlement):
    """devuelve los ids de todos los collares sin repeticiones en un establecimiento por fecha"""
    filtered_df = get_filtered_df_by_day_sett(df, day, settlement)
    if filtered_df.empty:
        return None    
    return list(filtered_df.UUID.unique())

#endpoint 1
def get_gps_positions_by_day(day, settlement, gpsId):
    df = get_hechos_df()
    return gps_positions_by_day(df,day, settlement, gpsId)

#endpoint 2
def get_gps_ids_by_day(day, settlement):
    df = get_hechos_df()
    return gps_ids_by_day(df, day, settlement)