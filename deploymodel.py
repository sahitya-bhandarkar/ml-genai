import json
from azure.ai.ml import MLClient
from azure.ai.ml.entities import ManagedOnlineEndpoint, ManagedOnlineDeployment, Model, Environment
from azure.identity import DefaultAzureCredential
import uuid  # To generate a unique endpoint name if needed

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

subscription_id = config["subscription_id"]
resource_group = config["resource_group"]
workspace_name = config["workspace_name"]

# Initialize MLClient
ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace_name)

# Define the environment
env = Environment(
    name="fraud-detection-env",
    image="mcr.microsoft.com/azureml/minimal-ubuntu18.04-py37-cpu-inference:latest",
    conda_file="conda.yml"
)

# Define the endpoint
endpoint_name = "fraud-detection-endpoint"  # Ensure this is unique in your workspace
endpoint = ManagedOnlineEndpoint(
    name=endpoint_name,
    auth_mode="key"  # You can also use "aml_token" if preferred
)

# Create the endpoint
print(f"Creating endpoint: {endpoint_name}")
ml_client.online_endpoints.begin_create_or_update(endpoint).wait()

# Define the deployment
deployment = ManagedOnlineDeployment(
    name="fraud-detection-deployment",
    endpoint_name=endpoint_name,
    model=ml_client.models.get(name="fraud-detection-model", label="latest"),
    environment=env,
    instance_type="Standard_DS3_v2",
    instance_count=1
)

# Deploy the model
print(f"Deploying model to endpoint: {endpoint_name}")
ml_client.online_deployments.begin_create_or_update(deployment).wait()