1. Database operation may fail but `AWS-SDKs` might be successful causing `discrepancy` between the information in the `POSTGRES` database and `AWS` always double check or improve codebase to better handle this.
2. While installing python libraries from  `requirements.txt` , `psycopg2` might throw some error . Hence use : `pip install psycopg2-binary`
3. The `AWS-CREDENTIALS` might not have been set properly hence causing zoning issues, always use in `ap-south-1` while prompted for zone after running `aws config`
