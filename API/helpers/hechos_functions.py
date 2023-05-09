import pandas as pd
from collections import OrderedDict

#auxiliares

## ========= TEMPORAL ===================
def get_hechos_df():
    return pd.read_csv('../ETL/transformations/tabla_hechos_final.csv')
#========================================


def get_filtered_df_by_day_sett_id(df, day, settlement, deviceId, deviceType):
    """filtra el dataset por dia, establecimiento, tipo de dispositivo y id de dispositivo"""
    if deviceType == 'GPS':
        sel_by_deviceType = df[df.UUID == deviceId]
        sel_by_id = sel_by_deviceType[sel_by_deviceType.dataRowType == 'GPS']
    else:
        sel_by_id = df[df.Mac == deviceId]
    if sel_by_id.empty:
        return pd.DataFrame()
    return get_filtered_df_by_day_sett(sel_by_id,day, settlement)


def get_filtered_df_by_day_sett(df,day, settlement):
    """filtra el dataset por dia, establecimiento"""
    sel_by_settlement = df[df.name == settlement]
    if sel_by_settlement.empty:
        return pd.DataFrame()
    sel_by_day = sel_by_settlement[sel_by_settlement.Fecha == day]
    return sel_by_day


def device_positions_by_day(df, day, settlement, deviceId, deviceType):
    """devuelve horas y sus respectivas posiciones de un dispositivo en un establecimiento durante una fecha"""
    filtered_df = get_filtered_df_by_day_sett_id(df,day, settlement, deviceId, deviceType)
    if filtered_df.empty:
        return None    
    hour_and_positions = filtered_df[['Hora','Latitud','Longitud']]
    dict_hour_pos = {hour.split('.')[0]: {'lat':lat,'long':long} for (hour,lat,long) in zip(hour_and_positions.Hora,hour_and_positions.Latitud,hour_and_positions.Longitud)}
    return OrderedDict(sorted(dict_hour_pos.items()))
   

def gps_positions_by_day(df,day, settlement, gpsId):
    """devuelve horas y sus respectivas posiciones de un collar en un establecimiento durante una fecha"""
    return device_positions_by_day(df,day, settlement, gpsId, 'GPS')


def beacon_positions_by_day(df, day, settlement, beaconId):
    """devuelve horas y sus respectivas posiciones de una caravana en un establecimiento durante una fecha"""
    return device_positions_by_day(df,day, settlement, beaconId, 'BEACON')


def gps_ids_by_day(df, day, settlement):
    """devuelve los ids de todos los collares sin repeticiones en un establecimiento por fecha"""
    filtered_df = get_filtered_df_by_day_sett(df, day, settlement)
    if filtered_df.empty:
        return None    
    return list(filtered_df.UUID.unique())


def beacon_ids_by_day(df, day, settlement):
    """devuelve los ids de todos las caravanas sin repeticiones en un establecimiento por fecha"""
    filtered_df = get_filtered_df_by_day_sett(df, day, settlement)
    if filtered_df.empty:
        return None    
    return list(filtered_df.Mac.dropna().unique())


#endpoint 1
def get_gps_positions_by_day(day, settlement, gpsId):
    df = get_hechos_df()
    return gps_positions_by_day(df,day, settlement, gpsId)

#endpoint 2
def get_gps_ids_by_day(day, settlement):
    df = get_hechos_df()
    return gps_ids_by_day(df, day, settlement)

#endpoint 3
def get_beacon_positions_by_day(day, settlement, beaconId):
    df = get_hechos_df()
    return beacon_positions_by_day(df, day, settlement, beaconId)

#endpoint 4
def get_beacon_ids_by_day(day, settlement):
    df = get_hechos_df()
    return beacon_ids_by_day(df, day, settlement)



