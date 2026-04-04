from fastapi import FastAPI
from pydantic import BaseModel
from logic import predict, undo, reset

app = FastAPI()

class PredictRequest(BaseModel):
    player: list[str]
    banker: list[str]

@app.post("/predict")
def predict_api(req: PredictRequest):
    return predict({"player": req.player, "banker": req.banker})

@app.post("/undo")
def undo_api():
    return undo()

@app.post("/reset")
def reset_api():
    return reset()

@app.get("/meta")
def meta():
    return {"version": "1.0.0", "status": "ok"}
