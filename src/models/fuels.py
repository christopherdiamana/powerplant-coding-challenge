from pydantic import BaseModel, Field
from src.staticsNames import *


class Fuels(BaseModel):
    gas_euro_per_MWh: float = Field(alias=FUEL_GAS)
    kerosine_euro_per_MWh: float = Field(alias=FUEL_KEROSINE)
    co2_euro_per_ton: float = Field(alias=FUEL_CO2)
    wind_percentage: float = Field(alias=FUEL_WIND)

