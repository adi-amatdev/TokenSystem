
# `tokenFuncs.py`

This script provides functions to manage API keys in AWS API Gateway. It allows you to create, associate, and delete API keys, as well as link them to a usage plan.

## Prerequisites

- **AWS SDK for Python (Boto3)**: Ensure that `boto3` is installed and configured with the necessary permissions to manage API keys and usage plans in API Gateway.
- **AWS Credentials**: The script uses your AWS credentials, so make sure they are configured properly.

## Dependencies

Install the required package by running:

```bash
pip install boto3
```

## Usage

### Function: `createApiKey`

#### Description

This function creates an API key in AWS API Gateway.

#### Parameters

- `name` (`str`): The name of the API key.
- `enabled` (`bool`): A boolean flag to enable or disable the API key.

#### Returns

- `apiKeyID` (`str`): The ID of the created API key.
- `apiKeyValue` (`str`): The value of the created API key.

#### Example

```python
apiKeyID, apiKeyValue = createApiKey("MyAPIKey", enabled=True)
```

---

### Function: `associateApiKeyWithUsagePlanID`

#### Description

This function associates an existing API key with a specified usage plan in AWS API Gateway.

#### Parameters

- `apiKeyID` (`str`): The ID of the API key to associate.
- `usagePlanID` (`str`): The ID of the usage plan to associate the API key with.

#### Returns

- `response` (`dict`): The response dictionary from the API Gateway.

#### Example

```python
response = associateApiKeyWithUsagePlanID(apiKeyID="12345", usagePlanID="67890")
```

---

### Function: `createToken`

#### Description

This function creates an API key and associates it with a usage plan.

#### Parameters

- `macId` (`str`): The name or identifier for the API key.
- `upi` (`str`): The ID of the usage plan.
- `enabled` (`bool`, optional): A boolean flag to enable or disable the API key (default is `True`).

#### Returns

- `response` (`dict`): The response dictionary from the API Gateway after the API key is associated with the usage plan.

#### Example

```python
response = createToken(macId="Device1", upi="UsagePlanID")
```

---

### Function: `deleteToken`

#### Description

This function deletes an API key based on its name.

#### Parameters

- `macId` (`str`): The name or identifier for the API key to be deleted.

#### Returns

- `True`: If the API key is deleted successfully.
- `False`: If the API key could not be deleted due to an error.

#### Example

```python
success = deleteToken(macId="Device1")
```

#### Output

If the API key is deleted successfully, you will see the following output:

```
API Key 'Device1' deleted successfully.
```

In case of an error, the script will print the error message.

## License

This code is provided as-is without any warranty. You are free to use and modify it according to your needs.
```

This documentation explains how to use the various functions within the `api_key_manager.py` script to manage API keys in AWS API Gateway.
