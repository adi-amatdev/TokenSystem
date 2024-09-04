### Important Notes

1. **Database Discrepancies:**
   - Database operations may sometimes fail, while the `AWS SDKs` might still succeed. This can lead to discrepancies between the data stored in the `POSTGRES` database and the data on `AWS`.
   - To prevent this, always double-check the consistency of the data or improve the codebase to handle such situations more robustly.

2. **Installing Python Libraries:**
   - When installing Python libraries from `requirements.txt`, you might encounter errors with `psycopg2`.
   - To avoid this, use the command: `pip install psycopg2-binary` instead.

3. **AWS Credentials and Zoning Issues:**
   - If the `AWS-CREDENTIALS` are not set up correctly, you might face zoning issues.
   - Always ensure that you use the `ap-south-1` region when prompted for the zone during the `aws config` setup.
