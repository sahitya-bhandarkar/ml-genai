import joblib
import json
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path("fraud-detection-model")
    model = joblib.load(model_path)

def run(data):
    try:
        input_data = json.loads(data)
        result = model.predict(input_data)
        return result.tolist()
    except Exception as e:
        return str(e)