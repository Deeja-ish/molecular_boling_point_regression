from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# check the first endpoint 
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to the Molecular Property API"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "success"
    assert data['model_loaded'] is True

def test_prediction():
    # create dummy data 
    data = {
        "molecular_id" : "MOL_0002",
        "molecular_weight" : 245.7,
        "logP" : 1.67,
        "TPSA" : 3.8,
        "HBD" : 6,
        "HBA" : 7,
        "rotatable_bonds" : 6.0,
        "aromatic_rings" : 3
    }

    response = client.post("/predict", json=data)
    print(response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["molecular_id"] == "MOL_0002"
    assert 'boiling_point_c' in data

def test_prediction_error():
    data = {
        "molecular_id" : "MOL_0002",
        "molecular_weight" : -654,
        "logP" : 1.67,
        "TPSA" : 3.8,
        "HBD" : -87,
        "HBA" : -8.9,
        "rotatable_bonds" : -0,
        "aromatic_rings" : 5
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 422

# test with none values 
def test_predict_null():
    data = {
        "molecular_id" : "MOL_0002",
        "molecular_weight" : 348.7,
        "logP" : None,
        "TPSA" : None,
        "HBD" : 3,
        "HBA" : 4,
        "rotatable_bonds" : None,
        "aromatic_rings" : 5  
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    data = response.json()
    assert 'boiling_point_c' in data