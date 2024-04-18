from pydantic import BaseModel


class PowerplantResponse(BaseModel):
    name: str
    p: float
