from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Model

ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace_name)

model = Model(path="model.pkl", name="fraud-detection-model", description="Fraud detection model")
ml_client.models.create_or_update(model)