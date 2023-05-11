import pandas as pd
from infrastructure.conexiones import *

from collections import OrderedDict


# auxiliares

def filter_df(df, start_date, end_date, settlement):
  """filtra filas del df por establecimiento y rango de fechas"""
  sett_df = df[df.name == settlement]
  if (start_date > end_date) or (sett_df.empty):
    return pd.DataFrame()
  en_rango = sett_df[(sett_df.Fecha >= start_date) & (sett_df.Fecha <= end_date)]
  return en_rango

def get_filtered_df_by_day_sett(df,day, settlement):
    """filtra el dataset por dia, establecimiento"""
    sel_by_settlement = df[df.name == settlement]
    if sel_by_settlement.empty:
        return pd.DataFrame()
    sel_by_day = sel_by_settlement[sel_by_settlement.Fecha == day]
    return sel_by_day


def get_filtered_df_by_day_sett_id(df, day, settlement, deviceId):
    """filtra el dataset por dia, establecimiento, tipo de dispositivo y id de dispositivo"""
    sel_by_id = df[df.UUID == deviceId]
    if sel_by_id.empty:
        return pd.DataFrame()
    return get_filtered_df_by_day_sett(sel_by_id,day, settlement)


def distances_by_day(df, start_date, end_date, settlement):
    filtered_df = filter_df(df, start_date, end_date, settlement)
    if filtered_df.empty:
        return None    
    dict_day_dist = {day.split('.')[0]: {'distancia_nocturna':round(noct,2),'distancia_diurna':round(diur,2),'distancia total':round(tot,2)} for (day,noct,diur,tot) in zip(filtered_df.Fecha,filtered_df['distancia nocturna'],filtered_df['distancia diurna'],filtered_df['distancia total'])}
    return OrderedDict(sorted(dict_day_dist.items()))

def individual_gps_distances_by_day(df, date, settlement, gpsId):
  filtered_df = get_filtered_df_by_day_sett_id(df, date , settlement, gpsId)
  if filtered_df.empty:
      return None    
  return {'distancia nocturna': round(filtered_df['distancia nocturna'].values[0],2), 'distancia diurna': round(filtered_df['distancia diurna'].values[0],2),'distancia total':round(filtered_df['distancia total'].values[0],2)}


#endpoint 1
def get_distances_by_day(start_date, end_date, settlement):
    df = get_daily_distances_df()
    return distances_by_day(df, start_date, end_date, settlement)

#endpoint 2
def get_individual_gps_distances_by_day(date, settlement, gpsId):
   df = get_recorrido_diario_df()
   return individual_gps_distances_by_day(df, date, settlement, gpsId)