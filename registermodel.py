# filepath: /workspaces/ml-genai/registermodel.py
import json
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Model

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

subscription_id = config["subscription_id"]
resource_group = config["resource_group"]
workspace_name = config["workspace_name"]

# Initialize MLClient
ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace_name)

# Define and register the model
model = Model(path="model.pkl", name="fraud-detection-model", description="Fraud detection model")
ml_client.models.create_or_update(model)