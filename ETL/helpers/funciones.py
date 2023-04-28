import pandas as pd
import numpy as np
import re
import math
import random
from datetime import datetime, timedelta
import folium
from folium.plugins import HeatMap
from geopy.distance import geodesic             # cálculo de distancia entre coordenadas
from geopy.distance import distance



# ----------->> COMIENZA CODIGO PARA 'df_general' <<-----------

def base_gps(df):
    
    # Reemplazo los NaN con la cadena "Sin datos"
    df["dataRowType"] = df["dataRowType"].fillna("Sin datos")

    # Filtro las filas con "GPS" en la columna dataRowType
    df_gps = df[df["dataRowType"].str.contains("GPS")]

    # Elimino columnas no utiles
    df_gps = df_gps.drop(['_id', "updatedAt", "__v", "payload"], axis=1)
    
    # Agrego dos nuevas columnas a df_gps: "Fecha" y "Hora" con el desglose de la columna createdAt
    df_gps[["Fecha", "Hora"]] = df_gps["createdAt"].apply(lambda x: pd.Series([x.strftime("%Y-%m-%d"), x.strftime("%H:%M:%S")]))

    # Paso "Fecha" a formato datetime.
    # La "Hora" queda con formato object, porque para que quede como datetime deberia quedar junto con la fecha, y no separada como esta
    df_gps["Fecha"] = pd.to_datetime(df_gps["Fecha"], format="%Y-%m-%d")   #, errors="coerce")
    df_gps["Hora"] = pd.to_datetime(df_gps["Hora"], format="%H:%M:%S").dt.time
    
    # Creo las columnas "Latitud" y "Longitud" y les asigno los datos segun la columna "dataRowData"
    df_gps["Latitud"] = df_gps["dataRowData"].apply(lambda x: x["lat"])
    df_gps["Longitud"] = df_gps["dataRowData"].apply(lambda x: x["lng"])

    # Elimino las filas que tengan Latitud o Longitud con NaN
    df_gps.dropna(subset=["Latitud", "Longitud"], inplace=True)
    
    # Creo las columnas "gpsAlt", "gpsVel" y les asigno los datos segun la columna "dataRowData"
    df_gps['gpsAlt'] = df_gps['dataRowData'].apply(lambda x: x['gpsAlt'])
    df_gps['gpsVel'] = df_gps['dataRowData'].apply(lambda x: x['gpsVel'])
    
    # Cambio el nombre de la columna "createdAt" a "Datetime" (la dejo en la tabla por si necesitamos la Hora en formato datetime)
    df_gps = df_gps.rename(columns={"createdAt": "Datetime"})

    # Reordeno las columnas
    df_gps = df_gps.reindex(columns=['Fecha', 'Hora', 'Datetime', 'UUID', 'Latitud', 'Longitud', 'gpsAlt', 'gpsVel', 'dataRowType', 'dataRowData'])

    # Reseteo el index
    df_gps = df_gps.reset_index(drop=True)
    
    return df_gps


def base_beacon(df):
    
    # Reemplazo los NaN con la cadena "Sin datos"
    df["dataRowType"] = df["dataRowType"].fillna("Sin datos")

    # Filtro las filas con "BEACON" en la columna dataRowType
    df_beacon = df[df["dataRowType"].str.contains("BEACON")]

    # Elimino columnas no utiles
    df_beacon = df_beacon.drop(['_id', "updatedAt", "__v", "payload"], axis=1)

    # Agrego dos nuevas columnas a df_beacon: "Fecha" y "Hora" con el desglose de la columna createdAt
    df_beacon[["Fecha", "Hora"]] = df_beacon["createdAt"].apply(lambda x: pd.Series([x.strftime("%Y-%m-%d"), x.strftime("%H:%M:%S")]))

    # Paso "Fecha" a formato datetime.
    # La "Hora" queda con formato object, porque para que quede como datetime deberia quedar junto con la fecha, y no separada como esta
    df_beacon["Fecha"] = pd.to_datetime(df_beacon["Fecha"], format="%Y-%m-%d")
    df_beacon["Hora"] = pd.to_datetime(df_beacon["Hora"], format="%H:%M:%S").dt.time

    # Creo las columnas "Mac", "Battery", "Temperature" y "RSSI" y les asigno los datos segun la columna "dataRowData"
    df_beacon['Mac'] = df_beacon['dataRowData'].apply(lambda x: x['mac'])
    df_beacon['Battery'] = df_beacon['dataRowData'].apply(lambda x: x['battery'])
    df_beacon['Temperature'] = df_beacon['dataRowData'].apply(lambda x: x['temperature'])
    df_beacon['RSSI'] = df_beacon['dataRowData'].apply(lambda x: x['rssi'])

    # Cambio el nombre de la columna "createdAt" a "Datetime" (la dejo en la tabla por si necesitamos la Hora en formato datetime)
    df_beacon = df_beacon.rename(columns={"createdAt": "Datetime"})

    # Reordeno las columnas
    df_beacon = df_beacon.reindex(columns=['Fecha', 'Hora', 'Datetime', "UUID", "Mac", "Battery", "Temperature", "RSSI", "dataRowType", "dataRowData"])

    # Reseteo el index
    df_beacon = df_beacon.reset_index(drop=True)
    
    return df_beacon


