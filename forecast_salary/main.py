from fastapi import FastAPI
from forecast_salary.functions import model_xgboost, model_predict
from forecast_salary.models import Payload


app = FastAPI()

model_xg, mape_xg = model_xgboost(0)

@app.post("/model_xg/")
async def model_predict_xg(payload: Payload) -> dict:
    pred_valor = await model_predict(payload, model_xg)

    return {'valor': pred_valor,
            'valor_min': round(pred_valor*(1-mape_xg), ndigits=2),
            'valor_max': round(pred_valor*(1+mape_xg), ndigits=2),
            }