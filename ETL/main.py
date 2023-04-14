from infra.connection_db import save_tranformation, read_mongo
from importlib import reload
import helpers.datarowdata_transfo # cargamos modulo
reload(helpers.datarowdata_transfo) # recargar modulo si cambian sus funciones
from helpers.datarowdata_transfo import flat_datarows #importamos sus funciones

#example
#df = read_mongo('animals')
#df2 = quit_outliers(df)
#save_tranformation(df2,'animals_limpio')