def base_battery(df):
    
    # Reemplazo los NaN con la cadena "Sin datos"
    df["dataRowType"] = df["dataRowType"].fillna("Sin datos")

    # Filtro las filas con "BATTERY" en la columna dataRowType
    df_battery = df[df["dataRowType"].str.contains("BATTERY")]

    # Elimino columnas no utiles
    df_battery = df_battery.drop(['_id', "updatedAt", "__v", "payload"], axis=1)

    # Agrego dos nuevas columnas a df_battery: "Fecha" y "Hora" con el desglose de la columna createdAt
    df_battery[["Fecha", "Hora"]] = df_battery["createdAt"].apply(lambda x: pd.Series([x.strftime("%Y-%m-%d"), x.strftime("%H:%M:%S")]))

    # Paso "Fecha" a formato datetime.
    # La "Hora" queda con formato object, porque para que quede como datetime deberia quedar junto con la fecha, y no separada como esta
    df_battery["Fecha"] = pd.to_datetime(df_battery["Fecha"], format="%Y-%m-%d")
    df_battery["Hora"] = pd.to_datetime(df_battery["Hora"], format="%H:%M:%S").dt.time

    # Creo las columnas "Voltage", "Battery", "Charge" y les asigno los datos segun la columna "dataRowData"
    df_battery['Voltage'] = df_battery['dataRowData'].apply(lambda x: x['voltage'])
    df_battery['Battery'] = df_battery['dataRowData'].apply(lambda x: x['battery'])
    df_battery['Charge'] = df_battery['dataRowData'].apply(lambda x: x['charge'])

    # Cambio el nombre de la columna "createdAt" a "Datetime" (la dejo en la tabla por si necesitamos la Hora en formato datetime)
    df_battery = df_battery.rename(columns={"createdAt": "Datetime"})

    # Reordeno las columnas
    df_battery = df_battery.reindex(columns=['Fecha', 'Hora', 'Datetime', "UUID", "Voltage", "Battery", "Charge", "dataRowType", "dataRowData"])

    # Reseteo el index
    df_battery = df_battery.reset_index(drop=True)
    
    return df_battery


def base_general(df1, df2, df3):
    
    # Armo la base general
    df_general = pd.concat([df1, df2, df3])

    # Eliminar UUIDs que identificamos con latitud y longitud erroneos
    df_general = df_general[~df_general['UUID'].isin(['0004A30B00F7FC52', '0004A30B00F7FAC0', '0004A30B00F7927C', '0004A30B00F8293E', '0004A30B00F86B3D', '0004A30B00F862D9', '0004A30B00F89E08', '0004A30B00F868C7'])]

    # Ordenar por "Fecha" y "Hora"
    df_general = df_general.sort_values(by=['Fecha', 'Hora'])

    # Reordenar las columnas
    df_general = df_general[['Fecha', 'Hora', 'Datetime', 'dataRowType', 'UUID', 'Latitud', 'Longitud', 'Mac', 'Battery', 'Temperature', 'RSSI', 'Voltage', 'Charge', 'gpsAlt', 'gpsVel', 'dataRowData']]

    # Reiniciar los indices
    df_general = df_general.reset_index(drop=True)
    
    return df_general    
    


# ----------->> TERMINA CODIGO POR 'df_general' <<-----------



# ----------->> COMIENZA CODIGO PARA 'df_plots2' <<-----------


def base_plots2(animals, devices, settlements):
    
    df_animals2 = animals.merge(devices, left_on='_id', right_on='deviceAnimalID')

    # Cambio nombres _id_x a _id_animals y _id_y a _id_devices
    df_animals2 = df_animals2.rename(columns={'_id_x': '_id_animals', '_id_y': '_id_devices'})

    # Elimino columnas birthDay, dateOfBirth, observations, __v_x, animalSenasa, __v_y
    df_animals2 = df_animals2.drop(['birthDay', 'dateOfBirth', 'observations', '__v_x', 'animalSenasa', '__v_y'], axis=1)

    # Extraigo el contenido de la columna 'animalSettlement' para crear 'animalSettlement_new'
    df_animals2['animalSettlement_new'] = df_animals2['animalSettlement'].apply(lambda x: re.findall(r"'([a-f0-9]{24})'", str(x))[0])

    # Reubico la columna en el df
    animalSettlement_new = df_animals2.pop('animalSettlement_new')
    df_animals2.insert(2, 'animalSettlement_new', animalSettlement_new)

    # Armo df_plots2 con las coincidencias de la columna 'animalSettlement_new' del df_animals2 
    # con la columna '_id' del df_setllements

    # Paso las columnas a comparar a string
    df_animals2['animalSettlement_new'] = df_animals2['animalSettlement_new'].astype(str)
    settlements['_id'] = settlements['_id'].astype(str)

    # Creo la base con las coincidencias
    df_plots2 = pd.merge(df_animals2, settlements, left_on='animalSettlement_new', right_on='_id')

    # Cambio columna _id a _id_settlements
    df_plots2 = df_plots2.rename(columns={'_id': '_id_settlements'})

    # Elimino la columna __v
    df_plots2 = df_plots2.drop('__v', axis=1)
    
    return df_plots2



