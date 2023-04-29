 
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

-> La empresa:

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

-> El proyecto:

En línea con esta funcionalidad, Bastó Ganado Inteligente asigna a nuestro equipo algunas tareas, con el fin de brindar a sus clientes un servicio de mayor excelencia. Estas tareas son:

•	Implementar un mapa de calor por hora, por día y por rango de fechas, que permita conocer los sectores del lote que más se frecuentan

•	Información de geolocalización distribuida en diurna y nocturna, para conocer si en días con condiciones climáticas adversas, los animales compensan la baja ingesta de alimentos diurna con una mayor actividad nocturna

•	Conteo periódico de cabezas, para conocer en cualquier momento la cantidad de animales y poder prevenir respecto a faltantes

•	Distancia diaria recorrida, para analizar si las vacas están caminando mucho (campo con malas pasturas) y poder accionar en consecuencia

•	Medicion y control del Indice de Temperatura y Humedad (ITH), que es el índice más utilizado para monitorear si las condiciones ambientales resultan estresantes para la hacienda. Valores de ITH ≥ 75 constituyen un alerta (leve); ITH  ≥ 79 es un peligro (moderado) e ITH ≥ 84 es una emergencia (severo)

Esta información debe ser presentada mediante alguna herramienta de visualización, que permita obtener aquellos datos que resulten relevantes de la forma más clara, sencilla y rápida, a fin de transmitir a los clientes datos útiles respecto a su propio ganado y su ciclo de pastoreo.

-> Funcionamiento del sistema de geolocalización:

Bastó Ganado Inteligente implementa su sistema de geolocalizacion del ganado, dentro de cada establecimiento, con la siguiente organización:

•	El 5% de los animales cuenta con dispositivos GPS, que son los únicos que transmiten señales con información al sistema de recepción central. Esta cantidad no es superior debido al impacto que tendría en el costo total del sistema.

•	El 95% restante del ganado, que suelen denominarse BEACON, cuenta con dispositivos Bluetooth, los que emiten señales con su información a los dispositivos GPS más cercanos. Los GPS toman esa información y la incluyen en el paquete de su envío, cada determinado tiempo.

La frecuencia de emisión para cada dispositivo es de 15 minutos para los GPS, y de 60 minutos para los BEACON.

Para el caso de las bases de datos de prueba, que la empresa nos proporciona para trabajar, no se dispone de información con la periodicidad indicada arriba. En su lugar, los datos se alternan en períodos completamente aleatorios, coexistiendo días con muchos registros y otros con muy pocos o casi nulos.

Para superar esto y con el fin de que podamos disponer de una base con una cantidad de registros medianamente aceptable, que en adelante nos permita representar datos con un buen volúmen de información, se dispone que tomemos un solo establecimiento y un rango de tiempo específico. Dentro de ese lapso, a partir de los registros ya existentes, debemos generar registros con localizaciones intermedias, para que en su lectura se perciba una continuidad lógica en el traslado de cada animal.

De esta manera se obtiene una base de datos más completa, con registros de localización que para el caso de los GPS indican la ubicación exacta, y para el caso de los BEACON asociados, se establecerá la distancia a su GPS emisor mediante una fórmula que incluye un dato ya incorporado (el RSSI o indicador de fuerza de señal recibida, que es una escala que mide el nivel de potencia de señal en redes inalámbricas).

Vale aclarar que la información diaria de los dispositivos no será completa, ya que en casos en que se cuente con solo una, o ninguna recepción diaria, o en intervalos que entre sí superen las ocho horas, la secuencia en el traslado del animal no podrá ser representado.

