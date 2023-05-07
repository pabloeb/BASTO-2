import pandas as pd
import numpy as np


# AUXILIARES


# ================================== TEMPORAL =====================================
def get_ith():
    """obtiene dataframe de transformaciones de dataset ith"""
    return pd.read_csv('../ETL/transformations/tabla_ith.csv.csv')
# ==============================================================================


def filter_df(df, start_date, end_date, settlement):
  """filtra filas del df por establecimiento y rango de fechas"""
  sett_df = df[df.name == settlement]
  if (start_date > end_date) or (sett_df.empty):
    return pd.DataFrame()
  en_rango = sett_df[(sett_df.fecha >= start_date) & (sett_df.fecha <= end_date)]
  return en_rango

def EC_hours(df, start_date, end_date, settlement):
  """
  dado un dataframe, devuelve horas de estress calorico en establecimiento para un periodo de tiempo
  """
  en_rango = filter_df(df, start_date, end_date, settlement)
  if en_rango.empty:
    return None
  res  = en_rango.alerta.sum()
  return int(res)

def mean_ith(df, start_date, end_date, settlement):
  """devuelve ith promedio para cada hora del dia de un establecimiento en un rango de fechas"""
  en_rango = filter_df(df, start_date, end_date, settlement)
  if en_rango.empty:
    return None
  mean_ith = en_rango.groupby('hora')[['ITH']].mean()
  mean_ith.index = [c[:-2].rstrip(':') for c in mean_ith.index.values]
  res = mean_ith.to_dict()['ITH']
  return res
  
def heat_wave_days(df, start_date, end_date, settlement):
  """devuelve dias de ola de calor de un establecimiento en un rango de fechas"""
  en_rango = filter_df(df, start_date, end_date, settlement)
  if en_rango.empty:
    return None
  dias_ola = en_rango.groupby('fecha')[['ola_calor']].max()
  res = dias_ola.values.sum()
  return int(res)

def ec_count_by_day_in_period(df, start_date, end_date, settlement):
  """devuelve dias junto a su cantidas de horas EC"""
  en_rango = filter_df(df, start_date, end_date, settlement)
  if en_rango.empty:
    return None
  ec_x_dia = en_rango.groupby('fecha')[['alerta']].sum()
  res = ec_x_dia.to_dict()['alerta']
  return res 

# endpoint 1
def get_ec_hours(start_date, end_date, settlement):
  df = get_ith()
  return EC_hours(df,start_date,end_date,settlement)

# endpoint 2
def get_mean_ith(start_date, end_date, settlement):
  df = get_ith()
  return mean_ith(df, start_date, end_date, settlement)

#endpoint 3
def get_heat_wave_days(start_date, end_date, settlement):
  df = get_ith()
  return heat_wave_days(df, start_date, end_date, settlement)

#endpoint 4
def get_ec_count_by_day_in_period(start_date, end_date, settlement):
  df = get_ith()
  return ec_count_by_day_in_period(df, start_date, end_date, settlement)