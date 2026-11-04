#  import the packages
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional
import joblib 
import pandas as pd 

app = FastAPI(
    title="BolingPoint predictor",
    description="This is a simple FastAPI app that can predicte the boling point of molecules base on their features of the molecule using Ridge regression"
)

# import the scaler and the model 
model_pipeline = joblib.load("models/model_pipeline.pkl")

# create the columns
FEATURE_COLUMNS = [
    "molecular_weight",
    "logP",
    "TPSA",
    "HBD",
    "HBA",
    "rotatable_bonds",
    "aromatic_rings"
]

# create a class of the input parameters
class ModelParameters(BaseModel):
    molecular_id : str = Field(examples=['MOL_001']) 
    molecular_weight : float =Field(examples=[238.90], ge=0)
    logP : Optional[float] = Field(examples=[1.89])
    TPSA : Optional[float] = Field(examples=[67.89])
    HBD : int = Field(examples=[5], ge=0)
    HBA : int = Field(examples=[8], ge=0)
    rotatable_bonds : Optional[int] = Field(examples=[6], ge=0)
    aromatic_rings : int = Field(examples=[3], ge=0)


# create the home endpoint
@app.get("/")
def get_home():
    return "Welcome to the Molecular Property API"

# create the health check endpoint
@app.get("/health")
def check_health():
    return {
        "status" : "success",
        "message" : "Model Loaded Successfully",
        "model_loaded" : True
    }

# Create the predict endpoiny
@app.post("/predict")
def predict_boling_point(data : ModelParameters):
    try:
        input_data = data.model_dump()
        molecular_id = input_data.pop("molecular_id")

        # predict the data 
        dataframe = pd.DataFrame([input_data])
        dataframe = dataframe[FEATURE_COLUMNS]
        prediction = model_pipeline.predict(dataframe)[0]

        return {
            "status" : "success",
            "molecular_id" : molecular_id,
            "boiling_point_c" : prediction
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(e)
        )
    

    