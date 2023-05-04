from infrastructure.conexiones import *

from importlib import reload

import helpers.ith_transfo
reload(helpers.ith_transfo)
from helpers.ith_transfo import get_ith_with_settlements_names_and_flags

from helpers.funciones import *
import pandas as pd


print('=======>> SE EXTRAEN LOS ARCHIVOS .bson DE GOOGLE DRIVE Y SE CONVIERTEN A DATAFRAME')

df_animals = bson_to_dataframe('animals.bson')
df_datarows = bson_to_dataframe('datarows.bson')
df_devices = bson_to_dataframe('devices.bson')
df_plots = bson_to_dataframe('plots.bson')
df_settlementithcounts = bson_to_dataframe('settlementithcounts.bson')
df_settlements = bson_to_dataframe('settlements.bson')

print('=======>> ARCHIVOS DATAFRAME YA GENERADOS')
print('')



print('=======>> COMIENZA CODIGO DE GENERACION df_general (ESTE PROCESO DEMORA UNOS MINUTOS)')

# Generacion de df con todos los dataRowType = GPS
df_gps = base_gps(df_datarows)

# Generacion de df con todos los dataRowType = BEACON
df_beacon = base_beacon(df_datarows)

# Generacion de df con todos los dataRowType = BATTERY
df_battery = base_battery(df_datarows)

# Armado de la base_general
df_general = base_general(df_gps, df_beacon, df_battery)

# Guardar como .csv y como .parquet
# df_general.to_csv('./tablas/df_general.csv', index=False)
# df_general.to_parquet("./tablas/df_general.parquet", index=False)


print('=======>> TERMINA CODIGO DE GENERACION df_general')
print('')


print("=======>> COMIENZA CODIGO DE GENERACION df_plots2")

# Armado de la base_plots2
df_plots2 = base_plots2(df_animals, df_devices, df_settlements)


print('=======>> TERMINA CODIGO DE GENERACION df_plots2')
print('')


print('=======>> COMIENZA CODIGO DE GENERACION tabla_hechos_final')


"""
Lógica del código:
- Partiendo de la tabla general y plots2 (que son tablas ya con joins previos de los archivos bson originales) se hace un join de ambas para poder tener en una tabla UUID (lat y long de los UUID), dataRowTypes (Beacon, GPS, Battery), MAC (identificación de los BEACON, Datetime, name (Nombre de los establecimientos)). Se hace un merge y se obtiene la tabla tablahechos_ini_filtrado1. 
- A partir de tablahechos_ini_filtrado1 que ya tiene cargadas las coord.(lat y long) aleatorias de los diapositivos BEACON, tomando la última posición del GPS que lo reportó, y aplicando a esa posición una función que calcula un punto aleatorio dentro de un circulo de radio de un metro del dispositivo GPS, y luego multiplica esa coordenada por una distancia en la misma dirección radial, que es función directa del nivel de recepción del RSSI.
- A esta tablahechos_ini_filtrado1 se le aplica la función 'interpolate_points', que va a generar otra tabla denominada resultado_final_BEACONVIR con coordenadas virtuales para puntos intermedios entre dos mediciones consecutivas del dipositivs BEACON con igual Mac, que cumplan con las condiciones de:  
-  1) Estar dentro del mismo día
-  2) Estar separadas entre sí por no más de una cantidad dada de minutos (tiemp_max)

La cantidad de puntos virtuales que se van a generar entre las dos mediciones contiguas se fija en minutos con la variable 'intervalo'.
Luego se concatenan ambas tablas para obtener otra tabla de hechos con las coordenadas de las mediciones de los GPS, las aleatorias de los Beacon, y los puntos virtuales entre dos BEACON consecutivos de igual Mac. Luego se genera una tabla de GPS virtuales entre entre dos dispositivos GPS con igual UUID y consecutivos que cumplan con las condicones 1 y 2 de arriba. Esta última se concatena con la anterior y se obtiene la tabla de hechos principal. 

A partir de la tabla general+plots2, que es el join entre ambas tablas (siendo 'plots2' una tabla que surge del join de settlements + devices + animals), se efectuan varias acciones sobre la tabla para obtener una tabla preliminar de hechos
"""

# LLamado a función que genera la tablahechos_inicial 
tablahechos_ini_filtrado1 = tablahechos_inicial(df_general, df_plots2)

# Llamado a la función fill_beacon_gps_pos que a partir de tablahechos_ini_filtrado1 le agrega una columna con posicion de gps asociado a cada beacon. Hace uso de las subfunciones "get_closest_gpspos" y "get_gps_prevdate"
tablahechos_ini_filtrado1 = fill_beacon_gps_pos(tablahechos_ini_filtrado1)

# Llamada a la función distancia_virtual que agrega la columna distancia virtual al DF tablahechos_ini_filtrado1
tablahechos_ini_filtrado1 = distancia_virtual(tablahechos_ini_filtrado1)

# Agregar las dos nuevas columnas y pasarlas a tipo float
tablahechos_ini_filtrado1[['Latitud_GPS', 'Longitud_GPS']] = tablahechos_ini_filtrado1.apply(lambda row: dividir_gps_position(row), axis=1)
tablahechos_ini_filtrado1[['Latitud_GPS', 'Longitud_GPS']] = tablahechos_ini_filtrado1[['Latitud_GPS', 'Longitud_GPS']].astype(float)

# Llamada a la función a cada fila del dataframe y cambio de nombre del dataframe
tablahechos_BEACON_aleatorios = coord_virtuales(tablahechos_ini_filtrado1)

# Se eliminan columnas "position_gps_assoc", "Latitud_GPS" y "Longitud_GPS" y cambio nombre a la tabla
tablahechos_BEACON_aleatorios = eliminacion_columnas_finales(tablahechos_BEACON_aleatorios,10)

