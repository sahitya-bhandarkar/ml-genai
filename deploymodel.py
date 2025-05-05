from azure.ai.ml.entities import Environment, InferenceConfig, OnlineEndpoint, OnlineDeployment

env = Environment(name="inference-env", conda_file="conda.yml")

inference_config = InferenceConfig(entry_script="score.py", environment=env)

endpoint = OnlineEndpoint(name="fraud-detection-endpoint")
deployment = OnlineDeployment(name="fraud-detection-deployment", model=model, endpoint=endpoint, inference_config=inference_config)

ml_client.online_endpoints.create_or_update(endpoint)
ml_client.online_deployments.create_or_update(deployment)