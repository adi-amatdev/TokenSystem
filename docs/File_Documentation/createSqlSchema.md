## SQL Code Documentation

### Purpose
This SQL code sets up a PostgreSQL database environment for managing sensor tokens, usage plans, and user accounts. It creates a new database, a user role, and schemas for organizing the data.

### Breakdown

#### Database and User Setup
* **CREATE DATABASE sensorTokens:** Creates a new database named "sensorTokens".
* **CREATE ROLE demo_user WITH LOGIN PASSWORD 'demoPass123!';:** Creates a new user role named "demo_user" with the password "demoPass123!".
* **GRANT CONNECT ON DATABASE sensorTokens TO demo_user;:** Grants the "demo_user" role the right to connect to the "sensorTokens" database.

#### Schema Creation
* **CREATE SCHEMA aams_tokens AUTHORIZATION demo_user;:** Creates a new schema named "aams_tokens" under the ownership of the "demo_user" role.
* **GRANT USAGE ON SCHEMA aams_tokens TO demo_user;:** Grants the "demo_user" role the right to use the "aams_tokens" schema.

#### Table Definitions

##### `tokenInfo` Table
* **macId:** Primary key, uniquely identifies a sensor device.
* **enabled:** Indicates whether the token is active or disabled.
* **usage_plan_id:** Foreign key referencing the usage plan for the token.
* **api_key_value:** The API key associated with the token.
* **created_time_stamp:** Timestamp of token creation.
* **activated:** Indicates whether the token has been activated.

##### `usagePlan` Table
* **batch_id:** Primary key, uniquely identifies a batch of usage plans.
* **usage_plan_id:** Identifier for the usage plan.
* **burstLimit:** The maximum number of requests allowed within a specific time window.
* **rate_limit:** The maximum number of requests allowed per time unit.
* **quota_limit:** The total number of requests allowed within a given period.
* **period:** The time period for which the quota applies (e.g., "hour", "day").
* **created_time_stamp:** Timestamp of usage plan creation.
* **activated:** Indicates whether the usage plan is active.

##### `users` Table
* **id:** Primary key, auto-incrementing integer.
* **username:** Unique username for the user.
* **password:** Hashed password for the user.
* **role:** Role or permission level of the user.

### Additional Notes
* **\d schema_name.table_name:** Used to describe the structure of a specific table.
* **\dt:** Lists all tables in the current database.
* **\dn:** Lists all schemas in the current database.

This SQL code provides a foundation for managing sensor tokens, usage plans, and user accounts in a PostgreSQL database. You can further customize and extend it based on your specific requirements.
