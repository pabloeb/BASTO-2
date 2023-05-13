 
<img width="600" alt="image" src="https://user-images.githubusercontent.com/110254796/235060788-b1b36bbd-f59e-4562-b800-ad0a67523646.png">

# HENRY LABS

# PROYECTO FINAL (grupal)

## DATA SCIENCE / DATA ENGINEER / DATA ANALYTICS

## Integrantes:

Alejandro Busquet

Nicolás Montuori

Pablo Borioli

Ricardo Ramos

-----
-----

## 1- Introduccion y proyecto a desarrollar:

### `-> La empresa:`

Bastó Ganado Inteligente (links de la empresa al pie de este Readme) es una empresa que brinda servicios de geolocalización de ganado, con el fin de aumentar la eficiencia, rentabilidad y sustentabilidad de la producción ganadera. Su sistema basado en IoT monitorea de forma constante la ubicación, salud y bienestar de los animales, lo que permite obtener un pastoreo de precisión.

Este servicio se logra gracias a la implementación de collares con dispositivos GPS, en una parte del ganado, mientras que el resto transmite al GPS mediante dispositivos Bluetooth. De esta forma se recibe informacion de geolocalizacion de la totalidad de los animales del establecimiento.

Algunas ventajas de contar con esta información son:

•	Ahorrar tiempos en la localización y el arreo del ganado

•	Control del manejo de hacienda

•	Conteo diario de animales

•	Prevención del robo de ganado

•	Protección del capital

•	Aportar trazabilidad a la cadena productiva

•	Obtener información de gasto calórico y analizar si esta cumple con los requerimientos diarios

•	Alteraciones del ciclo de pastoreo

•	Monitoreo y control del ITH (índice de temperatura-humedad, número utilizado para indicar la falta de confort causada por los efectos combinados de la temperatura y la humedad del aire; el estrés calórico afecta de manera directa la eficiencia y la producción)
 
<img width="1000" alt="image" src="https://user-images.githubusercontent.com/110254796/235061071-5711eb1c-d06f-4fe8-9f0c-4665f49bf75e.png">

### `-> El proyecto:`

En línea con esta funcionalidad, Bastó Ganado Inteligente asigna a nuestro equipo algunas tareas, con el fin de brindar a sus clientes un servicio de mayor excelencia. Estas tareas son:

•	Implementar un mapa de calor por hora, por día y por rango de fechas, que permita conocer los sectores del lote que más se frecuentan

•	Información de geolocalización distribuida en diurna y nocturna, para conocer si en días con condiciones climáticas adversas, los animales compensan la baja ingesta de alimentos diurna con una mayor actividad nocturna

•	Conteo periódico de cabezas, para conocer en cualquier momento la cantidad de animales y poder prevenir respecto a faltantes

•	Distancia diaria recorrida, para analizar si las vacas están caminando mucho (campo con malas pasturas) y poder accionar en consecuencia

•	Medicion y control del Indice de Temperatura y Humedad (ITH), que es el índice más utilizado para monitorear si las condiciones ambientales resultan estresantes para la hacienda. Valores de ITH ≥ 75 constituyen un alerta (leve); ITH  ≥ 79 es un peligro (moderado) e ITH ≥ 84 es una emergencia (severo)

Esta información debe ser presentada mediante alguna herramienta de visualización, que permita obtener aquellos datos que resulten relevantes de la forma más clara, sencilla y rápida, a fin de transmitir a los clientes datos útiles respecto a su propio ganado y su ciclo de pastoreo.

### `-> Funcionamiento del sistema de geolocalización:`

Bastó Ganado Inteligente implementa su sistema de geolocalizacion del ganado, dentro de cada establecimiento, con la siguiente organización:

•	El 5% de los animales cuenta con dispositivos GPS, que son los únicos que transmiten señales con información al sistema de recepción central. Esta cantidad no es superior debido al impacto que tendría en el costo total del sistema.

•	El 95% restante del ganado, que suelen denominarse BEACON, cuenta con pequeños y ligeros dispositivos Bluetooth denominados CARAVANAS, los que emiten señales con su información a los dispositivos GPS más cercanos. Los GPS toman esa información y la incluyen en el paquete de su envío, cada determinado tiempo.
 

