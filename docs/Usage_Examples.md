## Usage Examples for Token Manager API

### 1. Create a Single Token

- **Endpoint:** `POST /create_token`
- **Description:** Creates a new token associated with a specific MAC ID and UPI.
- **Headers:**
  - `Authorization: Bearer <JWT_TOKEN>`
- **Request Body:**
  ```json
  {
    "macId": "14",
    "upi": "6ueroe"
  }
  ```
- **Example Request:**
  ```
  POST http://127.0.0.1:5000/create_token
  Authorization: Bearer <JWT_TOKEN>
  Content-Type: application/json

  {
    "macId": "14",
    "upi": "6ueroe"
  }
  ```
- **Expected Response:**
  ```json
  {
    "message": "Token Created and associated with usage plan"
  }
  ```

### 2. Create Tokens in Bulk

- **Endpoint:** `POST /create_tokens_bulk/{usagePlan}`
- **Description:** Creates tokens in bulk by uploading a CSV file containing `macId`s.
- **Headers:**
  - `Authorization: Bearer <JWT_TOKEN>`
- **Request Body:**
  - Form Data:
    - `csv_file`: The CSV file containing the MAC IDs to create tokens for.
- **Example Request:**
  ```
  POST http://127.0.0.1:5000/create_tokens_bulk/ngmvnl
  Authorization: Bearer <JWT_TOKEN>
  Content-Type: multipart/form-data

  [Upload CSV file containing MAC IDs]
  ```
- **Expected Response:**
  ```json
  {
    "message": "all tokens successfully created"
  }
  ```

### 3. Delete a Single Token

- **Endpoint:** `DELETE /delete_token`
- **Description:** Deletes an existing token associated with a specific MAC ID.
- **Headers:**
  - `Authorization: Bearer <JWT_TOKEN>`
- **Request Body:**
  ```json
  {
    "macId": "14"
  }
  ```
- **Example Request:**
  ```
  DELETE http://127.0.0.1:5000/delete_token
  Authorization: Bearer <JWT_TOKEN>
  Content-Type: application/json

  {
    "macId": "14"
  }
  ```
- **Expected Response:**
  ```json
  {
    "message": "deleted token successfully"
  }
  ```

### 4. Delete Tokens in Bulk

- **Endpoint:** `DELETE /delete_tokens_bulk`
- **Description:** Deletes tokens in bulk by uploading a CSV file containing `macId`s.
- **Headers:**
  - `Authorization: Bearer <JWT_TOKEN>`
- **Request Body:**
  - Form Data:
    - `csv_file`: The CSV file containing the MAC IDs to delete tokens for.
- **Example Request:**
  ```
  DELETE http://127.0.0.1:5000/delete_tokens_bulk
  Authorization: Bearer <JWT_TOKEN>
  Content-Type: multipart/form-data

  [Upload CSV file containing MAC IDs]
  ```
- **Expected Response:**
  ```json
  {
    "message": "all tokens deleted successfully"
  }
  ```

### 5. Fetch All Sensors

- **Endpoint:** `GET /sensor_list`
- **Description:** Retrieves a list of all sensors and their activation statuses.
- **Headers:**
  - `Authorization: Bearer <JWT_TOKEN>`
- **Example Request:**
  ```
  GET http://127.0.0.1:5000/sensor_list
  Authorization: Bearer <JWT_TOKEN>
  ```
- **Expected Response:**
  ```json
  {
    "14": 0,
    "15": 1,
    // more macId and activation status pairs
  }
  ```

### 6. Fetch Token for a Sensor

- **Endpoint:** `GET /sensor_fetch`
- **Description:** Retrieves the token associated with a specific MAC ID.
- **Headers:**
  - `Authorization: Bearer <JWT_TOKEN>`
- **Request Body:**
  ```json
  {
    "macId": "12345"
  }
  ```
- **Example Request:**
  ```
  GET http://127.0.0.1:5000/sensor_fetch
  Authorization: Bearer <JWT_TOKEN>
  Content-Type: application/json

  {
    "macId": "12345"
  }
  ```
- **Expected Response:**
  ```json
  {
    "token": "abc123xyz"
  }
  ```

### 7. Create a Usage Plan

- **Endpoint:** `POST /create_usage_plan`
- **Description:** Creates a new usage plan for API Gateway.
- **Headers:**
  - `Authorization: Bearer <JWT_TOKEN>`
- **Request Body:**
  ```json
  {
    "name": "Monthly Plan",
    "description": "Monthly usage plan for API Gateway",
    "burst_limit": 100,
    "rate_limit": 10,
    "quota_limit": 1000,
    "period": "MONTH"
  }
  ```
