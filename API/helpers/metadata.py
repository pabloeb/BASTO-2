from fastapi import FastAPI

description = """

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
        "name": "Cantidad de horas de estress calorico",
        "description": "Admite filtros de **fecha inicio**, **fecha fin** y **establecimiento**."
    },
    {
        "name": "ITH promedio por hora",
        "description": "Admite filtros de **fecha inicio**, **fecha fin** y **establecimiento**.",
    },
    {
        "name": "Cantidad de dias de ola de calor",
        "description": "Admite filtros de **fecha inicio**, **fecha fin** y **establecimiento**.",
    },
    {
        'name':'Horas de EC por dia',
        'description':"Admite filtros de **fecha inicio**, **fecha fin** y **establecimiento**."
    }
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