Para el caso de la base de datos de prueba que la empresa nos proporciona para trabajar, es de tipo DEV, es decir de desarrollo y no dispone de una geolocalización exacta de la posición de los dispositivos CARAVANA.    
Por otro lado, la frecuencia ideal o recomendable de recepción de datos prevista para cada dispositivo es de 15 minutos para los GPS, y de 60 minutos para los datos de las CARAVANAS. En el mismo sentido, por contar con una base DEV, tampoco se dispone de información con la periodicidad indicada arriba. En su lugar, los datos se alternan en períodos completamente aleatorios, coexistiendo días con muchos registros y otros con muy pocos o casi nulos.

Para solucionar ambos inconvenientes se implementaron algunas funciones que suplen ambos faltantes. De esta manera se obtiene una base de datos más completa, con registros de localización que para el caso de los GPS indican la ubicación exacta, y para el caso de las CARAVANAS asociadas, indican una posición aproximada a través de una posición virtual relacionada con la distancia a la que se encuentra la CARAVANA del dispositivo GPS que transmite su posisción. Ambas funciones se explicarán con más detalle a continuación.  


### `Generación de geolocalización virtual de CARAVANAS:`  

 Se utilizó una función para geolocalización de las CARAVANAS diferente a la implementada por la empresa, entendiendo que la propuesta brinda mayor exactitud en el posicionamiento en campo de los dispositivos.   

