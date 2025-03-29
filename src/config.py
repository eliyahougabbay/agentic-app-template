import os

import logfire
from openai import AsyncAzureOpenAI
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# Set Jaeger tracing endpoint (HTTP)
traces_endpoint = "http://jaeger:4318/v1/traces"
os.environ["OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"] = traces_endpoint

# Configure logfire for tracing/logging
logfire.configure(
    service_name="my_logfire_service",
    send_to_logfire=False,
)

# Enable instrumentation for all agents
Agent.instrument_all()

# Retrieve environment variables
api_key = os.environ.get("AZURE_API_KEY")
azure_endpoint = os.environ.get("AZURE_ENDPOINT")
api_version = os.environ.get("AZURE_API_VERSION")
azure_model = os.environ.get("AZURE_MODEL_ID")

# Initialize the Azure OpenAI client and model
openai_client = AsyncAzureOpenAI(
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version,
)

openai_model = OpenAIModel(azure_model, openai_client=openai_client)
