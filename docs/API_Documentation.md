# API Documentation for Flask Application

## Overview
This API provides endpoints to manage users, tokens, and usage plans for a system. It includes user authentication, token management, and usage plan creation and retrieval. The API uses JSON Web Tokens (JWT) for securing the endpoints and requires JWT tokens for most operations.

### Base URL
- `http://<your-domain>:5000/`

## Authentication
All endpoints, except for the `/login` endpoint, require a valid JWT token in the `Authorization` header with the format `Bearer <token>`.

## Endpoints

### User Management

#### Create a New User
- **Endpoint:** `/signup`
- **Method:** `POST`
- **Description:** Creates a new user with a default role of `ADMIN`.
- **Headers:**
  - `Authorization: Bearer <token>`
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Responses:**
  - `200 OK`: User created successfully.
  - `400 Bad Request`: Username, password, or role not provided, or user already exists.

#### Login
- **Endpoint:** `/login`
- **Method:** `POST`
- **Description:** Authenticates a user and returns a JWT token.
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Responses:**
  - `200 OK`: Login successful. Returns a JWT token in the `Authorization` header.
  - `400 Bad Request`: Username or password incorrect.
  - `401 Unauthorized`: Authentication failed.

#### List Users
- **Endpoint:** `/list_users`
- **Method:** `GET`
- **Description:** Retrieves a list of all users.
- **Headers:**
  - `Authorization: Bearer <token>`
- **Responses:**
  - `200 OK`: Returns a list of users.
  - `400 Bad Request`: Failed to fetch users.

#### Update User Role
- **Endpoint:** `/update_role`
- **Method:** `PUT`
- **Description:** Updates the role of an existing user.
- **Headers:**
  - `Authorization: Bearer <token>`
- **Request Body:**
  ```json
  {
    "username": "string",
    "role": "string" // Valid roles: USER, MANAGER, ADMIN
  }
  ```
- **Responses:**
  - `200 OK`: Role updated successfully.
  - `400 Bad Request`: Invalid role or failure to update the role.

#### Delete User
- **Endpoint:** `/delete_user/<username>`
- **Method:** `DELETE`
- **Description:** Deletes a specified user.
- **Headers:**
  - `Authorization: Bearer <token>`
- **Responses:**
  - `200 OK`: User deleted successfully.
  - `400 Bad Request`: Failure to delete user.

### Token Management

#### Create a Single Token
- **Endpoint:** `/create_token`
- **Method:** `POST`
- **Description:** Creates a new token associated with a specified `macId` and `upi`.
- **Headers:**
  - `Authorization: Bearer <token>`
- **Request Body:**
  ```json
  {
    "macId": "string",
    "upi": "string"
  }
  ```
- **Responses:**
  - `200 OK`: Token created successfully.
  - `400 Bad Request`: Missing or invalid `macId` or `upi`.

#### Delete a Single Token
- **Endpoint:** `/delete_token`
- **Method:** `DELETE`
- **Description:** Deletes an existing token associated with a specified `macId`.
- **Headers:**
  - `Authorization: Bearer <token>`
- **Request Body:**
  ```json
  {
    "macId": "string"
  }
  ```
- **Responses:**
  - `200 OK`: Token deleted successfully.
  - `400 Bad Request`: Token does not exist or invalid `macId`.

#### Create Tokens in Bulk
- **Endpoint:** `/create_tokens_bulk/<usagePlan>`
- **Method:** `POST`
- **Description:** Creates tokens in bulk by uploading a CSV file containing `macId`s.
- **Headers:**
  - `Authorization: Bearer <token>`
- **Request:** Multipart Form Data
  - `csv_file`: CSV file containing `macId`s.
- **Responses:**
  - `200 OK`: All tokens created successfully.
  - `400 Bad Request`: Missing or invalid CSV file, or some tokens failed to be created.

#### Delete Tokens in Bulk
- **Endpoint:** `/delete_tokens_bulk`
- **Method:** `DELETE`
- **Description:** Deletes tokens in bulk by uploading a CSV file containing `macId`s.
- **Headers:**
  - `Authorization: Bearer <token>`
- **Request:** Multipart Form Data
  - `csv_file`: CSV file containing `macId`s.
- **Responses:**
  - `200 OK`: All tokens deleted successfully.
  - `400 Bad Request`: Missing or invalid CSV file, or some tokens failed to be deleted.

#### Fetch Token for Sensor
- **Endpoint:** `/sensor_fetch`
- **Method:** `GET`
- **Description:** Retrieves a token for a specific `macId`.
- **Headers:**
  - `Authorization: Bearer <token>`
- **Request Body:**
  ```json
  {
    "macId": "string"
  }
  ```
- **Responses:**
  - `200 OK`: Returns the token.
  - `400 Bad Request`: `macId` does not exist or token not found.

#### Fetch All Sensors
- **Endpoint:** `/sensor_list`
- **Method:** `GET`
- **Description:** Retrieves a list of all sensors and their statuses.
- **Headers:**
  - `Authorization: Bearer <token>`
- **Responses:**
  - `200 OK`: Returns the list of sensors.
  - `500 Internal Server Error`: Failed to fetch the sensor list.

### Usage Plan Management

#### Create Usage Plan
- **Endpoint:** `/create_usage_plan`
- **Method:** `POST`
- **Description:** Creates a new usage plan for a customer.
- **Headers:**
  - `Authorization: Bearer <token>`
- **Request Body:**
  ```json
  {
    "name": "string",
    "description": "string",
    "burst_limit": "integer",
    "rate_limit": "integer",
    "quota_limit": "integer",
    "period": "string" // Valid periods: DAY, WEEK, MONTH
  }
  ```
- **Responses:**
  - `200 OK`: Usage plan created successfully.
  - `400 Bad Request`: Missing or invalid details.

#### Fetch Usage Plans
- **Endpoint:** `/fetch_usage_plans`
- **Method:** `GET`
- **Description:** Retrieves all usage plans.
- **Headers:**
  - `Authorization: Bearer <token>`
- **Responses:**
  - `200 OK`: Returns the list of usage plans.
  - `400 Bad Request`: No usage plans available.

## Error Handling
All endpoints return a JSON response with an appropriate HTTP status code. The response includes an `Error` or `message` field describing the error or success message.

## Security Considerations
- Ensure that JWT tokens are kept secure and not exposed to unauthorized users.
- All sensitive data, like passwords, should be hashed before storage.
- Cross-Origin Resource Sharing (CORS) is enabled with `*`, which can be adjusted based on the deployment environment.

## Running the Application
- The application runs on port 5000 by default and can be accessed via `http://<your-domain>:5000/`.
- Ensure to set the necessary environment variables, including `SECRET_KEY` and `JWT_SECRET_KEY`, before running the application.