![Captura de pantalla 2023-04-28 a las 02 32 17](https://user-images.githubusercontent.com/110254796/235062566-d4e88e4b-41f3-411d-9dd2-9cacc83ec9b9.jpg)

## 2- Organización del trabajo:

-> Selección de herramientas:
Luego de estudiar la información que nos fue proporcionada, y el tipo de herramienta que la empresa necesitaba para el producto final, como equipo optamos por canalizar el trabajo mediante:

•	Python: para la extracción de la información de las bases, realización del EDA y ETL, y la posterior confección de las tablas que fueran necesarias para poder visualizar los datos requeridos.

•	Power BI: para traer los datos de las tablas anteriores, relacionarlas entre ellas y con un calendario, y trabajar la información para que podamos presentar los resultados esperados.


-> Metodologias ágiles:
Decidimos utilizar la herramienta Jira, de Atlassian, para la organización interna del equipo, separando todos los procesos en pequeñas tareas y estimando la secuencia correcta de progresión de las mismas. Luego, de forma casi diaria, procedimos a realizar la distribución de dichas tareas entre los miembros, estableciendo los correspondientes sprints o fijación de los tiempos asignados a cada una.
También realizamos seguimientos mediante daylis, de unos 30 minutos y vía meet, donde nos actualizábamos sobre lo que cada uno estaba haciendo, si estaba trabado en algo y qué es lo siguiente que iba a realizar.
Esta metodologia nos permitió avanzar en el proceso de manera organizada y colaborativa, ya que cuando alguien concluía su tarea, asistía a quien pudiera venir algo mas rezagado.

-> Python:
Fue el lenguaje seleccionado para todo el proceso del back, por ser el que nos resulta más comodo para trabajar. Complementado con algunas librerías como pandas, matplotlib, datetime, folium y geopy, logramos transformar los datos y obtener las tablas que necesitábamos, como objetivo final de esta etapa.

-> Extracción de los datos
Como punto de partida se nos proporcionaron seis bases de datos en formato .bson (MongoDB), que mediante python y la librería pandas, convertimos a dataframes para poder proceder a analizar sus datos y encontrar las relaciones entre ellas.

-> Análisis Exploratorio de Datos (EDA):
Una vez familiarizados con el tipo de datos existente en cada tabla, y la forma en que estas se vinculaban, se pasó al análisis de los datos, para lo cual nos apoyamos en la librería matplotlib, que nos permitió, de forma mas “amigable”, conocer los datos dentro de cada columna, ayudando esto a realizar un ETL en algunas de ellas. También se llevó adelante un estudio de outliers.

-> Power BI:
Una vez obtenidas las tablas en el back, se realizó la ingesta de las mismas en Power BI. Se procede a la organización de esos datos de manera tal que nos permita representar las tareas solicitadas. Para esta etapa se utilizaron herramientas como el mapa de calor, barras de desplazamiento, gráficos de líneas, de barras y de torta, así como diversos KPI. Todo distribuido en varios dashboards, que permiten la lectura de la información de forma clara y ordenada.

-> Dashboards:
Por ser la representación final de todo el trabajo realizado, tuvimos especial cuidado, no sólo en el contenido de los dasboards, que debió ser cada uno estructurado acorde a un patrón específico, sino también en las formas, cuidando la presencia de una portada de presentación, los correspondientes títulos, los colores y una secuencia de datos logica. Se procuró que para el final, al usuario le quede una sensación de integridad.

-> KPIs:
Distribuidos entre los diferentes dashboards, se utilizaron para expresar información relevante ante una selección de fecha o rango. Permiten visualizar rápidamente datos como la cantidad de dispositivos GPS, Bluetooth y totales, el recorrido diario, discriminar las distancias transitadas en períodos diurno y nocturno, determinar la cantidad de días de olas de calor, la cantidad de horas de estrés calórico (ITH) y demás.

-> Github:
Se interactuó con Github de manera colaborativa durante todo el proceso de trabajo. Una vez consideramos concluido el proyecto, se terminó de incorporar el mismo para una libre disponibilidad de quien lo quisiera ver, revisar y probar.

![Captura de pantalla 2023-04-28 a las 02 45 18](https://user-images.githubusercontent.com/110254796/235064505-111f373e-90d0-4444-92d2-7c12c214616a.jpg)

## 3- Etapas del trabajo:

-	En python:

•	Iniciamos el proceso transformando las bases proporcionaron, a dataframes.

•	Una vez fuimos comprendiendo los datos en cada una de las bases e interpretamos la relación existente entre ellas, estudiamos la manera más conveniente para confeccionar una tabla “madre”, donde ya estuvieran eliminados todos los datos que no nos serían de utilidad, y a la vez que contenga toda la información que necesitaríamos posteriormente para crear las tablas finales objetivo.

•	Mediante la utilización de tablas intermedias, se van cargando las coordenadas de latitud y longitud exactas de los GPS, y las ubicaciones aleatorias (conservando su distancia al GPS) de los BEACON. Estas últimas las logramos aplicando una función que calcula, a partir del dispositivo GPS que envió la señal, un punto aleatorio dentro de un círculo de radio de un metro de dicho dispositivo, y luego multiplicando esa coordenada por una distancia en la misma dirección radial, que es función directa del nivel de recepción del RSSI.

•	Se estandarizan los formatos de fechas, para que no existan inconsistencias al trabajar con las fechas, las horas y los datetime.

•	Generamos y guardamos la primera tabla, que será de gran utilidad para realizar diferentes visualizaciones,  como los mapas de calor. A su vez hará de “base” para el resto de las tablas por generar. Se la denomina ‘tabla_hechos_final.csv’.

•	Procedemos a realizar la segunda tabla, que contiene información referente a la cantidad de vacas, separadas por establecimiento y  por fecha, y dentro de estos parámetros, discriminadas por GPS y por BEACON. La guardamos como ‘cantidad_ganado.csv’.

•	A partir del dataframe ‘tabla_hechos_final’ obtenemos otros dos que nos dividen las posiciones del ganado en horarios diurno y nocturno, a fin de utilizarlas para cumplir con otra de las tareas asignadas.

•	Calculamos el recorrido diario del ganado, tomando como parámetro el GPS de mayor recorrido. Esto se encaró así por la existencia de una gran disparidad en la cantidad de mediciones entre diferentes GPS. Algunos transmiten muy pocas veces por día, y muy espaciado, por lo que la función que genera los puntos virtuales no los considera. Y por otro lado existen GPS que tienen varias mediciones en poco tiempo y luego nada, lo que significa una distancia recorrida muy corta. Otros GPS, en cambio, sólo tienen una medición diaria, con lo cual la distancia recorrida es nula. Por todos estos factores, entendemos que presentar un promedio no reflejaría una distancia recorrida medianamente representativa de la realidad. Esta tabla se guarda como ‘distancias_recorridas.csv’.

•	Por último se encara la tarea referente a los valores de ITH, cuyas mediciones son provistas por los dispositivos, y se procede a confeccionar la última tabla, que será de utilidad para determinar el valor de este índice para los días que se seleccionen. Con este dato y con la tabla del punto anterior, se podrá evaluar si los animales, ante una importante disminución en su actividad diurna, producto de condiciones climáticas adversas, compensan este aspecto con una mayor actividad en horarios nocturnos, cuando el clima suele ser más agradable. El objetivo final de este análisis es hacer un seguimiento de la ingesta diaria del animal, la cual debería mantenerse constante y no decaer. En este caso se trata de la ‘tabla_ith.csv’.

Obtenidas las cuatro tablas, el equipo cuenta con la información necesaria para satisfacer las demandas, dando por finalizada esta etapa del proyecto. A continuación se cargarán las mismas en Power BI, donde trabajaremos en la expresión visual de los datos requeridos.

-	Power BI:
•	Mediante la vinculación de las 4 tablas a una tabla calendario central, se conforma la estructura de trabajo para esta herramienta. La misma queda de esta manera:

 ![Captura de pantalla 2023-04-25 a las 16 57 05](https://user-images.githubusercontent.com/110254796/235063353-6012a486-32e2-45e6-97bf-d37711b9a4eb.jpg)

•	Si bien no fue lo primero en lo que se trabajó, acá mostramos en principio la portada, a fin de respetar el mismo orden que se lleva en la presentación final.

 ![PHOTO-2023-04-27-18-57-59](https://user-images.githubusercontent.com/110254796/235063522-6fb85234-f59a-4bcb-81cc-054c7ae36ab8.jpg)

•	A continuación, una imágen del primer dashboard. En ella se puede apreciar un mapa de calor que muestra la ubicación geográfica de todas las vacas en cada período preseleccionado, haciendo énfasis en las zonas con mayor presencia animal. La información se puede filtrar por día y por establecimiento, y una vez definidos, se reflejan los datos referentes a los recorridos diarios, diurnos y nocturnos, mediante la implementación de 3 KPI y un gráfico de barras verticales.

 ![PHOTO-2023-04-27-15-08-41](https://user-images.githubusercontent.com/110254796/235063886-81f9c45b-b04f-4b7d-a5bc-c785c8a942e2.jpg)

•	El segundo dashboard proporciona información, previa selección del período y el establecimiento deseados, sobre el desplazamiento del ganado y su relación con el índice ITH. Mediante sendos KPI informa la cantidad de días de calor y las horas de estrés calorico, complementado por un gráfico de líneas que enseña el promedio diario.

 ![PHOTO-2023-04-27-15-09-17](https://user-images.githubusercontent.com/110254796/235063945-55774a08-a848-4b18-abb5-e9392bf067ac.jpg)

•	El tercer dashboard refleja el recuento diario del ganado. Como en los anteriores, con la previa selección, muestra el correspondiente mapa de calor del período e informa el total de animales, discriminando por aquellos que tienen dispositivos GPS y los que tienen Bluetooth. Esto se complementa con una representación gráfica mediante un gráfico de torta.

 ![PHOTO-2023-04-27-18-58-01](https://user-images.githubusercontent.com/110254796/235064017-5da4d7b9-75d5-43b0-9357-25af5f65a28f.jpg)

•	El último dashboard se ocupa de establecer una relación entre la distancia recorrida por las vacas y el promedio de ITH del mismo período. El objetivo de esta información es controlar que el ganado, ante situaciones climáticas extremas, no merma su ingesta diaria, ya que compensa su baja actividad diurna con una alta actividad nocturna. Esta información es de gran importancia para el sector ganadero.

![PHOTO-2023-04-27-23-40-41](https://user-images.githubusercontent.com/110254796/235064062-3f42533e-b439-4603-909f-f74fe8eed77e.jpg)


Y eso es todo! Esperamos hayan disfrutado el recorrido.

## Muchas gracias!!

-------
-------

### Autores:

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
* Con el fin de mejorar la calidad de datos de los datasets que nos proveyó el equipo de Bastó adjuntamos un informe de calidad de datos con observaciones que creemos deben tenerse en cuenta, y además añadimos un diccionario de datos con los términos que creemos más importantes para la comprensión de los datasets.

