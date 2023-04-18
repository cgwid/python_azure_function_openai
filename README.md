# python_azure_function_openai

Azure function written with Python that calls OpenAI with model, prompt, max_tokens, and temperature and returns the results as a text string. 
The API call to the azure function can be incorporated into any type of application. Pass the same parameters (model, prompt, max_tokens, and temperature)
when calling the azure function which will pass it to OpenAI call. The API key for OpenAI is stored in Azure Key Vault

# Setup:
1) Need a Microsoft Azure Subscription
2) Create a resource group to contain the things below:
3) Need an Azure Function app within the resource group
4) Need an Azure storage account 
5) Need an Azure Key Vault
6) To connect the Azure Key Vault with the Function App --> go to the function app --> settings --> Identity --> Toggle Managed Identity "On"
7) Go to Azure Key Vault --> Access Policies --> Create a new policy for the Function App