### Documentation for: `TokenManager`, `UsagePlanManager`, and `UserManager`

This documentation outlines the implementation of the `TokenManager`, `UsagePlanManager`, and `UserManager` classes used for managing tokens, usage plans, and user authentication in a cloud-based environment. The classes utilize functions from `tokenFuncs`, `usagePlan`, and `DatabaseOps` modules to interact with the backend services.

### 1. Imports and Environment Setup

```python
from tokenFuncs import createToken, deleteToken
from usagePlan import createUsagePlan
from DatabaseOps import DatabaseOps
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

```

- **`load_dotenv()`**: Loads environment variables from a `.env` file, which are used for configuration purposes.
- **Environment Variables**:
    - `APIID`: The API ID for usage plans.
    - `STAGE`: The stage of the API.
- The above will be available in `AWS API GATEWAY` console, under the concerened REST API.
    - For Example:

    ```bash
    APIID = "f6voilnlr2"
    STAGE = "dev"
    ```


### 2. `TokenManager` Class

The `TokenManager` class provides methods for creating, deleting, and fetching tokens associated with devices identified by MAC addresses.

- **Initialization:**

    ```python
    databaseOpsManager = DatabaseOps()

    class TokenManager:
        def __init__(self):
            pass

    ```

- **`createTokenHandler(macId: str, upi: str)` Method:**
    - **Purpose**: Creates a token associated with a specific MAC ID and usage plan ID (UPI).
    - **Process**:
        1. Checks if the token already exists using `databaseOpsManager.checkTokenExists(macId)`.
        2. Calls `createToken(macId, upi)` to create the token via AWS.
        3. If successful, stores token information in the database.
    - **Returns**: A dictionary with a status code and message.
- **`createBulkTokenHandler(macIdList: list, upi: str)` Method:**
    - **Purpose**: Creates tokens for multiple MAC IDs in bulk.
    - **Process**:
        1. Iterates through the list of MAC IDs.
        2. Calls `createTokenHandler(macId, upi)` for each MAC ID.
        3. Collects and returns a response with the status of token creation for each MAC ID.
- **`deleteTokenHandler(macId: str)` Method:**
    - **Purpose**: Deletes a token associated with a specific MAC ID.
    - **Process**:
        1. Checks if the token exists.
        2. Calls `deleteToken(macId)` to remove the token via AWS.
        3. Deletes the token information from the database if successful.
    - **Returns**: A dictionary with a status code and message.
- **`deleteBulkTokenHandler(macIdList: list)` Method:**
    - **Purpose**: Deletes tokens for multiple MAC IDs in bulk.
    - **Process**: Similar to `createBulkTokenHandler`, but for deletion.
    - **Returns**: A response dictionary indicating the status of token deletion for each MAC ID.
- **`sensorFetchHandler(macId: str)` Method:**
    - **Purpose**: Fetches the token associated with a specific MAC ID.
    - **Process**: Checks if the token exists and retrieves it from the database.
    - **Returns**: A dictionary with the status and token information.
- **`fetchSensorListHandler()` Method:**
    - **Purpose**: Fetches a list of all MAC IDs in the database.
    - **Returns**: A list of MAC IDs.

### 3. `UsagePlanManager` Class

The `UsagePlanManager` class provides methods for creating and fetching usage plans for tokens.

- **Initialization:**

    ```python
    class UsagePlanManager:
        def __init__(self) -> None:
            pass

    ```

- **`createUsagePlanHandler(batchName, description, burstLimit, rateLimit, quotaLimit, period)` Method:**
    - **Purpose**: Creates a usage plan with specific limits and associates it with an API.
    - **Process**:
        1. Checks if a batch name already exists.
        2. Validates the provided period against allowed values (`DAY`, `WEEK`, `MONTH`).
        3. Constructs the API stage and quota settings.
        4. Calls `createUsagePlan()` to create the usage plan via AWS.
        5. Stores the usage plan information in the database if successful.
    - **Returns**: A dictionary with a status code and message.
- **`fetchUsagePlansHandler()` Method:**
    - **Purpose**: Fetches all usage plans from the database.
    - **Returns**: A list of usage plans.

### 4. `UserManager` Class

The `UserManager` class provides methods for managing user accounts, including creating users, deleting users, fetching user details, and updating roles.

- **Initialization:**

    ```python
    class UserManager:
        def __init__(self) -> None:
            self.validRoles = ['USER','MANAGER','ADMIN']

    ```

- **`createUser(username: str, password: str, role: str)` Method:**
    - **Purpose**: Creates a new user with the specified role.
    - **Process**:
        1. Validates the role against allowed values.
        2. Checks if the username is available.
        3. Calls `databaseOpsManager.createUser()` to create the user in the database.
    - **Returns**: A dictionary with a status code and message.
- **`deleteUser(username: str)` Method:**
    - **Purpose**: Deletes a user by username.
    - **Process**: Checks if the user exists and deletes the user if found.
    - **Returns**: A dictionary with a status code and message.
- **`fetchUsers()` Method:**
    - **Purpose**: Fetches all users from the database.
    - **Returns**: A list of users.
- **`fetchUserLogin(username: str)` Method:**
    - **Purpose**: Fetches the login details for a specific user.
    - **Process**: Checks if the user exists and retrieves the user details if found.
    - **Returns**: A dictionary with status and user details.
- **`updateRole(username: str, role: str)` Method:**
    - **Purpose**: Updates the role of a specific user.
    - **Process**: Validates the role and updates it in the database.
    - **Returns**: A dictionary with a status code and message.