# Se ordena por columnas
tablahechos_BEACON_aleatorios = tablahechos_BEACON_aleatorios.sort_values(['Mac', 'Fecha', 'Hora'], ascending=[True, True, True])

# Llamada a función para obtener la tabla de puntos de cordenadas interpolados entre dos mediciones BEACON con igual MAC
resultado_final_BEACONVIR = tabla_BEACONvir(tablahechos_BEACON_aleatorios)

# Se concatenan la tabla de hechos inicial con la tabla de puntos virtuales UUID + MAC virtuales)
df_tablahechos_parcial = pd.concat([tablahechos_BEACON_aleatorios, resultado_final_BEACONVIR])

df_tablahechos_parcial.dropna(subset=['Latitud','Longitud'],inplace = True)

# Hay que compatibilizar los formatos de la columna hora (eran diferentes en las tablas antes de concatenar)
df_tablahechos_parcial['Fecha'] = pd.to_datetime(df_tablahechos_parcial['Fecha'])

# A partir de df_tablahechos_parcial genero una nueva tabla sólo de GPS en la columna dataRowType
df_solo_UUID = df_tablahechos_parcial.loc[df_tablahechos_parcial['dataRowType'].str.contains('GPS')]                   

# Se ordena la tabla
df_solo_UUID = df_solo_UUID.sort_values(['UUID', 'Fecha', 'Hora'], ascending=[True, True, True])

# Se ordena para después poder recorrerla por fecha, y se la reindexa
df_solo_UUID = df_solo_UUID.sort_values(['Datetime'], ascending=[True])
df_solo_UUID = df_solo_UUID.reset_index(drop=True)

# Llama a la función tabla_UUIDvir que recorre todo el dataframe df_solo_UUID fila por fila y cuando encuentra dos GPS consecutivos iguales alimenta con un par de diccionarios correspondientes a lat, lon y datetime de cada uno de los GPS y alimenta la funcion interpolate_points que calcula los puntos intermedios según las limitaciones impuestas. Se reindexa el dataframe
resultado_final_UUIDvir = tabla_UUIDvir(df_solo_UUID)
resultado_final_UUIDvir = resultado_final_UUIDvir.reset_index(drop=True)

# df_tablahechos_final es la tabla que se usará para graficar el ganado en el mapa y es una concatenacion de resultado_final_UUIDvir (que tiene los UUID virtuales) con tabla_hechos_parcial (que contiene los UUID medidos, más las lat y long de los MAC, mas lat y long de los MAC virtuales BEACON) 
df_tablahechos_final = pd.concat([df_tablahechos_parcial, resultado_final_UUIDvir])

# Se cambian los formatos de fecha para poder ordenar por Fecha, Hora o Datetime
df_tablahechos_final['Fecha'] = pd.to_datetime(df_tablahechos_final['Fecha'])
df_tablahechos_final['Fecha'] = df_tablahechos_final['Fecha'].dt.date
#df_tablahechos_final['Datetime'] = pd.to_datetime(df_tablahechos_final['Datetime'])
df_tablahechos_final['Hora'] = df_tablahechos_final['Hora'].astype(str)
df_tablahechos_final = df_tablahechos_final.reset_index(drop=True)

# Guardar en CSV
save_tranformation(df_tablahechos_final, 'tabla_hechos_final')

print("=======>> TERMINA CODIGO DE GENERACION tabla_hechos_final")
print('')


print("=======>> COMIENZA CODIGO DE GENERACION 'cantidad_ganado'")


# Calcula la cantidad de vacas separadas por GPS y Mac hay en un campo por fecha 
df_cantidad_ganado = cantidad_ganado (df_tablahechos_final)

# Guardar en CSV
save_tranformation(df_cantidad_ganado, 'cantidad_ganado')

print("=======>> TERMINA CODIGO DE GENERACION 'cantidad_ganado'")
print('')




print("=======>> COMIENZA CODIGO DE GENERACION 'distancias_recorridas'")

# A partir del dataframe df_tablahechos_final obtenemos dos dataframes con la posición de las vacas 
# en horario diuro y nocturno
horainicio = '08:00:00'                             # <----------------------- hora de comienzo del sol
horafin = "20:00:00"                                # <----------------------- hora de finalización del sol)
df_UUID_diurno, df_UUID_nocturno = filtrar_diurno_nocturno (df_tablahechos_final, horainicio, horafin)

df_UUID_diurno = df_UUID_diurno.sort_values(['UUID', 'Fecha', 'Hora'], ascending=[True, True, True])
df_UUID_nocturno = df_UUID_nocturno.sort_values(['UUID', 'Fecha', 'Hora'], ascending=[True, True, True])

# Llama a funcion distancia_diaria que devuelve un DataFrame con el recorrido diario del ganado 
# (se toma al GPS de máximo recorrido diario)
df_distancias_recorridas = distancia_diaria(df_UUID_diurno, df_UUID_nocturno)

# Se guarda la tabla
save_tranformation(df_distancias_recorridas, 'distancias_recorridas') 

print("=======>> TERMINA CODIGO DE GENERACION 'distancias_recorridas'")
print('')


print("=======>> COMIENZA CODIGO DE GENERACION 'tabla_ith'")


ith_sett_join = get_ith_with_settlements_names_and_flags()
save_tranformation(ith_sett_join, 'tabla_ith.csv')


print("=======>> TERMINA CODIGO DE GENERACION 'tabla_ith'")
print()

print("=======>> YA SE HA FINALIZADO CON LA EJECUCIÓN DEL CÓDIGO")
print("=======>> LOS ARCHIVOS GENERADOS SE ENCUENTRAN EN LA CARPETA 'transformations'")


