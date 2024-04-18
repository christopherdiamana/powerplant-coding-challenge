import pandas as pd
from src.models.payload import Payload
from src.staticsNames import *


class ProductionPlan():
    def __init__(self, payload: Payload):
        self.payload = payload
        self.df_powerplants = self.get_df_powerplants()

    def get_df_powerplants(self):
        powerplant_dicts = [powerplant.dict() for powerplant in self.payload.powerplants]
        dataframe = pd.DataFrame(powerplant_dicts)
        return dataframe

    def calculate_cost(self, row):
        if "wind" in row.type:
            cost = 0
        elif "gas" in row.type:
            cost_euro_mwh = self.payload.fuels.gas_euro_per_MWh
            cost = cost_euro_mwh * (1 - row['efficiency'])
        elif "turbojet" == row.type:
            cost_euro_mwh = self.payload.fuels.kerosine_euro_per_MWh
            cost = cost_euro_mwh * (1 - row['efficiency'])
        else:
            cost = -1

        return cost

    def apply_merit_order(self):
        self.df_powerplants['cost'] = self.df_powerplants.apply(self.calculate_cost, axis=1)
        self.df_powerplants.sort_values(by='cost', ascending=True, inplace=True)
        self.df_powerplants.reset_index(inplace=True)

    def apply_wind_conditions(self):
        wind_conditions = self.payload.fuels.wind_percentage
        wind_powerplants = self.df_powerplants["type"] == "windturbine"

        pmax = round((wind_conditions / 100) * self.df_powerplants.loc[wind_powerplants, 'pmax'], 1)
        self.df_powerplants.loc[wind_powerplants, 'pmax'] = pmax

        pmin = round((wind_conditions / 100) * self.df_powerplants.loc[wind_powerplants, 'pmin'], 1)
        self.df_powerplants.loc[wind_powerplants, 'pmin'] = pmin

    def production_plan(self):
        self.apply_merit_order()
        self.apply_wind_conditions()

        response = []
        load = self.payload.load
        for index, powerplant in self.df_powerplants.iterrows():
            power_production = min(powerplant['pmax'], load) if load >= powerplant['pmin'] else 0.0
            response.append({"name": powerplant['name'], "p": power_production})
            load -= power_production

        return response


