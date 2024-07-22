import boto3

apigateway = boto3.client('apigateway')

# Function to create an API key in API Gateway
def createApiKey(name:str, enabled:bool):
    response = apigateway.create_api_key(
        name=name,
        enabled=enabled
    )
    return response['id'], response['value']


# Function to associate an API key with a usage plan

def associateApiKeyWithUsagePlanID(apiKeyID:str, usagePlanID:str):
    response = apigateway.create_usage_plan_key(
        usagePlanId=usagePlanID,
        keyId=apiKeyID,
        keyType='API_KEY'
    )
    return response

def createToken(macId:str , upi:str,enabled=True):
    apiKeyID, apiKeyValue = createApiKey(macId, enabled)
    resp = associateApiKeyWithUsagePlanID(apiKeyID, upi)
    return resp

def deleteToken(macId:str):
    try:
        # Get API keys
        response = apigateway.get_api_keys(nameQuery=macId, includeValues=False)
        # Extract API key ID
        apiKeyID = response['items'][0]['id']

        # Delete API key
        apigateway.delete_api_key(apiKey=apiKeyID)
        print(f"API Key '{macId}' deleted successfully.")
        return True

    except apigateway.exceptions.BadRequestException as e:
        print(f"Failed to delete API key: {e}")
        return False
