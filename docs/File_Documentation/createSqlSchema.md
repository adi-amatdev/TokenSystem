### PostgreSQL Setup Documentation

This documentation outlines the steps to set up a PostgreSQL database for managing tokens, usage plans, and user authentication. The database schema is structured under a schema named `aams_tokens`, with tables to store token information, usage plans, and user credentials.

#### 1. Database and Role Creation

- **Create Database:**
  ```sql
  CREATE DATABASE sensorTokens;
  ```
  This command creates a new database named `sensorTokens`.

- **Create Role:**
  ```sql
  CREATE ROLE demo_user WITH LOGIN PASSWORD 'demoPass123!';
  ```
  This command creates a role named `demo_user` with login capability and sets the password to `'demoPass123!'`.

- **Grant Database Connection Permission:**
  ```sql
  GRANT CONNECT ON DATABASE sensorTokens TO demo_user;
  ```
  This command grants the `demo_user` role permission to connect to the `sensorTokens` database.

#### 2. Schema Setup

- **Create Schema:**
  ```sql
  CREATE SCHEMA aams_tokens AUTHORIZATION demo_user;
  ```
  This command creates a new schema named `aams_tokens` within the `sensorTokens` database and authorizes `demo_user` as the owner.

- **Grant Schema Usage Permission:**
  ```sql
  GRANT USAGE ON SCHEMA aams_tokens TO demo_user;
  ```
  This command grants `demo_user` the ability to use the `aams_tokens` schema.

#### 3. Tokens Schema DDL

- **Create `tokenInfo` Table:**
  ```sql
  CREATE TABLE aams_tokens.tokenInfo (
      macId VARCHAR(17) PRIMARY KEY,
      enabled BOOLEAN,
      usage_plan_id VARCHAR(6),
      api_key_value TEXT,
      created_time_stamp TIMESTAMP,
      activated BIGINT
  );
  ```
  This command creates the `tokenInfo` table within the `aams_tokens` schema, with columns to store:
  - `macId`: MAC address (Primary Key)
  - `enabled`: Status of the token (Boolean)
  - `usage_plan_id`: ID of the associated usage plan (String)
  - `api_key_value`: API key value (Text)
  - `created_time_stamp`: Timestamp of token creation (Timestamp)
  - `activated`: Activation count (BigInt)

- **Grant Table Permissions:**
  ```sql
  GRANT INSERT, SELECT, UPDATE, DELETE ON aams_tokens.tokeninfo TO demo_user;
  ```
  This command grants `demo_user` the ability to perform `INSERT`, `SELECT`, `UPDATE`, and `DELETE` operations on the `tokenInfo` table.

#### 4. Usage Plans Schema DDL

- **Create `usagePlan` Table:**
  ```sql
  CREATE TABLE aams_tokens.usagePlan (
      batch_id VARCHAR(30) PRIMARY KEY,
      usage_plan_id VARCHAR(6),
      burstLimit BIGINT,
      rate_limit BIGINT,
      quota_limit BIGINT,
      period CHAR(10),
      created_time_stamp TIMESTAMP,
      activated BOOLEAN
  );
  ```
  This command creates the `usagePlan` table within the `aams_tokens` schema, with columns to store:
  - `batch_id`: Batch identifier (Primary Key)
  - `usage_plan_id`: Usage plan ID (String)
  - `burstLimit`: Burst limit (BigInt)
  - `rate_limit`: Rate limit (BigInt)
  - `quota_limit`: Quota limit (BigInt)
  - `period`: Period duration (Char)
  - `created_time_stamp`: Timestamp of plan creation (Timestamp)
  - `activated`: Activation status (Boolean)

- **Grant Table Permissions:**
  ```sql
  GRANT INSERT, SELECT ON aams_tokens.usageplan TO demo_user;
  ```
  This command grants `demo_user` the ability to perform `INSERT` and `SELECT` operations on the `usagePlan` table.

#### 5. User Login Schema DDL

- **Create `users` Table:**
  ```sql
  CREATE TABLE aams_tokens.users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role VARCHAR(10) NOT NULL
  );
  ```
  This command creates the `users` table within the `aams_tokens` schema, with columns to store:
  - `id`: Unique identifier (Primary Key, Auto-incremented)
  - `username`: Username (Unique, Not Null)
  - `password`: User password (Not Null, Assumed to be hashed)
  - `role`: User role (String, Not Null)

- **Grant Table Permissions:**
  ```sql
  GRANT INSERT, SELECT, UPDATE, DELETE ON aams_tokens.users TO demo_user;
  GRANT USAGE, SELECT ON SEQUENCE aams_tokens.users_id_seq TO demo_user;
  ```
  These commands grant `demo_user` the ability to perform `INSERT`, `SELECT`, `UPDATE`, and `DELETE` operations on the `users` table, as well as permission to use and select from the `users_id_seq` sequence for auto-incremented IDs.

#### 6. Additional Commands

- **Describe Tables:**
  ```sql
  \d schema_name.table_name
  ```
  This command is used to describe the structure of a specific table.

- **List Tables:**
  ```sql
  \dt
  ```
  This command lists all tables in the current schema.

- **List Schemas:**
  ```sql
  \dn
  ```
  This command lists all schemas in the current database.