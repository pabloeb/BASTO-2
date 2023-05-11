import pandas as pd
from infrastructure.conexiones import *

from collections import OrderedDict



def filter_df(df, start_date, end_date, settlement):
  """filtra filas del df por establecimiento y rango de fechas"""
  sett_df = df[df.name == settlement]
  if (start_date > end_date) or (sett_df.empty):
    return pd.DataFrame()
  en_rango = sett_df[(sett_df.Fecha >= start_date) & (sett_df.Fecha <= end_date)]
  return en_rango


def distances_by_day(df, start_date, end_date, settlement):
    filtered_df = filter_df(df, start_date, end_date, settlement)
    if filtered_df.empty:
        return None    
    dict_day_dist = {day.split('.')[0]: {'distancia_nocturna':round(noct,2),'distancia_diurna':round(diur,2),'distancia total':round(tot,2)} for (day,noct,diur,tot) in zip(filtered_df.Fecha,filtered_df['distancia nocturna'],filtered_df['distancia diurna'],filtered_df['distancia total'])}
    return OrderedDict(sorted(dict_day_dist.items()))


def get_distances_by_day(start_date, end_date, settlement):
    df = get_daily_distances_df()
    return distances_by_day(df, start_date, end_date, settlement)

    