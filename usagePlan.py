import boto3

# Create a boto3 client for API Gateway
apigateway = boto3.client('apigateway')

def createUsagePlan(name:str, description:str, apiStages:list, throttleSettings:dict, quotaSettings:dict):
    try:
        response = apigateway.create_usage_plan(
            name=name,
            description=description,
            apiStages=apiStages,
            throttle=throttleSettings,
            quota=quotaSettings
        )
        print("Usage Plan Created Successfully:")
        print(f"Usage Plan ID: {response['id']}")
        return response
    except Exception as e:
        print(f"Error creating usage plan: {e}")
        return None