# ----------->> TERMINA CODIGO POR 'df_plots2' <<-----------



# ----------->> COMIENZA CODIGO PARA 'tabla_hechos_final' <<-----------

def tablahechos_inicial(df_general, df_plots2):

    # Lee el archivo parquet
    # df_general = pd.read_parquet('./tablas/df_general.parquet')
    
    # Cargo la base (join de varias tablas originales)
    # df_plots2 = pd.read_csv("./tablas/df_plots2.csv")

    # Join de ambas tablas 
    tablahechos_ini = df_general.merge(df_plots2,left_on = "UUID", right_on ="deviceMACAddress")
    
    #tablahechos_ini = tablahechos_ini.drop(columns = "_id", axis=1) 

    # Se pasa la columna "name" a la posición 8
    nombre_columna = tablahechos_ini.pop("name")
    tablahechos_ini.insert(8, "name", nombre_columna)
    
    # Se pasa la columna "RSSI" a la posición 9
    nombre_columna = tablahechos_ini.pop("RSSI")
    tablahechos_ini.insert(9, "RSSI", nombre_columna)

    # Se filtra hasta la columna 10
    tablahechos_ini = tablahechos_ini.iloc[ : , :10]

    # Se filtra el campo MACSA por fecha para obtener un Dataframe que va desde el 24/02/2023 al 08/03/2023
    tablahechos_ini_filtrado = tablahechos_ini[(tablahechos_ini["Fecha"] > "2023-02-23") & (tablahechos_ini["Fecha"] < "2023-03-09") & (tablahechos_ini["name"]=="MACSA" )]

    # Se filtra para conservar solo las categorias GPS y BEACON del campo dataRowType
    tablahechos_ini_filtrado = tablahechos_ini_filtrado[tablahechos_ini_filtrado["dataRowType"] != "BATTERY"]
    
    # Muy importante ordenar para que funcione el código posterior:
    tablahechos_ini_filtrado = tablahechos_ini_filtrado.sort_values(['dataRowType',"Mac",'Fecha'], ascending=[True, True, True])
    tablahechos_ini_filtrado1 = tablahechos_ini_filtrado.reset_index().drop(columns =["index"])

    return tablahechos_ini_filtrado1


# funcion auxiliar para obtener fechas gps asociado
def get_gps_prevdate(df, uuid, fecha):
    """dado uuid y fecha trae todos los gps de df con ese uuid y previos a esa fecha"""
    gps_prev = df[(df.UUID == uuid) & (df.Fecha <= fecha) & (df.Fecha >= (pd.to_datetime(fecha) + pd.offsets.Day(-5)).strftime("%Y-%m-%d")) & (df.dataRowType == 'GPS')]
    if (len(gps_prev) > 0): 
      return gps_prev
    return df[(df.UUID == uuid) & (df.Fecha <= fecha) & (df.dataRowType == 'GPS')]


# funcion para obtener latitud y longitud gps asociado a beacon
def get_closest_gpspos(beacon, df):
    """dado beacon y df retorna posicion de su gps mas cercano"""
    test_date = pd.to_datetime(beacon.Datetime)
    gps_prev = get_gps_prevdate(df, beacon.UUID, beacon.Fecha)
    if (len(gps_prev) > 0):
        gps_prev['diff_frombeacon'] = gps_prev.Datetime.apply(lambda x : abs(test_date.timestamp() - pd.to_datetime(x).timestamp()))
        mindiff = min(gps_prev.diff_frombeacon)
        res = gps_prev[gps_prev.diff_frombeacon == mindiff]
        if (res.Latitud.any() and res.Longitud.any()):
            return (res.Latitud.values[0], res.Longitud.values[0])
    return (None, None)


# funcion que completa para cada beacon las posiciones de sus gps en una nueva columna
def fill_beacon_gps_pos(df):
    """dado df genera una columna con posicion de gps asociado a cada beacon"""
    df['position_gps_assoc'] = df.apply(lambda row: get_closest_gpspos(row, df) if row['dataRowType'] == 'BEACON' else None, axis=1)
    return df


""" 
Agrega una columna distancia_virtual en metros al dataframe tablahechos_ini_filtrado1, que es la distancia virtual de un beacon al GPS que lo reportó.
Desde aquí se puede corregir la distancia aleatoria del Beacon al GPS en función de la fórmula que involucra al RSSI.
"""
def distancia_virtual(df):
    distancias = []
    for index, row in df.iterrows():
        if row['position_gps_assoc'] is not None:
            distancia = 10 + (-0.4) * row['RSSI']      #<--------------------------- Establece la distancia aleatoria del GPS al BEACON
            distancias.append(distancia)
        else:
            distancias.append(None)
    df.insert(loc=10, column='distancia_virtual', value=distancias)
    return df


