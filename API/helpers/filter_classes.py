from pydantic import BaseModel
from typing import Optional
from datetime import date

class FiltroFechasEstablecimiento(BaseModel):
	start_date: str="2023-03-01"
	end_date: str="2023-03-02"
	settlement: str="MACSA"
	
class FiltroDiaEstablecimientoGpsId(BaseModel):
	date: str="2023-03-02"
	settlement: str="MACSA"
	gpsId: str='0004A30B00F89C5D'

class FiltroDiaEstablecimiento(BaseModel):
	date: str="2023-03-02"
	settlement: str="MACSA"

class FiltroDiaEstablecimientoBeaconId(BaseModel):
	date: str="2023-03-02"
	settlement: str="MACSA"
	beaconId: str='07FDB1987FEB'
