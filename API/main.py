from fastapi import FastAPI
from helpers.filter_classes import *
from helpers.ith_functions import *
from helpers.hechos_functions import *
from helpers.distancias_functions import *
from helpers.metadata import app
from fastapi import Response

#ENDPOINTS HECHOS

@app.post("/get_gps_positions",tags=["Posiciones de un collar por fecha y establecimiento"],summary='Devuelve horas junto a sus posiciones del collar o null en caso de parametros invalidos')

def get_gpspos(filtro: FiltroDiaEstablecimientoGpsId):
    
    return get_gps_positions_by_day(filtro.date, filtro.settlement, filtro.gpsId)


@app.post("/get_gps_ids_by_day",tags=["Identificadores de collares por fecha y establecimiento"],summary='Devuelve ids de collares por fecha o null en caso de parametros invalidos')

def get_gps_ids_day(filtro: FiltroDiaEstablecimiento):
    
    return get_gps_ids_by_day(filtro.date, filtro.settlement)


@app.post("/get_beacon_positions",tags=["Posiciones de una caravana por fecha y establecimiento"],summary='Devuelve horas junto a sus posiciones de la caravana o null en caso de parametros invalidos')

def get_beacon_pos(filtro: FiltroDiaEstablecimientoBeaconId):
    
    return get_beacon_positions_by_day(filtro.date, filtro.settlement, filtro.beaconId)


@app.post("/get_beacon_ids_by_day",tags=["Identificadores de caravanas por fecha y establecimiento"],summary='Devuelve ids de caravanas por fecha o null en caso de parametros invalidos')

def get_beacon_ids_day(filtro: FiltroDiaEstablecimiento):
    
    return get_beacon_ids_by_day(filtro.date, filtro.settlement)


@app.post("/get_distances_by_day",tags=["Distancias recorrida por el ganado en un establecimiento"], summary='Devuelve distancias recorridas, en metros, por el ganado en un establecimiento o null en caso de parametros invalidos')

def get_distances_day(filtro: FiltroFechasEstablecimiento):
    
    return get_distances_by_day(filtro.start_date, filtro.end_date, filtro.settlement)


@app.post("/get_individual_gps_distances_by_day",tags=["Distancias recorridas por un collar en un establecimiento"], summary='Devuelve distancias recorridas, en metros, de un collar en un establecimiento o null en caso de parametros invalidos')

def get_gps_individual_distances_day(filtro: FiltroDiaEstablecimientoGpsId):
    
    return get_individual_gps_distances_by_day(filtro.date, filtro.settlement, filtro.gpsId)

#ENDPOINTS ITH

@app.post("/get_ec",tags=["Cantidad de horas de estress calorico en establecimiento"],summary='Devuelve total horas de estress calorico o null en caso de parametros invalidos')

def get_ec(filtro: FiltroFechasEstablecimiento):
    
    horas = get_ec_hours(filtro.start_date, filtro.end_date, filtro.settlement)
    if horas:
        return {'horas_EC':horas}
    return horas


@app.post("/get_mean_ith",tags=["ITH promedio por hora en establecimiento"],summary='Devuelve horas del dia junto a su ith promedio o null en caso de parametros invalidos')

def get_mean_ith_inrange(filtro: FiltroFechasEstablecimiento):

    return get_mean_ith(filtro.start_date, filtro.end_date, filtro.settlement)
    

@app.post("/get_heat_wave_days",tags=["Cantidad de dias de ola de calor en establecimiento"],summary='Devuelve cantidad de dias de ola de calor o null en caso de parametros invalidos')

def get_heat_wave_d(filtro: FiltroFechasEstablecimiento):

    dias = get_heat_wave_days(filtro.start_date, filtro.end_date, filtro.settlement)
    if dias:
        return {'dias_oc': dias}
    return dias


@app.post("/get_ec_by_day",tags=["Horas de EC por dia en establecimiento"],summary='Devuelve dias junto a su cantidad de horas de EC o null en caso de parametros invalidos')

def get_ec_by_d(filtro: FiltroFechasEstablecimiento):

    return get_ec_count_by_day_in_period(filtro.start_date, filtro.end_date, filtro.settlement)



