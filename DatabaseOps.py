import datetime
import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime


# Load environment variables from .env file
load_dotenv()

class DatabaseOps:
    def __init__(self) -> None:
        pass
    # Connect to the PostgreSQL database
    @staticmethod
    def connectDB():
        conn = psycopg2.connect(database=os.getenv('DATABASE_NAME'), user=os.getenv('USERNAME'), password=os.getenv('PASSWORD'), host=os.getenv('HOST'), port=os.getenv('PORT'))
        cur = conn.cursor()
        return conn,cur

    #token and usage plan functions
    def saveTokenInfo(self,macId:str, enabled:bool, usagePlanID:str, apiKeyValue:str, createdTimeStamp:datetime, activated:int):
        conn, cur = self.connectDB()
        # Define SQL statement with placeholders for data
        sql = """
        INSERT INTO aams_tokens.tokenInfo (mac_id, enabled, usage_plan_id, api_key_value, created_time_stamp, activated)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        # Prepare the statement to prevent SQL injection vulnerabilities
        preparedStmt = cur.mogrify(sql, (macId, enabled, usagePlanID, apiKeyValue, createdTimeStamp, activated))

        try:
            # Execute the prepared statement with the actual data
            cur.execute(preparedStmt)
            # Commit the changes to the database
            conn.commit()
            print("Token information saved successfully!")
        except (Exception, psycopg2.Error) as error:
            print("Error while saving token information:", error)
        finally:
            # Close the connection
            if conn:
                conn.close()

    def insertUsagePlan(self,batchName:str, usagePlanID:str, burstLimit:int, rateLimit:int, quotaLimit:int, period:str,timeStamp:datetime, activated:bool):
        conn, cur = self.connectDB()


        # Define the SQL INSERT statement
        sql = """
            INSERT INTO aams_tokens.usagePlan (
                batch_id, usage_plan_id, burst_limit, rate_limit, quota_limit, period, created_time_stamp, activated
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s
            )
        """

        # Execute the INSERT statement
        preparedStmt = cur.mogrify(sql,(
            batchName, usagePlanID, burstLimit, rateLimit, quotaLimit, period, timeStamp, activated
        ))

        try:
            # Execute the prepared statement with the actual data
            cur.execute(preparedStmt)
            # Commit the changes to the database
            conn.commit()
            print("Usage Plan information saved successfully!")
        except (Exception, psycopg2.Error) as error:
            print("Error while saving Usage Plan information:", error)
        finally:
            # Close the connection
            if conn:
                conn.close()


    def deleteTokenInfo(self,macId:str):
        conn, cur = self.connectDB()
        # Define SQL statement with placeholder for mac_id
        sql = """
        DELETE FROM aams_tokens.tokenInfo
        WHERE mac_id = %s
        """

        # Prepare the statement to prevent SQL injection vulnerabilities
        preparedStmt = cur.mogrify(sql, (macId,))

        try:
            # Execute the prepared statement with the actual data
            cur.execute(preparedStmt)
            # Commit the changes to the database
            conn.commit()
            print(f"Token information for MAC address '{macId}' deleted successfully!")
        except (Exception, psycopg2.Error) as error:
            print("Error while deleting token information:", error)
        finally:
            # Close the connection
            if conn:
             conn.close()

    def checkTokenExists(self,macId:str):
        conn , cur = self.connectDB()

        try:
            # Define SQL statement with placeholder for mac_id
            sql = """
            SELECT EXISTS (
                SELECT 1
                FROM aams_tokens.tokenInfo
                WHERE mac_id = %s
            )
            """

            # Execute the query with the actual data
            cur.execute(sql, (macId,))

            # Fetch the result
            exists = cur.fetchone()[0]

            return exists

        except (Exception, psycopg2.Error) as error:
            print("Error while checking token existence:", error)
            return False

        finally:
            # Close the cursor and connection
            if conn:
                conn.close()


    def batchExists(self,batchName:str):
        conn, cur = self.connectDB()

        try:
            # Define the SQL SELECT statement
            sql = """
                SELECT 1 FROM aams_tokens.usagePlan WHERE batch_id = %s
            """

            # Execute the SELECT statement
            cur.execute(sql, (batchName,))

            # Fetch one record
            result = cur.fetchone()

            return result is not None

        except Exception as error:
            print("Error checking batch existence:", error)
            return False

        finally:
            # Close the cursor and connection
            if conn:
                conn.close()

    def sensorFetch(self,macId:str):
        conn , cur = self.connectDB()

        try:
            # Define SQL statement with placeholder for mac_id
            sql = """
            SELECT api_key_value
            FROM aams_tokens.tokenInfo
            WHERE mac_id = %s
            """
            updateSql = """
                    UPDATE aams_tokens.tokenInfo
                    SET activated = activated + 1
                    WHERE mac_id = %s
                    RETURNING api_key_value;
                    """
            # Execute the query with the actual data
            cur.execute(sql, (macId,))

            # Fetch the result
            result = cur.fetchone()

                    # If result is not None, return the api_key_value, otherwise return None
            if result:
                cur.execute(updateSql, (macId,))
                conn.commit()
                return result[0]
            else:
                return None

        except (Exception, psycopg2.Error) as error:
            print("Error while checking token existence:", error)
            return None

        finally:
            # Close the cursor and connection
            if conn:
                conn.close()

    def fetchAllMacIds(self):
        conn, cur = self.connectDB()

        try:
            # Define SQL statement to fetch all macIds and their corresponding activated values
            sql = """
            SELECT mac_id, activated
            FROM aams_tokens.tokenInfo;
            """

            # Execute the query
            cur.execute(sql)

            # Fetch all results
            results = cur.fetchall()

            # Return the results as a list of tuples
            return results

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching macIds and activated values:", error)
            return None

        finally:
            # Close the cursor and connection
            if conn:
                cur.close()
                conn.close()


    def fetchAllUsagePlans(self):
        conn, cur = self.connectDB()

        try:
            # Define SQL statement to fetch all macIds and their corresponding activated values
            sql = """
            SELECT batch_id, usage_plan_id
            FROM aams_tokens.usageplan;
            """

            # Execute the query
            cur.execute(sql)

            # Fetch all results
            results = cur.fetchall()

            # Return the results as a list of tuples
            return results

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching Batch Names and Usage Plan IDs:", error)
            return None

        finally:
            # Close the cursor and connection
            if conn:
                cur.close()
                conn.close()

    #user functions
    def createUser(self,username:str,password:str,role:str):
        conn,cur = self.connectDB()

        sql = '''
            INSERT INTO aams_tokens.users(username,password,role) VALUES (%s,%s,%s)
        '''

        preparedStmt = cur.mogrify(sql,(username,password,role))

        try:
            # Execute the prepared statement with the actual data
            cur.execute(preparedStmt)
            # Commit the changes to the database
            conn.commit()
            print(f"User:{username} Created !")
            return True
        except (Exception, psycopg2.Error) as error:
            print("Error while saving user information:", error)
            return False
        finally:
            # Close the connection
            if conn:
                conn.close()

    def deleteUser(self,username:str):
        conn, cur = self.connectDB()
        # Define SQL statement with placeholder for mac_id
        sql = """
        DELETE FROM aams_tokens.users
        WHERE username = %s
        """

        # Prepare the statement to prevent SQL injection vulnerabilities
        preparedStmt = cur.mogrify(sql, (username,))

        try:
            # Execute the prepared statement with the actual data
            cur.execute(preparedStmt)
            # Commit the changes to the database
            conn.commit()
            print(f"User information belonging to:'{username}' deleted successfully!")
            return True
        except (Exception, psycopg2.Error) as error:
            print("Error while deleting user information:", error)
            return False
        finally:
            # Close the connection
            if conn:
             conn.close()

    def userExists(self,username:str):
        conn, cur = self.connectDB()

        try:
            # Define the SQL SELECT statement
            sql = """
                SELECT 1 FROM aams_tokens.users WHERE username = %s
            """

            # Execute the SELECT statement
            cur.execute(sql, (username,))

            # Fetch one record
            result = cur.fetchone()

            return result is not None

        except Exception as error:
            print("Error checking user existence:", error)
            return False

        finally:
            # Close the cursor and connection
            if conn:
                cur.close()
                conn.close()

    def fetchAllUsers(self):
            conn, cur = self.connectDB()

            try:
                # Define SQL statement to fetch all macIds and their corresponding activated values
                sql = """
                SELECT username, role
                FROM aams_tokens.users;
                """

                # Execute the query
                cur.execute(sql)

                # Fetch all results
                results = cur.fetchall()

                # Return the results as a list of tuples
                return results

            except (Exception, psycopg2.Error) as error:
                print("Error while fetching users :", error)
                return None

            finally:
                # Close the cursor and connection
                if conn:
                    conn.close()

    def fetchUser(self,username:str):
            conn, cur = self.connectDB()

            try:
                # Define SQL statement to fetch all macIds and their corresponding activated values
                sql = """
                SELECT username, password, role
                FROM aams_tokens.users
                WHERE username = %s;
                """
                preparedStmnt = cur.mogrify(sql,(username,))
                # Execute the query
                cur.execute(preparedStmnt)

                # Fetch all results
                result  = cur.fetchone()

                # Return the results as a list of tuples
                return result

            except (Exception, psycopg2.Error) as error:
                print(f"Error while fetching user {username} :", error)
                return None

            finally:
                # Close the cursor and connection
                if conn:
                    conn.close()

    def updateRole(self,username:str,role:str):
        conn, cur = self.connectDB()

        try:
            # Define SQL statement to fetch all macIds and their corresponding activated values
            sql = """
            UPDATE aams_tokens.users
            SET role = %s
            WHERE username = %s;
            """
            preparedStmnt = cur.mogrify(sql,(role,username))
            # Execute the query
            cur.execute(preparedStmnt)
            conn.commit()
            return True
        except (Exception, psycopg2.Error) as error:
            conn.rollback()
            print(f"Error while updating user {username} :", error)
            return False

        finally:
            # Close the cursor and connection
            if conn:
                conn.close()
