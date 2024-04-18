import pandas as pd
from src.models.payload import Payload


class ProductionPlan():
    def __init__(self, payload: Payload):
        self.payload = payload
        self.df_powerplants = self.get_df_powerplants()

    def get_df_powerplants(self):
        powerplant_dicts = [powerplant.dict() for powerplant in self.payload.powerplants]
        dataframe = pd.DataFrame(powerplant_dicts)
        return dataframe



