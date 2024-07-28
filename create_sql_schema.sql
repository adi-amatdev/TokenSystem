-- postgres set up
CREATE DATABASE sensorTokens;
CREATE ROLE demo_user WITH LOGIN PASSWORD 'demoPass123!';

GRANT CONNECT ON DATABASE sensorTokens TO demo_user;
CREATE SCHEMA aams_tokens AUTHORIZATION demo_user;
GRANT USAGE ON SCHEMA aams_tokens TO demo_user;

-- tokens schema ddl
CREATE TABLE aams_tokens.tokenInfo (
    macId VARCHAR(17) PRIMARY KEY,
    enabled BOOLEAN,
    usage_plan_id VARCHAR(6),
    api_key_value TEXT,
    created_time_stamp TIMESTAMP,
    activated BIGINT
);
GRANT INSERT, SELECT, UPDATE, DELETE ON aams_tokens.tokeninfo TO demo_user;


-- use \d schema_name.table_name to describe tables
-- use \dt to list tables
-- use \dn to list schemas

-- usage plans schema ddl
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
GRANT INSERT, SELECT ON aams_tokens.usageplan TO demo_user;


-- user login schema ddl
-- Assuming hashed password
CREATE TABLE aams_tokens.users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  password TEXT NOT NULL,
  role VARCHAR(10) NOT NULL
);
GRANT INSERT, SELECT, UPDATE, DELETE ON aams_tokens.users TO demo_user;
GRANT USAGE, SELECT ON SEQUENCE aams_tokens.users_id_seq TO demo_user;
