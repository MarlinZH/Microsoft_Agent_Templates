import os

# Add references
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FunctionTool, ToolSet
# from user_functions import user_functions --Data to feed to the Agent


def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        project_connection = os.getenv("PROJECT_ENDPOINT")
        model_deployment =  os.getenv("MODEL_DEPLOYMENT")
        
        # Initialize the project client
          # Connect to the Azure AI Foundry project
          project_client = AIProjectClient.from_connection_string(
               credential=DefaultAzureCredential
               (exclude_environment_credential=True,
                    exclude_managed_identity_credential=True),
               conn_str=PROJECT_CONNECTION_STRING
          )

        ## Get a chat client
        chat = projectClient.inference.get_chat_completions_client()

        # Initialize prompt with system message
          prompt=[
               SystemMessage("You are a helpful AI assistant that answers questions.")
               ]

               

        # Loop until the user types 'quit'
        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue
            
                 # Get a chat completion
               prompt.append(UserMessage(input_text))
               response = chat.complete(
                    model=model_deployment,
                    messages=prompt)
               completion = response.choices[0].message.content
               print(completion)
               prompt.append(AssistantMessage(completion))


    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()



          