- **Example Request:**
  ```
  POST http://127.0.0.1:5000/create_usage_plan
  Authorization: Bearer <JWT_TOKEN>
  Content-Type: application/json

  {
    "name": "Monthly Plan",
    "description": "Monthly usage plan for API Gateway",
    "burst_limit": 100,
    "rate_limit": 10,
    "quota_limit": 1000,
    "period": "MONTH"
  }
  ```
- **Expected Response:**
  ```json
  {
    "message": "Usage Plan Created"
  }
  ```

### 8. Fetch All Usage Plans

- **Endpoint:** `GET /fetch_usage_plans`
- **Description:** Retrieves all usage plans.
- **Headers:**
  - `Authorization: Bearer <JWT_TOKEN>`
- **Example Request:**
  ```
  GET http://127.0.0.1:5000/fetch_usage_plans
  Authorization: Bearer <JWT_TOKEN>
  ```
- **Expected Response:**
  ```json
  {
    "Monthly Plan": "ngmvnl",
    "Weekly Plan": "abcd12"
    // more usage plan names and IDs
  }
  ```
  ### 9. User Signup

  - **Endpoint:** `POST /signup`
  - **Description:** Registers a new user with a default role of `ADMIN`.
  - **Headers:**
    - `Authorization: Bearer <JWT_TOKEN>`
  - **Request Body:**
    ```json
    {
      "username": "aams12",
      "password": "password"
    }
    ```
  - **Example Request:**
    ```
    POST http://127.0.0.1:5000/signup
    Authorization: Bearer <JWT_TOKEN>
    Content-Type: application/json

    {
      "username": "aams12",
      "password": "password"
    }
    ```
  - **Expected Response:**
    ```json
    {
      "message": "aams12 successfully created"
    }
    ```

  ### 10. User Login

  - **Endpoint:** `POST /login`
  - **Description:** Authenticates a user and returns a JWT token.
  - **Request Body:**
    ```json
    {
      "username": "aams1",
      "password": "password"
    }
    ```
  - **Example Request:**
    ```
    POST http://127.0.0.1:5000/login
    Content-Type: application/json

    {
      "username": "aams1",
      "password": "password"
    }
    ```
  - **Expected Response:**
    ```json
    {
      "MESG": "login success"
    }
    ```
    - **Note:** The JWT token will be returned in the `Authorization` header of the response.

  ### 11. List All Users

  - **Endpoint:** `GET /list_users`
  - **Description:** Retrieves a list of all registered users.
  - **Headers:**
    - `Authorization: Bearer <JWT_TOKEN>`
  - **Example Request:**
    ```
    GET http://127.0.0.1:5000/list_users
    Authorization: Bearer <JWT_TOKEN>
    ```
  - **Expected Response:**
    ```json
    {
      "aams12": "ADMIN",
      "aams1": "USER"
      // more users and their roles
    }
    ```

  ### 12. Update User Role

  - **Endpoint:** `PUT /update_role`
  - **Description:** Updates the role of an existing user.
  - **Headers:**
    - `Authorization: Bearer <JWT_TOKEN>`
  - **Request Body:**
    ```json
    {
      "username": "aams1",
      "role": "MANAGER"
    }
    ```
  - **Example Request:**
    ```
    PUT http://127.0.0.1:5000/update_role
    Authorization: Bearer <JWT_TOKEN>
    Content-Type: application/json

    {
      "username": "aams1",
      "role": "MANAGER"
    }
    ```
  - **Expected Response:**
    ```json
    {
      "message": "Role for aams1 updated to MANAGER"
    }
    ```

  ### 13. Delete a User

  - **Endpoint:** `DELETE /delete_user/<username>`
  - **Description:** Deletes a user by their username.
  - **Headers:**
    - `Authorization: Bearer <JWT_TOKEN>`
  - **Example Request:**
    ```
    DELETE http://127.0.0.1:5000/delete_user/aams12
    Authorization: Bearer <JWT_TOKEN>
    ```
  - **Expected Response:**
    ```json
    {
      "message": "aams12 successfully deleted"
    }
    ```

  ### 14. Home Route

  - **Endpoint:** `GET /`
  - **Description:** Displays the home page (requires authentication).
  - **Headers:**
    - `Authorization: Bearer <JWT_TOKEN>`
  - **Example Request:**
    ```
    GET http://127.0.0.1:5000/
    Authorization: Bearer <JWT_TOKEN>
    ```
  - **Expected Response:**
    - HTML content of the home page (usually an `index.html` file).
    - This response is typically not in JSON format, as it is meant for web display.

  ## Summary

  These examples demonstrate how to interact with the Token Manager API using common HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) and JSON payloads. Most operations require a JWT token for authentication, ensuring that only authorized users can perform actions such as creating tokens, managing users, and setting up usage plans.

  For practical use, replace placeholder values like `<JWT_TOKEN>`, `macId`, `upi`, and usernames with actual data relevant to your application.
