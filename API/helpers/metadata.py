from fastapi import FastAPI

description = """

## Posiciones de un collar durante fecha en un establecimiento

Consulte latitudes y longitudes de un animal con collar durante un dia en un establecimiento.

Las opciones son: 

* **fecha** fecha a consultar - formato: año-mes-dia (ejemplo 2023-03-01).
* **id collar** identificador de collar (ejemplo A12)
* **establecimiento** nombre del establecimiento en que circula el ganado (ejemplo MACSA).

## Identificadores de collares durante fecha en un establecimiento

Consulte identificadores de collares de animales durante un dia en un establecimiento.

Las opciones son: 

* **fecha** fecha a consultar - formato: año-mes-dia (ejemplo 2023-03-01).
* **establecimiento** nombre del establecimiento en que circula el ganado (ejemplo MACSA).

## Posiciones de una caravana durante fecha en un establecimiento

Consulte latitudes y longitudes de un animal con caravana durante un dia en un establecimiento.

Las opciones son: 

* **fecha** fecha a consultar - formato: año-mes-dia (ejemplo 2023-03-01).
* **id collar** identificador de collar (ejemplo A12)
* **establecimiento** nombre del establecimiento en que circula el ganado (ejemplo MACSA).

## Identificadores de caravanas durante fecha en un establecimiento

Consulte identificadores de caravanas de animales durante un dia en un establecimiento.

Las opciones son: 

* **fecha** fecha a consultar - formato: año-mes-dia (ejemplo 2023-03-01).
* **establecimiento** nombre del establecimiento en que circula el ganado (ejemplo MACSA).

## Distancias recorridas por el ganado en un establecimiento

Consulte distancias diurnas, nocturnas y total recorrida por los animales durante un período de fechas en un establecimiento. El resultado esta en metros.

Las opciones son: 

* **fecha inicio** inicio de periodo a consultar - formato: año-mes-dia (ejemplo 2023-03-01).
* **fecha fin** fin de periodo a consultar - formato: año-mes-dia (ejemplo 2023-03-02)
* **establecimiento** nombre del establecimiento en que circula el ganado (ejemplo MACSA).

## Distancias de un collar durante una fecha en un establecimiento

Consulte distancias recorridas: nocturnas, diurnas y totales, de un animal con collar durante un dia en un establecimiento.

Las opciones son: 

* **fecha** fecha a consultar - formato: año-mes-dia (ejemplo 2023-03-01).
* **id collar** identificador de collar (ejemplo A12)
* **establecimiento** nombre del establecimiento en que circula el ganado (ejemplo MACSA).

## Cantidad de horas de estress calorico 

Consulte el total de horas de estress calorico (ITH mayor o igual a 75) padecido por el ganado en un establecimiento durante un lapso de tiempo.

Las opciones son: 

* **fecha inicio** inicio de periodo a consultar - formato: año-mes-dia (ejemplo 2023-03-01).
* **fecha fin** fin de periodo a consultar - formato: año-mes-dia (ejemplo 2023-03-02)
* **establecimiento** nombre del establecimiento en que circula el ganado (ejemplo MACSA).

## ITH promedio por hora

Consulte el valor de ITH promedio en cada hora durante un periodo de fechas.

Las opciones son: 

* **fecha inicio** inicio de periodo a consultar - formato: año-mes-dia (ejemplo 2023-03-01).
* **fecha fin** fin de periodo a consultar - formato: año-mes-dia (ejemplo 2023-03-02)
* **establecimiento** nombre del establecimiento en que circula el ganado (ejemplo MACSA).

## Cantidad de dias de ola de calor

Consulte cuantos dias de ola de calor (3er dia con ITH mayor o igual a 79) hubo en un establecimiento durante un periodo de fechas.

Las opciones son: 

* **fecha inicio** inicio de periodo a consultar - formato: año-mes-dia (ejemplo 2023-03-01).
* **fecha fin** fin de periodo a consultar - formato: año-mes-dia (ejemplo 2023-03-02)
* **establecimiento** nombre del establecimiento en que circula el ganado (ejemplo MACSA).

## Horas de EC por dia

Consulte cantidad de horas de estress calorico en cada dia durante un periodo de fechas en un establecimiento.

Las opciones son: 

* **fecha inicio** inicio de periodo a consultar - formato: año-mes-dia (ejemplo 2023-03-01).
* **fecha fin** fin de periodo a consultar - formato: año-mes-dia (ejemplo 2023-03-02)
* **establecimiento** nombre del establecimiento en que circula el ganado (ejemplo MACSA).


"""
tags_metadata = [
    {
        'name':'Posiciones de un collar por fecha y establecimiento',
        'description':"Admite filtros de **fecha**, **id de collar** y **establecimiento**."
    },
    {
        'name':'Identificadores de collares por fecha y establecimiento',
        'description':"Admite filtros de **fecha** y **establecimiento**."
    },
    {
        'name':'Posiciones de una caravana por fecha y establecimiento',
        'description':"Admite filtros de **fecha**, **id de collar** y **establecimiento**."
    },
    {
        'name':'Identificadores de caravanas por fecha y establecimiento',
        'description':"Admite filtros de **fecha** y **establecimiento**."
    },
    {
        'name':'Distancias recorrida por el ganado en un establecimiento',
        'description':"Admite filtros de **fecha inicio**, **fecha fin** y **establecimiento**."
    },
    {
        'name':'Distancias recorridas por un collar en un establecimiento',
        'description':"Admite filtros de **fecha**, **id de collar** y **establecimiento**."
    },
    {
        "name": "Cantidad de horas de estress calorico en establecimiento",
        "description": "Admite filtros de **fecha inicio**, **fecha fin** y **establecimiento**."
    },
    {
        "name": "ITH promedio por hora en establecimiento",
        "description": "Admite filtros de **fecha inicio**, **fecha fin** y **establecimiento**.",
    },
    {
        "name": "Cantidad de dias de ola de calor en establecimiento",
        "description": "Admite filtros de **fecha inicio**, **fecha fin** y **establecimiento**.",
    },
    {
        'name':'Horas de EC por dia en establecimiento',
        'description':"Admite filtros de **fecha inicio**, **fecha fin** y **establecimiento**."
    },
    
]

app = FastAPI(
    title="API Proyecto 1 Bastó",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Grupo 6",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)