# Función para separar la columna 'position_gps_assoc' que es una tupla de latitud y longitud, en dos nuevas columnas diferentes y agregarlas al DF(Latitud-GPS, Longitud_GPS)
# Función para separar la tupla de la columna "position_gps_assoc" en dos columnas
def dividir_gps_position(row):
    if row['position_gps_assoc'] is None:
        return pd.Series({'Latitud_GPS': None, 'Longitud_GPS': None})
    else:
        lat, lon = row['position_gps_assoc']
        return pd.Series({'Latitud_GPS': lat, 'Longitud_GPS': lon})


# Sub-función de la función 'move_point_along_radius'. Genera un punto aleatorio sobre un circulo de radio 1m alrededor de un centro de coordenadas (lat,lon GPS asociado)

def random_point_on_circle(center_lat, center_lon):
    # Radio del círculo en metros
    radius = 1.0
    
    # Generar un ángulo aleatorio en radianes
    random_angle = random.uniform(0, 2*math.pi)
    
    # Calcular las coordenadas del punto aleatorio en latitud y longitud
    lat = math.degrees(math.asin(math.sin(math.radians(center_lat)) * math.cos(radius/6371000) +
                                  math.cos(math.radians(center_lat)) * math.sin(radius/6371000) * math.cos(random_angle)))
    
    lon = math.degrees(math.radians(center_lon) + math.atan2(math.sin(random_angle) * math.sin(radius/6371000) * math.cos(math.radians(center_lat)),
                                  math.cos(radius/6371000) - math.sin(math.radians(center_lat)) * math.sin(math.radians(lat))))
    
    return lat, lon

# Función cálculo de las coordenadas virtuales de los BEACON en función de la posición del GPS y del RSSI:
def move_point_along_radius(center_lat, center_lon, distance):
    # Obtener un punto aleatorio sobre un círculo de radio un metro
    point_lat, point_lon = random_point_on_circle(center_lat, center_lon)
    
    # Calcular la dirección del radio en radianes
    center_lat_rad, center_lon_rad = math.radians(center_lat), math.radians(center_lon)
    point_lat_rad, point_lon_rad = math.radians(point_lat), math.radians(point_lon)
    direction = math.atan2(math.sin(point_lon_rad - center_lon_rad) * math.cos(point_lat_rad),
                              math.cos(center_lat_rad) * math.sin(point_lat_rad) -
                              math.sin(center_lat_rad) * math.cos(point_lat_rad) *
                              math.cos(point_lon_rad - center_lon_rad))
    
    # Calcular las nuevas coordenadas a lo largo del radio
    new_lat = math.degrees(math.asin(math.sin(center_lat_rad) * math.cos(distance/6371000) +
                                          math.cos(center_lat_rad) * math.sin(distance/6371000) * math.cos(direction)))
    new_lon = math.degrees(center_lon_rad + math.atan2(math.sin(direction) * math.sin(distance/6371000) * math.cos(center_lat_rad),
                                          math.cos(distance/6371000) - math.sin(center_lat_rad) * math.sin(math.radians(new_lat))))
    
    return new_lat, new_lon

def coord_virtuales(tablahechos_ini_filtrado1):
    # Recorrer el dataframe
    for i, row in tablahechos_ini_filtrado1.iterrows():
        # Sólo modificar lat y long virtuales en los BEACON 
        if row["dataRowType"]=="BEACON" :
            # Obtener las coordenadas del centro y la distancia virtual
            center_lat = row["Latitud_GPS"]
            center_lon = row["Longitud_GPS"]
            distance = row["distancia_virtual"]

            # Calcular las nuevas coordenadas virtuales
            new_lat, new_lon = move_point_along_radius(center_lat, center_lon, distance)
            
            # Actualizar las columnas de Latitud y Longitud
            tablahechos_ini_filtrado1.at[i, "Latitud"] = new_lat
            tablahechos_ini_filtrado1.at[i, "Longitud"] = new_lon

    return tablahechos_ini_filtrado1


# Elimina las columnas finales de un DataFrame desde la columna "numero_columna" hasta la última:
def eliminacion_columnas_finales(df,numero_columna):
    df = df.iloc[ : , 0 : numero_columna]
    return df


