import joblib
import json
import os

def init():
    global model
    # Load the model from the path provided by the environment variable
    model_path = os.getenv("AZUREML_MODEL_DIR") + "/model.pkl"
    model = joblib.load(model_path)

def run(data):
    try:
        # Parse the input data
        input_data = json.loads(data)
        # Perform prediction
        result = model.predict(input_data)
        return {"predictions": result.tolist()}
    except Exception as e:
        return {"error": str(e)}