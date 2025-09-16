# microsoft_agent_templates and boilerplate
Repository of Templates from Microsoft Learning for future projects

Portals:
Azure AI Foundry portal: https://ai.azure.com

Variables
    Azure AI Foundry resource: A valid name for your Azure AI Foundry resource
    Subscription: Your Azure subscription
    Resource group: Create or select a resource group
    Region: Select any AI Services supported location*
    

    -------

    rm -r mslearn-ai-foundry -f
    git clone https://github.com/microsoftlearning/mslearn-ai-studio mslearn-ai-foundry
    cd mslearn-ai-foundry/labfiles/chat-app/python

    python -m venv labenv
    ./labenv/bin/Activate.ps1
    pip install python-dotenv azure-identity azure-ai-projects azure-ai-inference
