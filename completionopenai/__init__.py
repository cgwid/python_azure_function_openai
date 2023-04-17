import logging
import openai
import json
import azure.functions as func
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

# sample request
# {"model":"text-davinci-003","prompt":"Give me a slogan for a flower company","max_tokens":"100","temperature":"0"}

# Call to Azure Key Vault
def get_openai_key():
    
    keyVaultName = os.environ.get('key_vault_name')
    KVuri = f'https://{keyVaultName}.vault.azure.net/'

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVuri, credential=credential)

    retrieved_secret = client.get_secret(os.environ.get('secret_name'))

    return retrieved_secret.value



secret_key = get_openai_key()

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # provide OpenAI with API key
    openai.api_key = secret_key

    # get params from incoming request
    req_body = req.get_json()

    # make API call to OpenAI
    result = openai.Completion.create(
        model=req_body['model'],
        prompt=req_body['prompt'],
        max_tokens=req_body['max_tokens'],
        temperature=req_body['temperature']
    )

    # format response from OpenAI to send back to client
    response_text = result.choices[0].text


    # send back response

    return func.HttpResponse(
                response_text,
                status_code=200
            )