Se genera una función que busca cuál fué el último GPS que transmitió previo a la emisión de la CARAVANA. En base a la localización de ese GPS, se fija la posición de la CARAVANA en forma aleatoria. Utilizando una función que calcula un círculo de un metro de radio con centro en las coordenadas del GPS, genera un ángulo aleatorio posicionando un punto sobre el círculo, lo que introduce una dirección aleatoria. Luego, otra función de distancia basada en la proporcionalidad del valor del RSSI leido por el GPS, nos da la distancia en la que debe posicionarse la CARVANA del GPS. Para esta última función se utilizó una variante de la fórmula de Friis.  
 
 ![image](https://github.com/pabloeb/PROYECTO-BASTO/assets/112908710/7d61b13b-8d94-4916-ae9a-b1c07bce502b)


** Cálculo de la función distancia en la geolocalización de las CARAVANAS:
La potencia de transmisión de los dispositivos Bluetooth puede variar dependiendo del estándar Bluetooth utilizado, y del diseño específico del dispositivo. En general, la mayoría de los dispositivos Bluetooth de Clase 2, que son los más comunes, tienen una potencia de transmisión máxima de alrededor de 2,5 mW o 4 dBm.
Esto puede ser suficiente para la transmisión en campo abierto a distancias cortas de hasta unos pocos metros. Sin embargo, si se necesita una mayor distancia de transmisión o se encuentra en un entorno con obstáculos o interferencias de señales, puede ser necesario utilizar dispositivos Bluetooth de Clase 1, que tienen una potencia de transmisión máxima de alrededor de 100 mW o 20 dBm.
La distancia entre el equipo receptor y el transmisor se calcula en forma aproximada a través de la fórmula de Friis: 

d = 10^((RSSI(1) - RSSI(X) ) / (10 * n))  

donde:

    • d: es la distancia entre el emisor y el receptor en metros.  
    • RSSI(1): es el valor de RSSI de calibración. Se coloca el Emisor a 1m del receptor y se mide el RSSI [dBm].  
    • RSSI (X): es el valor del RSSI medido en [dBm]  
    • n: exponente de pérdida de camino, que depende de las características del entorno y obstáculos. En general, el valor de n varía entre 2 y 4.  


Sin embargo, como referencia, en un entorno de campo abierto sin obstáculos, se puede esperar una pérdida de señal de alrededor de 40 a 60 dB en distancias cortas (hasta 10 metros) para dispositivos Bluetooth de baja potencia (por ejemplo, Clase 2) y de alrededor de 60 a 80 dB en distancias más largas de hasta 100 metros para dispositivos de mayor potencia (por ejemplo, Clase 1). 
Conclusión:
Dependiendo del equipo de bluetooth a utilizar y de las condiciones de transmisión, hay que determinar experimentalmente, en campo, el valor de RSSI(1).

Para nuestro caso de muestra se fijó RSSI(1) en -52 db y n=2.
Se recomienda hacer las mediciones de campo reemplazando los datos supuestos en la función, en el código, en la variable distancia (d).  


### `Generación de puntos intermedios entre mediciones consecutivas muy distantes en el tiempo:`

Para superar este inconveniente y con el fin de poder disponer de una base de datos con una cantidad de registros medianamente aceptable, que en adelante nos permita representar datos con un buen volúmen de información, se dispone suministrar datos adicionales entre mediciones consecutivas de un mismo dispositivo que superen el tiempo de emisión deseado, que para el caso antes mencionado era de 15 minutos. De esta forma, se generan registros con localizaciones intermedias, para que en su lectura se perciba una continuidad lógica en el traslado de cada animal. Con esta finalidad, se implementa una función específica que permite, mediante la selección de un par de variables, elegir el tiempo máximo permitido entre dos mediciones consecutivas, para generar valores intemedios (tiempo_entre_mediciones_max), y también se puede seleccionar cada cuántos minutos se va a generar esas geolocalizaciones virtuales (set_intervalo). Para ejemplificar, si un mismo dispositivo transmite, en un mismo día, dos señales de geoloclización separadas por un lapso de cuatro horas y si las variables mencionadas están fijadas en el panel de variables del programa main.py que se encuentra en la carpeta ETL de la siguiente forma:  

tiempo_entre_mediciones_max = 300  
set_intervalo = 30

La función va a generar 9 puntos de geolocalización "virtual", separados por un intérvalo de 30 minutos entre ellos, y posicionados sobre una recta que une las geolocalizaciones originales inicial y final. Las variables mencionadas pueden ser modificadas fácilmente desde main.py en la carpeta ETL.

Vale aclarar que la información diaria de los dispositivos no será completa, ya que en casos en que se cuente con solo una, o ninguna recepción diaria, en intervalos que entre sí superen la variable fijada como tiempo máximo entre mediciones conseutivas, o en días diferentes, la secuencia en el traslado del animal no podrá ser representada.  



![Captura de pantalla 2023-04-28 a las 02 32 17](https://user-images.githubusercontent.com/110254796/235062566-d4e88e4b-41f3-411d-9dd2-9cacc83ec9b9.jpg)

## `2- Organización del trabajo:`

### `-> Selección de herramientas:`
Luego de estudiar la información que nos fue proporcionada, y el tipo de herramienta que la empresa necesitaba para el producto final, como equipo optamos por canalizar el trabajo mediante:

•	Python: para la extracción de la información de las bases, realización del EDA y ETL, y la posterior confección de las tablas que fueran necesarias para poder visualizar los datos requeridos.

•	Power BI: para traer los datos de las tablas anteriores, relacionarlas entre ellas y con un calendario, y trabajar la información para que podamos presentar los resultados esperados.


### `-> Metodologias ágiles:`
Decidimos utilizar la herramienta Jira, de Atlassian, para la organización interna del equipo, separando todos los procesos en pequeñas tareas y estimando la secuencia correcta de progresión de las mismas. Luego, de forma casi diaria, procedimos a realizar la distribución de dichas tareas entre los miembros, estableciendo los correspondientes sprints o fijación de los tiempos asignados a cada una.
También realizamos seguimientos mediante daylis, de unos 30 minutos y vía meet, donde nos actualizábamos sobre lo que cada uno estaba haciendo, si estaba trabado en algo y qué es lo siguiente que iba a realizar.
Esta metodologia nos permitió avanzar en el proceso de manera organizada y colaborativa, ya que cuando alguien concluía su tarea, asistía a quien pudiera venir algo mas rezagado.

### `-> Python:`
Fue el lenguaje seleccionado para todo el proceso del back, por ser el que nos resulta más comodo para trabajar. Complementado con algunas librerías como pandas, matplotlib, datetime, folium y geopy, logramos transformar los datos y obtener las tablas que necesitábamos, como objetivo final de esta etapa.

### `-> Extracción de los datos`
Como punto de partida se nos proporcionaron seis bases de datos en formato .bson (MongoDB), que mediante python y la librería pandas, convertimos a dataframes para poder proceder a analizar sus datos y encontrar las relaciones entre ellas.

### `-> Análisis Exploratorio de Datos (EDA):`
Una vez familiarizados con el tipo de datos existente en cada tabla, y la forma en que estas se vinculaban, se pasó al análisis de los datos, para lo cual nos apoyamos en la librería matplotlib, que nos permitió, de forma mas “amigable”, conocer los datos dentro de cada columna, ayudando ésto a realizar un ETL en algunas de ellas. También se llevó adelante un estudio de outliers.

### `-> Power BI:`
Una vez obtenidas las tablas en el back, se realizó la ingesta de las mismas en Power BI. Se procede a la organización de esos datos de manera tal que nos permita representar las tareas solicitadas. Para esta etapa se utilizaron herramientas como el mapa de calor, barras de desplazamiento, gráficos de líneas, de barras y de torta, así como diversos KPI. Todo distribuido en varios dashboards, que permiten la lectura de la información de forma clara y ordenada.

### `-> Dashboards:`
Por ser la representación final de todo el trabajo realizado, tuvimos especial cuidado, no sólo en el contenido de los dasboards, que debió ser cada uno estructurado acorde a un patrón específico, sino también en las formas, cuidando la presencia de una portada de presentación, los correspondientes títulos, los colores y una secuencia de datos logica. Se procuró que para el final, al usuario le quede una sensación de integridad.

### `-> KPIs:`
Distribuidos entre los diferentes dashboards, se utilizaron para expresar información relevante ante una selección de fecha o rango. Permiten visualizar rápidamente datos como la cantidad de dispositivos GPS, Bluetooth y totales, el recorrido diario, discriminar las distancias transitadas en períodos diurno y nocturno, determinar la cantidad de días de olas de calor, la cantidad de horas de estrés calórico (ITH) y demás.

### `-> Github:`
Se interactuó con Github de manera colaborativa durante todo el proceso de trabajo. Una vez consideramos concluido el proyecto, se terminó de incorporar el mismo para una libre disponibilidad de quien lo quisiera ver, revisar y probar.

![Captura de pantalla 2023-04-28 a las 02 45 18](https://user-images.githubusercontent.com/110254796/235064505-111f373e-90d0-4444-92d2-7c12c214616a.jpg)

## `3- Etapas del trabajo:`

-	En python:

•	Iniciamos el proceso transformando las bases proporciondas, a dataframes.

•	Una vez fuimos comprendiendo los datos en cada una de las bases e interpretamos la relación existente entre ellas, estudiamos la manera más conveniente para confeccionar una tabla “madre”, donde ya estuvieran eliminados todos los datos que no nos serían de utilidad, y a la vez que contenga toda la información que necesitaríamos posteriormente para crear las tablas finales objetivo.

•	Mediante la utilización de tablas intermedias, se van cargando las coordenadas de latitud y longitud exactas de los GPS, y las ubicaciones aleatorias (conservando su distancia al GPS) de los BEACON(CARAVANA). Estas últimas las logramos aplicando una función que calcula, a partir del dispositivo GPS que envió la señal, un punto aleatorio dentro de un círculo de radio de un metro de dicho dispositivo, y luego multiplicando esa coordenada por una distancia en la misma dirección radial, que es función directa del nivel de recepción del RSSI.

•	Se estandarizan los formatos de fechas, para que no existan inconsistencias al trabajar con las fechas, las horas y los datetime.

•	Generamos y guardamos la primera tabla, que será de gran utilidad para realizar diferentes visualizaciones,  como los mapas de calor. A su vez hará de “base” para el resto de las tablas por generar. Se la denomina ‘tabla_hechos_final.csv’.

•	Procedemos a realizar la segunda tabla, que contiene información referente a la cantidad de vacas, separadas por establecimiento y  por fecha, y dentro de estos parámetros, discriminadas por GPS y por BEACON. La guardamos como ‘cantidad_ganado.csv’.

•	A partir del dataframe ‘tabla_hechos_final’ obtenemos otros dos que nos dividen las posiciones del ganado en horarios diurno y nocturno, a fin de utilizarlas para cumplir con otra de las tareas asignadas.

•	Calculamos el recorrido diario del ganado, tomando como parámetro el GPS de mayor recorrido. Esto se encaró así por la existencia de una gran disparidad en la cantidad de mediciones entre diferentes GPS. Algunos transmiten muy pocas veces por día, y muy espaciado, por lo que la función que genera los puntos virtuales no los considera. Y por otro lado existen GPS que tienen varias mediciones en poco tiempo y luego nada, lo que significa una distancia recorrida muy corta. Otros GPS, en cambio, sólo tienen una medición diaria, con lo cual la distancia recorrida es nula. Por todos estos factores, entendemos que presentar un promedio no reflejaría una distancia recorrida medianamente representativa de la realidad. Esta tabla se guarda como ‘distancias_recorridas.csv’.

•	Para la tabla referente a los valores de ITH, cuyas mediciones son provistas por los dispositivos, y cuya utilidad será determinar el valor de este índice para los días que se seleccionen. Con este dato y con la tabla del punto anterior, se podrá evaluar si los animales, ante una importante disminución en su actividad diurna, producto de condiciones climáticas adversas, compensan este aspecto con una mayor actividad en horarios nocturnos, cuando el clima suele ser más agradable. El objetivo final de este análisis es hacer un seguimiento de la ingesta diaria del animal, la cual debería mantenerse constante y no decaer. En este caso se trata de la ‘tabla_ith.csv’.

•   Tabla 'Calendario', tabla de fechas  

•   La tabla 'GPS_recorrido_individual' contiene la información de la distancia diurna, nocturna y total recorrida por cada animal que posee dispositivo GPS, por día y por establecimiento.  

•   La tabla 'recorrido_rebanio' contiene los datos para geolocalizar el recorrido de un animal con dispositivo GPS, por día y por establecimiento.

Obtenidas las siete tablas, el equipo cuenta con la información necesaria para satisfacer las demandas, dando por finalizada esta etapa del proyecto. Las tablas se guardan en formato .csv y por duplicado en dos carpetas separadas, ya que entre ambos grupos por su destino hay pequeñas variantes de configuración. Un grupo van a ser guardadas en el archivo que genera cada vez que se corre main.py (ETL) denominado 'PowerBI_files', desde donde son ingesadas por PowerBI para generar los dashboards. Otro grupo con la misma modalidd se guardan en el archivo 'transformations', y son las tablas que va a consumir la API para entregar la información requerida.

-	Power BI:
•	Mediante la vinculación de las 7 tablas se conforma la estructura de trabajo para esta herramienta. La misma queda de esta manera:

![image](https://github.com/pabloeb/PROYECTO-BASTO/assets/112908710/fbda5b52-a9bc-4883-8b7a-858200fa37d9)



•	Si bien no fue lo primero en lo que se trabajó, acá mostramos en principio la portada, a fin de respetar el mismo orden que se lleva en la presentación final.

 ![PHOTO-2023-04-27-18-57-59](https://user-images.githubusercontent.com/110254796/235063522-6fb85234-f59a-4bcb-81cc-054c7ae36ab8.jpg)

•	A continuación, una imágen del primer dashboard. En ella se puede apreciar un mapa de calor que muestra la ubicación geográfica de todas las vacas en cada período preseleccionado, haciendo énfasis en las zonas con mayor presencia animal. La información se puede filtrar por día y por establecimiento, y una vez definidos, se reflejan los datos referentes a los recorridos diarios, diurnos y nocturnos, mediante la implementación de 3 KPI y un gráfico de barras verticales.

 ![PHOTO-2023-04-27-15-08-41](https://user-images.githubusercontent.com/110254796/235063886-81f9c45b-b04f-4b7d-a5bc-c785c8a942e2.jpg)

•	El segundo dashboard permite visualizar el mapa el recorrido completo diario de un animal (GPS) por fecha y por establecimiento.

![image](https://github.com/pabloeb/PROYECTO-BASTO/assets/112908710/e7383207-b119-4c9b-b776-21706d14bf08)


•	El tercer dashboard permite visualizar las métricas del recorrido completo diario total, diurno y nocturno, de un animal (GPS) por fecha y por establecimiento.

![image](https://github.com/pabloeb/PROYECTO-BASTO/assets/112908710/1b839af1-3470-43d9-9d7a-75c5c850f949)


•   El cuarto dashboard proporciona información, previa selección del período y el establecimiento deseados, sobre el desplazamiento del ganado y su relación con el índice ITH. Mediante sendos KPI informa la cantidad de días de calor y las horas de estrés calórico, complementado por un gráfico de líneas que enseña el promedio diario.

 ![PHOTO-2023-04-27-15-09-17](https://user-images.githubusercontent.com/110254796/235063945-55774a08-a848-4b18-abb5-e9392bf067ac.jpg)


•	El quinto dashboard refleja el recuento diario del ganado. Como en los anteriores, con la previa selección, muestra el correspondiente mapa de calor del período e informa el total de animales, discriminando por aquellos que tienen dispositivos GPS y los que tienen Bluetooth. Esto se complementa con una representación gráfica mediante un gráfico de torta.

 ![PHOTO-2023-04-27-18-58-01](https://user-images.githubusercontent.com/110254796/235064017-5da4d7b9-75d5-43b0-9357-25af5f65a28f.jpg)


•	El último dashboard se ocupa de establecer una relación entre la distancia recorrida por las vacas y el promedio de ITH del mismo período. El objetivo de esta información es controlar que el ganado, ante situaciones climáticas extremas, no merma su ingesta diaria, ya que compensa su baja actividad diurna con una alta actividad nocturna. Esta información es de gran importancia para el sector ganadero.

![PHOTO-2023-04-27-23-40-41](https://user-images.githubusercontent.com/110254796/235064062-3f42533e-b439-4603-909f-f74fe8eed77e.jpg)


## `4- API`
A partir de los datos transformados, resultado del proceso ETL, generamos una API para exponer esos datos al usuario.
Esta se compone de varios endpoints, como por ejemplo:

* Cantidad de caravanas en un día y establecimiento
* Posiciones de caravanas en un día y establecimiento
* Horas de estres calórico en un período de fechas en un establecimiento

La idea es que el usuario pueda seleccionar un establecimiento y una fecha, o un rango de fechas, y obtener la última información de los sensores del ganado registrados en la base de Bastó.


## `5- Secuencia de uso y Flujo de datos`  

### `Toma de datos:`  

Debido a cuestiones operacionales se decidió que el programa principal main.py (ETL) busque los datos en los archivos BSON (Mongo) proporcionados por la empresa Bastó. Los mismos se encuentran hosteados en la nube, en nuestro caso DROPBOX. Si se desea modificar o actualizar archivos, los mismos se deberán leer desde donde el usuario determine hostearlos. En nuestro caso lo hacemos desde:

print('=======>> SE EXTRAEN LOS ARCHIVOS .bson DE GOOGLE DRIVE Y SE CONVIERTEN A DATAFRAME')

df_animals = bson_to_dataframe('animals.bson')
df_datarows = bson_to_dataframe('datarows.bson')
df_devices = bson_to_dataframe('devices.bson')
df_plots = bson_to_dataframe('plots.bson')
df_settlementithcounts = bson_to_dataframe('settlementithcounts.bson')
df_settlements = bson_to_dataframe('settlements.bson')

Se podrían incorporar algunas pocas líneas de código para leer desde una base MONGO

### `Fijar variables:`  

El código main.py (ETL) permite modificar ciertas variables de acuerdo a las necesidades del usuario:

` ================================================================================================================`  
` ================================================================================================================`  
` ----------------------------------------------->>  IMPORTANTE  <<-----------------------------------------------`  
` ================================================================================================================`  
` ================================================================================================================`

DEFINICION DE VARIABLES

hora_inicio =       "08:00:00"              # <----------------------- hora de comienzo período diurno  
hora_fin =          "20:00:00"              # <----------------------- hora de comienzo período nocturno  
set_intervalo =     30                      # <----------------------- controla el intervalo entre puntos virtuales (en minutos)  
fecha_inicial =     "2023-02-22"            # <----------------------- el primer dia dentro del rango deseado (va o la fecha o "")  
fecha_final =       "2023-03-08"            # <----------------------- el ultimo dia dentro del rango deseado (va o la fecha o "")  
establecimiento =   "MACSA"                 # <----------------------- el establecimiento a analizar (va o el nombre del establecimiento o "")  
RSSI_un_metro =     -52                     # <----------------------- constante que se obtiene por medición del emisor y receptor, a 1 m de distancia  
n =                 2                       # <----------------------- constante en función de las obstrucciones del terreno y que oscila entre 2 y 4 (2 = campo abierto)  


tiempo_entre_mediciones_max = 480           # <----------------------- tiempo máximo que puede haber entre mediciones para calcular puntos virtuales en el medio (en minutos)

` ================================================================================================================`  
` ================================================================================================================`  
 `----------------------------------------------->>  IMPORTANTE  <<-----------------------------------------------`  
` ================================================================================================================`  
` ================================================================================================================`

Esto permite hacer algunos filtros a la hora de visualizar la información final. 
* Se puede generar una tabla completa con todos los establecimientos fijando 'establecimiento en ""', o puede colocarse el nombre del establecimiento cuyos datos se desean analizar.  
* Se puede filtrar las bases de datos a generar por fechas con fecha_inicial y final.
* Se puede modificar el horario de comienzo de los recorridos nocturnos y diurnos, para estipularlos según las condiciones estacionales.(hora_inicio y hora_fin).
* La función que mide la distancia de las CARAVANAS a los GPS que retransmiten su información, es proporcional al valor del RSSI medido por el GPS. Ese valor es sensible a muchas condicines que lo afectan directamente. Entre ellas la potencia y clase de los equipos de bluetooth y GPS utilizados, y determinadas condiciones de campo. Por lo que es menester realizar una prueba experimental para determinar el valor de la variable RSSI_un_metro. En campo, la prueba se realiza colocando los dos dispositivos a un metro de distancia y se lee el valor de RSSI del receptor. Hay que ajustar el valor de la variable en el cuadro presentado arriba, para que la función respectiva pueda hacer un cálculo aproximado de la distancia entre CARAVANA y GPS.
* El otro valor a ajustar es 'n' que depende de las condiciones geográficas y nivel de obstáculos del terreno. Varía entre 2 y 4. En terreno abierto se puede utilizar n=2.

### `Ejecutar main.py (ETL):`   

La ejecución del programa main.py del archivo ETL, generará como ya se explicó previamente, las tablas necesarias para que sean ingestadas por PowerBI, si se desean ver dashboards con todos los graficos de la información, o para utilizar la API y extraer los datos necesarios por esa vía.

### `Ver los datos en Power BI:`   
Ejecutar el archivo Dashboard final.pbix que se encuentra en la carpeta Dashboard desde PowerBi Desktop. Para ver los últimos datos generdos al correr main.py, simplemente oprimir el botón Actualizar en la cinta de Power BI.

### `Hacer consultas y extraer datos de la API:` 
- Para obtener los datos de la API, ejecutar el programa main.py (API)  

- Luego, en la consola ejecutar uvicorn main:app --reload, de la siguiente forma:  

(proyctobastoenv) C:\Users\DELL\Desktop\Henry\LABS\PF-Basto\PROYECTO-BASTO\API>uvicorn main:app --reload  
INFO:     Will watch for changes in these directories: ['C:\\Users\\DELL\\Desktop\\Henry\\LABS\\PF-Basto\\PROYECTO-BASTO\\API']  
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)  
INFO:     Started reloader process [4600] using WatchFiles  
INFO:     Started server process [1544]  
INFO:     Waiting for application startup.  
INFO:     Application startup complete.  

- Abrir el browser y colocar los datos del localhost, por ejemplo:

http://127.0.0.1:8000/docs

Aparecera la consola de FastAPI, con la documentación y la posibilidad de hacer queries directamente en pantalla:

![image](https://github.com/pabloeb/PROYECTO-BASTO/assets/112908710/fe80b650-403f-4346-bb22-3652ac86adfa)

![image](https://github.com/pabloeb/PROYECTO-BASTO/assets/112908710/5e69d9ea-a1d4-4e16-91f1-9e224a8f1ad6)


Esperamos que hayan disfrutado el recorrido.

## Muchas gracias!!

-------
-------

### `Autores:`

* Alejandro Busquet -> algabu00@gmail.com

* Pablo Borioli -> boriolip@yahoo.com.ar

* Nicolás Montuori -> nicomontuori@gmail.com

* Ricardo Ramos -> rikigermanramos@gmail.com

-------

### Bastó Ganado Inteligente:

* Visitar sitio web [AQUÍ](https://www.xn--bast-tqa.com.ar/ "AQUÍ")

* Visitar Linkedin [AQUÍ](https://www.linkedin.com/in/bast%C3%B3ganadointeligente/?originalSubdomain=ar![image] "AQUÍ")

-------

### Agradecimientos:

* Al staff de Henry Labs por habernos permitido realizar nuestro proyecto final trabajando para una empresa real. Especialmente a aquellos con quienes tuvimos más contacto: Pablo Romero y nuestro HM Jonathan Deiloff, siempre presente para brindar una opinión y/o colaborar con su ayuda.

* A todo el equipo de Bastó Ganado Inteligente, por su asistencia, seguimiento y buena onda siempre. Fue un placer haber trabajado con uds y ojalá podamos darle continuidad de alguna forma.

-------

### Notas:
* Con el fin de mejorar la calidad de datos de los datasets que nos proveyó el equipo de Bastó, adjuntamos un informe de calidad de datos con observaciones que creemos deben tenerse en cuenta, y además añadimos un diccionario de datos con los términos que creemos más importantes para la comprensión de los datasets.
