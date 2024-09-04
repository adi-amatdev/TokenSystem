## Prerequisites

Ensure you have the following software installed:

- Python 3.x
- Flask
- PostgreSQL
- AWS-CLI

## Step-by-Step Instructions

1. **Virtual Environment Setup**:
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    
    ```
    
2. **Installing Dependencies**:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
3. **Setting up Databases**:
    - Create a PostgreSQL database.
    - Update database credentials in the Flask app configuration.
4. **Setting up AWS-Credentials:**
    - First Install `AWS CLI` and run `aws` in your terminal to make sure it is running.
    - Run  `aws config`  and then set up the credentials as necessary.
    - Refer : ( Refer `IAM role` in this documentation for easy set up)
    
    [Set up the AWS CLI - AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html)
    

## Configuration

- **Environment Variables**:
    - `DATABASE_Credentials`:  for connecting to the PostgreSQL database. For Example
        
        ```bash
        # DATBASE CONSTANTS
        DATABASE_NAME = 'sensortokens'
        USERNAME = 'demo_user'
        PASSWORD = 'demoPass123!'
        HOST = 'localhost'
        PORT = 5432
        ```
        
    - `SECRET_KEY`: Secret key for Flask session management.
        
        ```bash
        #APP CONFIG
        SECRET_KEY = "Dev"
        JWT_SECRET_KEY = "jwt@123!"
        ```
        
    - `DEBUG`: Set to `True` for development mode. (refer main function in `app.py`)
- **Configuration Files**:
    - `create_sql_schema.sql`: SQL script for creating the database schema.

Ensure all configurations are set correctly before running the project.