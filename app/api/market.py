from fastapi import APIRouter
from app.services.market_service import predict,history,recommendation,top,forecast,profit

router=APIRouter()

@router.get("/market/predict")
def p(crop:str): return predict(crop)

@router.get("/market/history")
def h(crop:str): return history(crop)

@router.get("/market/recommendation")
def r(crop:str): return recommendation(crop)

@router.get("/market/top")
def t(crop:str): return top(crop)

@router.get("/market/forecast")
def f(crop:str): return forecast(crop)

@router.get("/market/profit")
def pf(crop:str,quantity:float): return profit(crop,quantity)
