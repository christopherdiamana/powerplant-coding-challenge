from pydantic import BaseModel
from src.models.powerplant import Powerplant
from src.models.fuels import Fuels


class Payload(BaseModel):
    load: int
    fuels: Fuels
    powerplants: list[Powerplant]

