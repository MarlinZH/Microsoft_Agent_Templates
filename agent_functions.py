# Add references
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FunctionTool, ToolSet
# from user_functions import user_functions --Data to feed to the Agent


# Connect to the Azure AI Foundry project
project_client = AIProjectClient.from_connection_string(
     credential=DefaultAzureCredential
         (exclude_environment_credential=True,
          exclude_managed_identity_credential=True),
     conn_str=PROJECT_CONNECTION_STRING
)

# Get a chat client
chat = projectClient.inference.get_chat_completions_client()

# Initialize prompt with system message
prompt=[
         SystemMessage("You are a helpful AI assistant that answers questions.")
     ]