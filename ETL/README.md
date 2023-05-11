Esta carpeta contiene los pasos necesarios para el proceso ETL de los datos proporcionados por BASTÓ.
Para obtener los archivos transformados, requeridos por el dashboard mencionado en el proyecto, realizar:
- clonar el repositorio
- moverse a la carpeta ETL 
- crear entorno virtual
- activar entorno virtual
- realizar pip install -r requirements.txt
- ejecutar el archivo main.py
- al terminar la ejecución se habrá generado una carpeta llamada transformations donde se hallan los datasets ya transformados y listos para usarse en el dashboard

#### Nota
El proceso ETL actualmente esta simplificado para fines demostrativos. 
En la tabla ith solo se tiene en cuenta los datos relacionados a un establecimiento.
Para eliminar esta restricción:
- acceder al archivo helpers/ith_transfo.py
- en la linea 78 cambiar a 

    <code>df_sett = get_selected_settlements()<code>