""" En el siguiente código, la función 'interpolate_points' calcula  puntos virtuales con coordenadas de latitud y longitud sobre una recta definida por dos mediciones consecutivas de un mismo dispositivo BEACON en un intérvalo de tiempo seleccionado a través de la variable 'intervalo'"""
# Función de interpolación lineal
def interpolate_points(p1, p2):
    intervalo = 30              # <---------------------------- La variable intervalo controla el intervalo entre puntos virtuales (en minutos)

    # Calculamos la diferencia de tiempo en minutos
    delta_t = (p2['datetime'] - p1['datetime']).total_seconds() / 60.0

    # Cuando el intervalo entre 2 mediciones es menor al intervalo seleccionado para generar los puntos vituales, la función no devuelve nada
    # El código a continuación fuerza esa circunstancia en el caso que :
    # - delta_t sea nula (dos mediciones consecutivas del mismo device en el mismo momento = duplicado ==> no genera resultado y sigue iterando),
    # - delta_t sea mayor al tiempo máximo estipulado para generar los puntos virtuales o que sean de dias diferentes.
    
    if delta_t == 0 or (p1['datetime'].date() != p2['datetime'].date()):
        intervalo = intervalo -1
        delta_t = 1


    # Convertimos las coordenadas en radianes
    lat1, lon1 = map(math.radians, [p1['lat'], p1['lon']])
    lat2, lon2 = map(math.radians, [p2['lat'], p2['lon']])


    # Calculamos la distancia entre los dos puntos
    d = 2 * math.asin(math.sqrt(math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2)) * 6371  # radio de la Tierra en km
    
    # Calculamos la velocidad promedio entre los dos puntos
    speed = d / delta_t

    # Calculamos los puntos intermedios. Se fijan los minutos de intervalo deseado con la variable "intervalo":

    num_points = int(delta_t / intervalo)     
    points = []
    for i in range(num_points):
        frac = (i + 1) / (num_points + 1)
        lat = math.degrees(lat1 + frac * (lat2 - lat1))
        lon = math.degrees(lon1 + frac * (lon2 - lon1))
        time = p1['datetime'] + timedelta(minutes=(i + 1) * intervalo)   
        points.append({'lat': lat, 'lon': lon, 'datetime': time})
    return points


""" Esta función es llamada por la función "tabla_BEACONvir" En el siguiente código, la función 'interpolate_points' calcula puntos virtuales con coordenadas de latitud y longitud sobre una recta definida por dos mediciones consecutivas de un mismo dispositivo BEACON en un intérvalo de tiempo seleccionado a través de la variable 'intervalo'"""
# Función de interpolación lineal
def interpolate_points(p1, p2):
    intervalo = 30              # <---------------------------- La variable intervalo controla el intervalo entre puntos virtuales (en minutos)

     # Calculamos la diferencia de tiempo en minutos
    delta_t = (p2['datetime'] - p1['datetime']).total_seconds() / 60.0

    # Cuando el intervalo entre 2 mediciones es menor al intervalo seleccionado para generar los puntos vituales, la función no devuelve nada
    # El código a continuación fueza esa circunstancia en el caso que delta_t sea nula (dos mediciones consecutivas del mismo device en el mismo momento = duplicados ==> no genera resultado y sigue iterando), o que delta_t sea mayor al tiempo máximo estipulado para generar los puntos virtuales, o que sean de dias diferentes.

    if delta_t == 0 or (p1['datetime'].date() != p2['datetime'].date()):
        intervalo = intervalo - 1
        delta_t = 1


    # Convertimos las coordenadas en radianes
    lat1, lon1 = map(math.radians, [p1['lat'], p1['lon']])
    lat2, lon2 = map(math.radians, [p2['lat'], p2['lon']])


    # Calculamos la distancia entre los dos puntos
    d = 2 * math.asin(math.sqrt(math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2)) * 6371  # radio de la Tierra en km
    
    # Calculamos la velocidad promedio entre los dos puntos
    speed = d / delta_t

    # Calculamos los puntos intermedios.Se fijan los minutos de intervalo deseado con la variable "intervalo":

    num_points = int(delta_t / intervalo)     
    points = []
    for i in range(num_points):
        frac = (i + 1) / (num_points + 1)
        lat = math.degrees(lat1 + frac * (lat2 - lat1))
        lon = math.degrees(lon1 + frac * (lon2 - lon1))
        time = p1['datetime'] + timedelta(minutes=(i + 1) * intervalo)   
        points.append({'lat': lat, 'lon': lon, 'datetime': time})
    return points


