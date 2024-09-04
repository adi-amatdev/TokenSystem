# `usageplan.py`

This script is designed to interact with AWS API Gateway to create a usage plan using the `boto3` library.

## Prerequisites

- **AWS SDK for Python (Boto3)**: Ensure that `boto3` is installed and configured with the necessary permissions to create usage plans in API Gateway.
- **AWS Credentials**: The script uses your AWS credentials, so make sure they are configured properly.

## Dependencies

Install the required package by running:

```bash
pip install boto3

```

## Usage

### Function: `createUsagePlan`

### Description

This function creates a usage plan in AWS API Gateway.

### Parameters

- `name` (`str`): The name of the usage plan.
- `description` (`str`): A description of the usage plan.
- `apiStages` (`list`): A list of API stages to associate with the usage plan. Each item in the list should be a dictionary with keys like `apiId` and `stage`.
- `throttleSettings` (`dict`): A dictionary specifying the request throttling limits, typically including `rateLimit` and `burstLimit`.
- `quotaSettings` (`dict`): A dictionary specifying the request quota limits, typically including `limit`, `period`, and `offset`.

### Returns

- On success: Returns the response dictionary containing the usage plan details, including the `Usage Plan ID`.
- On failure: Returns `None` and prints an error message.

### Example

```python
import boto3

# Create a boto3 client for API Gateway
apigateway = boto3.client('apigateway')

def createUsagePlan(name, description, apiStages, throttleSettings, quotaSettings):
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

# Example usage
response = createUsagePlan(
    name="MyUsagePlan",
    description="A usage plan for my API",
    apiStages=[{"apiId": "abcd1234", "stage": "prod"}],
    throttleSettings={"rateLimit": 100, "burstLimit": 200},
    quotaSettings={"limit": 1000, "period": "MONTH", "offset": 0}
)

```
