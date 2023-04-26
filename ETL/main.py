from infra.connection_db import save_tranformation, read_mongo
from importlib import reload
import helpers.datarowdata_transfo # cargamos modulo
reload(helpers.datarowdata_transfo) # recargar modulo si cambian sus funciones
from helpers.datarowdata_transfo import flat_datarows #importamos sus funciones
import helpers.ith_transfo
reload(helpers.ith_transfo)
from helpers.ith_transfo import get_ith_with_settlements_names_and_flags



ith_sett_join = get_ith_with_settlements_names_and_flags()
save_tranformation(ith_sett_join, 'tabla_ith.csv')