"""
Esta función itera el dataframe tablahechos_BEACON_aleatorios, y cuando encuentra dos BEACON consecutivos con igual MAC arma un diccionario con los valores de latitud, longitud y datetime de cada medición del Mac y los envía a la función "interpolate_points2" que evalua si hay que generar nuevos puntos interpolados entre las mediciones. Este código devuelve un dataframe sólo de los nuevos puntos interpolados.
"""
def tabla_BEACONvir(tablahechos_BEACON_aleatorios):   
    
    resultados = []

    # Iterar a través de las filas del DataFrame
    for m in range(len(tablahechos_BEACON_aleatorios)-1):
        # Comparar filas consecutivas solo si ambas tienen dataRowType = 'BEACON'
        if (tablahechos_BEACON_aleatorios.loc[m, 'dataRowType'] == 'BEACON') and (tablahechos_BEACON_aleatorios.loc[m+1, 'dataRowType'] == 'BEACON'):
            # Verificar si los valores de la columna 'Mac' son iguales
            if tablahechos_BEACON_aleatorios.loc[m, 'Mac'] == tablahechos_BEACON_aleatorios.loc[m+1, 'Mac']:
                # Si son iguales, crear un diccionario para cada fila con las claves 'lat', 'lon' y 'datetime' y los valores correspondientes
                diccionario1 = {'lat': tablahechos_BEACON_aleatorios.loc[m, 'Latitud'], 'lon': tablahechos_BEACON_aleatorios.loc[m, 'Longitud'], 'datetime': tablahechos_BEACON_aleatorios.loc[m, 'Datetime'] }
                diccionario2 = {'lat': tablahechos_BEACON_aleatorios.loc[m+1, 'Latitud'], 'lon': tablahechos_BEACON_aleatorios.loc[m+1, 'Longitud'], 'datetime': tablahechos_BEACON_aleatorios.loc[m+1, 'Datetime']}
                
                #Colocar los diccionarios resultantes de las dos mediciones de Mac consecutivas en la función para calcular los puntos intermedios entre ellas 
                data = [diccionario1, diccionario2]
                df = pd.DataFrame(data)
                df['datetime'] = pd.to_datetime(df['datetime'])
                interpolated_points = []
                for i in range(len(df) - 1):
                    p1, p2 = df.iloc[i], df.iloc[i + 1]
                    points = interpolate_points(p1, p2)
                    interpolated_points.extend(points)
                    resultado = pd.DataFrame(interpolated_points)
                    
                    #Se agregan las otras columnas necesarias al dtaframe resultado     #<-------- Se puede agregar otras columnas a la tabla
                    resultado["dataRowType"] = tablahechos_BEACON_aleatorios.loc[m, 'dataRowType']
                    resultado["Mac"] = tablahechos_BEACON_aleatorios.loc[m, 'Mac']
                    resultado["name"] = tablahechos_BEACON_aleatorios.loc[m, 'name']
                    resultado["UUID"] = tablahechos_BEACON_aleatorios.loc[m, 'UUID']
                    resultado["RSSI"] = tablahechos_BEACON_aleatorios.loc[m, 'RSSI']

                    #Se acumulan las filas
                    resultados.append(resultado)
                                
    # Concatenar todos los DataFrames en resultados en un solo DataFrame
    if len(resultados) > 0:
        resultado_final_BEACONVIR = pd.concat(resultados)
    else:
        resultado_final_BEACONVIR  = pd.DataFrame()

    resultado_final_BEACONVIR = resultado_final_BEACONVIR.rename(columns={'lat': 'Latitud', 'lon': 'Longitud', 'datetime': 'Datetime'})

    # Generar las columnas Fecha y Hora a partir de Datetime:
    resultado_final_BEACONVIR['Datetime'] = pd.to_datetime(resultado_final_BEACONVIR['Datetime'])

    # Creamos las columnas Fecha y Hora
    resultado_final_BEACONVIR['Fecha'] = resultado_final_BEACONVIR['Datetime'].dt.date
    #resultado_final_BEACONVIR['Hora'] = resultado_final_BEACONVIR['Datetime'].dt.time   #<---- CUIDADO: No usar este código. En el merge con tablahechos_BEACON_aleatorios revisar que no haya conflicto con el tipo de dato (object/float)
    resultado_final_BEACONVIR['Hora'] = resultado_final_BEACONVIR['Datetime'].dt.strftime('%H:%M:%S')

    #Ordeno las columnas para poder concatenar con la tabla tablahechos_BEACON_aleatorios
    resultado_final_BEACONVIR = resultado_final_BEACONVIR[["Fecha", "Hora", "Datetime", "dataRowType", "UUID", "Latitud", "Longitud", "Mac", "name", "RSSI"]]

    return resultado_final_BEACONVIR 


