# `databaseOps.py`

This script provides various operations to interact with a PostgreSQL database, specifically for managing tokens, usage plans, and user information. It uses the `psycopg2` library to connect and execute queries on the database.

## Prerequisites

- **Python Libraries**:
  - `psycopg2`: Ensure that the `psycopg2` library is installed for PostgreSQL database interactions.
  - `dotenv`: Used to load environment variables from a `.env` file.
  - `os`: Used to access environment variables.
  - `datetime`: Used for handling date and time objects.
  
- **Environment Variables**: The script expects the following environment variables to be set:
  - `DATABASE_NAME`
  - `USERNAME`
  - `PASSWORD`
  - `HOST`
  - `PORT`

## Dependencies

Install the required packages by running:

```bash
pip install psycopg2 python-dotenv
```

## Class: `DatabaseOps`

The `DatabaseOps` class encapsulates all database operations.

### Method: `connectDB()`

#### Description

Connects to the PostgreSQL database using the credentials provided in the environment variables.

#### Returns

- `conn`: The connection object to the PostgreSQL database.
- `cur`: The cursor object to interact with the database.

---

### Method: `saveTokenInfo`

#### Description

Inserts token information into the `aams_tokens.tokenInfo` table.

#### Parameters

- `macId` (`str`): The MAC address identifier.
- `enabled` (`bool`): Whether the token is enabled.
- `usagePlanID` (`str`): The ID of the usage plan.
- `apiKeyValue` (`str`): The API key value.
- `createdTimeStamp` (`datetime`): The timestamp of when the token was created.
- `activated` (`int`): The activation count of the token.

#### Returns

- `None`

---

### Method: `insertUsagePlan`

#### Description

Inserts usage plan information into the `aams_tokens.usagePlan` table.

#### Parameters

- `batchName` (`str`): The batch identifier.
- `usagePlanID` (`str`): The ID of the usage plan.
- `burstLimit` (`int`): The burst limit.
- `rateLimit` (`int`): The rate limit.
- `quotaLimit` (`int`): The quota limit.
- `period` (`str`): The period of the quota.
- `timeStamp` (`datetime`): The timestamp of when the usage plan was created.
- `activated` (`bool`): Whether the usage plan is activated.

#### Returns

- `None`

---

### Method: `deleteTokenInfo`

#### Description

Deletes token information from the `aams_tokens.tokenInfo` table based on the provided MAC address.

#### Parameters

- `macId` (`str`): The MAC address identifier.

#### Returns

- `None`

---

### Method: `checkTokenExists`

#### Description

Checks if a token exists in the `aams_tokens.tokenInfo` table based on the provided MAC address.

#### Parameters

- `macId` (`str`): The MAC address identifier.

#### Returns

- `exists` (`bool`): `True` if the token exists, otherwise `False`.

---

### Method: `batchExists`

#### Description

Checks if a batch exists in the `aams_tokens.usagePlan` table based on the provided batch name.

#### Parameters

- `batchName` (`str`): The batch identifier.

#### Returns

- `result` (`bool`): `True` if the batch exists, otherwise `False`.

---

### Method: `sensorFetch`

#### Description

Fetches the API key value associated with the provided MAC address from the `aams_tokens.tokenInfo` table. Also increments the `activated` count for the token.

#### Parameters

- `macId` (`str`): The MAC address identifier.

#### Returns

- `api_key_value` (`str`): The API key value if found, otherwise `None`.

---

### Method: `fetchAllMacIds`

#### Description

Fetches all MAC IDs and their corresponding activated values from the `aams_tokens.tokenInfo` table.

#### Returns

- `results` (`list` of `tuple`): A list of tuples containing `mac_id` and `activated` values.

---

### Method: `fetchAllUsagePlans`

#### Description

Fetches all batch IDs and usage plan IDs from the `aams_tokens.usagePlan` table.

#### Returns

- `results` (`list` of `tuple`): A list of tuples containing `batch_id` and `usage_plan_id` values.

---

### Method: `createUser`

#### Description

Inserts a new user into the `aams_tokens.users` table.

#### Parameters

- `username` (`str`): The username.
- `password` (`str`): The password.
- `role` (`str`): The role of the user.

#### Returns

- `success` (`bool`): `True` if the user was created successfully, otherwise `False`.

---

### Method: `deleteUser`

#### Description

Deletes a user from the `aams_tokens.users` table based on the provided username.

#### Parameters

- `username` (`str`): The username.

#### Returns

- `success` (`bool`): `True` if the user was deleted successfully, otherwise `False`.

---

### Method: `userExists`

#### Description

Checks if a user exists in the `aams_tokens.users` table based on the provided username.

#### Parameters

- `username` (`str`): The username.

#### Returns

- `result` (`bool`): `True` if the user exists, otherwise `False`.

---

### Method: `fetchAllUsers`

#### Description

Fetches all usernames and their corresponding roles from the `aams_tokens.users` table.

#### Returns

- `results` (`list` of `tuple`): A list of tuples containing `username` and `role` values.

---

### Method: `fetchUser`

#### Description

Fetches the username, password, and role of a user from the `aams_tokens.users` table based on the provided username.

#### Parameters

- `username` (`str`): The username.

#### Returns

- `result` (`tuple`): A tuple containing `username`, `password`, and `role` if found, otherwise `None`.

---

### Method: `updateRole`

#### Description

Updates the role of a user in the `aams_tokens.users` table based on the provided username.

#### Parameters

- `username` (`str`): The username.
- `role` (`str`): The new role.

#### Returns

- `success` (`bool`): `True` if the role was updated successfully, otherwise `False`.
```

This documentation details each method in the `databaseOps.py` file, describing the purpose, parameters, and return values of each method.