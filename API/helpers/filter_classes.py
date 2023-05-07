from pydantic import BaseModel
from typing import Optional
from datetime import date

class FiltroFechasEstablecimiento(BaseModel):
	start_date: str="2023-03-01"
	end_date: str="2023-03-02"
	settlement: str="MACSA"
	