"""
Esta función itera el dataframe df_tablahechos_parcial, y cuando encuentra dos GPS consecutivos con igual UUID arma un par de diccionarios con los valores de latitud, longitud y datetime de cada medición del UUID y los envía a la función "interpolate_points", que evalua si hay que generar nuevos puntos interpolados entre las mediciones. Este código devuelve un dataframe sólo de los nuevos puntos UUID interpolados.
"""
def tabla_UUIDvir(df_tablahechos_parcial):   
    
    resultados = []

    # Iterar a través de las filas del DataFrame
    for m in range(len(df_tablahechos_parcial)-1):
        # Comparar filas consecutivas solo si ambas tienen dataRowType = 'GPS'
        if (df_tablahechos_parcial.loc[m, 'dataRowType'] == 'GPS') and (df_tablahechos_parcial.loc[m+1, 'dataRowType'] == 'GPS'):
            # Verificar si los valores de la columna 'UUID' son iguales
            if df_tablahechos_parcial.loc[m, 'UUID'] == df_tablahechos_parcial.loc[m+1, 'UUID']:
                # Si son iguales, crear un diccionario para cada fila con las claves 'lat', 'lon' y 'datetime' y los valores correspondientes
                diccionario1 = {'lat': df_tablahechos_parcial.loc[m, 'Latitud'], 'lon': df_tablahechos_parcial.loc[m, 'Longitud'], 'datetime': df_tablahechos_parcial.loc[m, 'Datetime']}
                diccionario2 = {'lat': df_tablahechos_parcial.loc[m+1, 'Latitud'], 'lon': df_tablahechos_parcial.loc[m+1, 'Longitud'], 'datetime': df_tablahechos_parcial.loc[m+1,'Datetime']}
                
                #Colocar los diccionarios resultantes de dos mediciones de GPS consecutivas en la función para calcular los puntos intermedios entre ellas 
                data = [diccionario1, diccionario2]
                df = pd.DataFrame(data)
                df['datetime'] = pd.to_datetime(df['datetime'])
                interpolated_points = []
                for i in range(len(df) - 1):
                    p1, p2 = df.iloc[i], df.iloc[i + 1]
                    points = interpolate_points(p1, p2)
                    interpolated_points.extend(points)
                    resultado = pd.DataFrame(interpolated_points)
                    
                    #Se agregan las otras columnas necesarias al dtaframe resultado     
                    resultado["dataRowType"] = df_tablahechos_parcial.loc[m, 'dataRowType']
                    resultado["Mac"] = df_tablahechos_parcial.loc[m, 'Mac']
                    resultado["name"] = df_tablahechos_parcial.loc[m, 'name']
                    resultado["UUID"] = df_tablahechos_parcial.loc[m, 'UUID']
                    resultado["RSSI"] = df_tablahechos_parcial.loc[m, 'RSSI']

                    #Se acumulan las filas
                    resultados.append(resultado)

    # Concatenar todos los DataFrames en resultados en un solo DataFrame
    if len(resultados) > 0:
        resultado_final_UUID = pd.concat(resultados)
    else:
        resultado_final_UUID = pd.DataFrame()

    resultado_final_UUID = resultado_final_UUID.rename(columns={'lat': 'Latitud', 'lon': 'Longitud', 'datetime': 'Datetime'})

    # Generar las columnas Fecha y Hora a partir de Datetime:
    resultado_final_UUID['Datetime'] = pd.to_datetime(resultado_final_UUID['Datetime'])

    # Creamos las columnas Fecha y Hora
    resultado_final_UUID['Fecha'] = resultado_final_UUID['Datetime'].dt.date
    resultado_final_UUID ['Hora'] = resultado_final_UUID['Datetime'].dt.time   #<---- CUIDADO: No usar este código. En el merge con la tabla tablahechos_BEACON_aleatorios revisar que no haya conflicto con el tipo de dato (object/float)
    #resultado_final_UUID['Hora'] = resultado_final_UUID['Datetime'].dt.strftime('%H:%M:%S')

    #Ordeno las columnas para poder concatenar con la tabla tablahechos_BEACON_aleatorios
    resultado_final_UUID = resultado_final_UUID[["Fecha", "Hora", "Datetime", "dataRowType", "UUID", "Latitud", "Longitud", "Mac", "name", "RSSI"]]

    return resultado_final_UUID 

# ----------->> TERMINA CODIGO POR 'tabla_hechos_final' <<-----------




# ----------->> COMIENZA CODIGO PARA 'cantidad_ganado' <<-----------


# Función para calcular la tabla de cantidad de cabezas de ganado cada día
def cantidad_ganado(df): 
    df1 = df[df["dataRowType"]=='GPS'].copy()                       # agregamos el método copy()
    df1 = df1.reset_index(drop=True)                                # asignamos el resultado a una nueva variable
    df1['Fecha'] = df1['Fecha'].astype(str).str.strip()             # encadenamos los métodos
    resultado = df1.groupby(df1['Fecha'])['UUID'].nunique().reset_index()

    df2 = df[df["dataRowType"]=='BEACON'].copy()                    # agregamos el método copy()
    df2 = df2.reset_index(drop=True)                                # asignamos el resultado a una nueva variable
    df2['Fecha'] = df2['Fecha'].astype(str).str.strip()             # encadenamos los métodos
    resultado1 = df2.groupby(df2['Fecha'])['Mac'].nunique().reset_index()

    resultado["Mac"] = resultado1["Mac"]
    resultado["Cantidad total"] = resultado["UUID"] + resultado["Mac"] 
    return resultado


# ----------->> TERMINA CODIGO POR 'cantidad_ganado' <<-----------



# ----------->> COMIENZA CODIGO PARA 'distancias_recorridas' <<-----------

# Filtra la tabla_hechos_final por tipo GPS y luego por horario, obteniendo un dataframe de GPS diurno y otro noctuno  

def filtrar_diurno_nocturno(df, horainicio, horafin):

    # Filrar el dataframe para que queden solo los dispositivos GPS
    df = df[(df['dataRowType'] == "GPS")]

    # Convertir la columna "Fecha" a datetime para poder filtrar por fecha
    #df['Fecha'] = pd.to_datetime(df['Fecha'])      # ESTO LO COMENTE YO PORQUE ME TIRABA UN WARNING (lo cambie por las 2 lineas que siguen abajo)
    df = df.copy()
    df.loc[:, 'Fecha'] = pd.to_datetime(df['Fecha']).dt.strftime('%Y-%m-%d')

    # Filtrar el DataFrame por hora
    horainicio == pd.to_datetime(horainicio, format='%H:%M:%S').time()
    horafin == pd.to_datetime(horafin, format='%H:%M:%S').time()
     #df = df[(df['Hora'] >= horainicio) & (df['Hora'] <= horafin)]
    
    mask = (df['Hora'].between(horainicio,horafin))
    df1 = df[mask].reset_index(drop=True)
    
    #Obtengo el dataframe nocturno con la máscara opuesta 
    df2 = df[~mask].reset_index(drop=True)

    return df1, df2


