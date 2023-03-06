# uvicorn main:app --reload
from fastapi import FastAPI
from model import predict
from pydantic import BaseModel
from xgboost import XGBClassifier

class Textin(BaseModel):
    album_type: str
    track_duration:int
    nombre_artist: int
    track_release_month:str
    danceability:float
    energy:float
    key: int
    loudness:float
    mode: float
    speechiness:float
    acousticness: float
    instrumentalness:float
    liveness:float
    valence: float
    tempo:float
    time_signature: float
    pays_du_producteur: str
  
    

class Prediction(BaseModel):
    popularity_Label: int
    

app = FastAPI()

@app.post("/predict", response_model=Prediction)
async def root_predict(payload : Textin):
    value = [x for x in payload.__dict__.values()]
    to_return = predict(value)
    return {"popularity_Label": to_return}