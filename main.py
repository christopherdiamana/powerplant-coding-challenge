from fastapi import FastAPI
from src.models.payload import Payload
from src.models.powerplantResponse import PowerplantResponse
from src.productionPlan import ProductionPlan


app = FastAPI()


@app.post("/productionplan", response_model=list[PowerplantResponse])
async def create_production_plan(item: Payload):
    plan = ProductionPlan(item)
    return plan.production_plan()


@app.get("/")
async def root():
    return {"message": "Hello World"}