# función para calcular la distancia total a partir de una lista de puntos con latitud y longitud

'''
Para el cálculo del recorrido diario se tomaron sólo los GPS que transmitieron, y se tomó como distancia recorrida 
el GPS de mayor recorrido, en lugar de tomar un promedio de todos los GPS como hubiera sido conveniente.
Esto se hizo así porque hay mucha disparidad en la cantidad de mediciones entre diferentes GPS. Muchos transmiten 
muy pocas veces por día y muy espaciado, por lo que la función que genera puntos virtuales no los toma, y por otro 
lado hay otros que tienen varias mediciones en poco tiempo y luego nada, lo que genera una distancia recorrida muy 
corta, y otros GPS solo tienen una medición diaria, con lo cual la distancia recorrida es nula. 
Por ello, hacer un promedio no reflejaría una distancia recorrida medianamente representativa de la realidad.
'''

def calcular_distancia_total(puntos):       # esta funcion se llama desde la funcion distancias (abajo)
    total_distance = 0
    for i in range(len(puntos) - 1):
        distancia = distance(puntos[i], puntos[i + 1]).meters
        total_distance += distancia
    return total_distance

def distancias(df):
    # inicializar variables
    uuid_anterior = None
    lat_anterior = None
    lon_anterior = None
    fecha_anterior = None
    puntos = []
    data = {'UUID': [], 'Fecha': [], 'distancia recorrida': []}

    # recorrer dataframe fila por fila
    for index, row in df.iterrows():
        uuid_actual = row['UUID']
        lat_actual = row['Latitud']
        lon_actual = row['Longitud']
        fecha_actual = row['Fecha']
        
        # si es la primera fila del recorrido, no calculamos distancia
        if uuid_anterior is None:
            uuid_anterior = uuid_actual
            lat_anterior = lat_actual
            lon_anterior = lon_actual
            fecha_anterior = fecha_actual
            puntos.append((lat_actual, lon_actual))
            continue
        
        # si es la misma unidad de recorrido, agregamos punto a la lista
        if uuid_actual == uuid_anterior and fecha_anterior == fecha_actual:
            puntos.append((lat_actual, lon_actual))
            lat_anterior = lat_actual
            lon_anterior = lon_actual
        
        # si es una unidad de recorrido diferente, guardamos los datos en el dataframe nuevo
        else:
            distancia_total = calcular_distancia_total(puntos)
            data['UUID'].append(uuid_anterior)
            data['Fecha'].append(fecha_anterior)
            data['distancia recorrida'].append(distancia_total)
            uuid_anterior = uuid_actual
            lat_anterior = lat_actual
            lon_anterior = lon_actual
            fecha_anterior = fecha_actual
            puntos = [(lat_actual, lon_actual)]
        
    # guardar último recorrido en el dataframe nuevo
    distancia_total = calcular_distancia_total(puntos)
    data['UUID'].append(uuid_anterior)
    data['Fecha'].append(fecha_anterior)
    data['distancia recorrida'].append(distancia_total)

    # crear dataframe nuevo
    df1 = pd.DataFrame(data)

    #Obtenr un DF con la fecha y el recorrido delUUID que más distancia recorrió ese díamáximo
    #Agrupar por fecha y UUID
    df1 = df1.groupby(['Fecha', 'UUID'])['distancia recorrida'].max().reset_index()
    
    # Agrupar por fecha y obtener el máximo de la columna "distancia recorrida"
    df1 =df1 .groupby('Fecha')['distancia recorrida'].max().reset_index()

    return df1


# funcion que devuelve las distancias diurnas, nocturnas y totales del UUID que más distancia recorrió ese día
def distancia_diaria(df, df1):

    df_GPS_distancias_diurnas = distancias(df)

    if 'Unnamed: 0' in df1.columns:
        df1.drop('Unnamed: 0', axis=1, inplace=True)
    df_GPS_distancias_nocturna = distancias(df1)

    # Obtener tabla de distancia diaria total recorrida
    df_GPS_distancia_diaria = df_GPS_distancias_nocturna
    df_GPS_distancia_diaria ["distancia diurna"] = df_GPS_distancias_diurnas ["distancia recorrida"]
    df_GPS_distancia_diaria.rename(columns ={"distancia recorrida": "distancia nocturna"}, inplace = True) 
    df_GPS_distancia_diaria ["distancia total"] = df_GPS_distancia_diaria["distancia nocturna"] + df_GPS_distancia_diaria ["distancia diurna"] 
    df_GPS_distancia_diaria 

    return df_GPS_distancia_diaria 

# ----------->> TERMINA CODIGO POR 'distancias_recorridas' <<-----------


