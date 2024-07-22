from ast import LShift
from tokenFuncs import  createToken,deleteToken
from usagePlan import createUsagePlan
from DatabaseOps import DatabaseOps
from datetime import datetime
import csv
from dotenv import load_dotenv
import os

load_dotenv()
#note: change api stage as required in line: 123
databaseOpsManager = DatabaseOps()

class TokenManager:
    def __init__(self):
        pass

    def createTokenHandler(self, macId:str,upi:str):
        if databaseOpsManager.checkTokenExists(macId):
            return  {
                        "status":400,
                        "message":"token already exists"
                    }

        resp = createToken(macId,upi)
        if resp['ResponseMetadata']['HTTPStatusCode'] == 201:
            keyVal = resp['value']
            enabled = True
            activated = 0
            databaseOpsManager.saveTokenInfo(macId,enabled,upi,keyVal,datetime.now(),activated)
            return {
                "status" : 200,
                "message": "Token Created and associated with usage plan"
            }
        else:
            return {
                "status": 400,
                "message": "aws error"
            }

    def createBulkTokenHandler(self, macIdList:list,upi:str):
        responseDict = {}
        for macId in macIdList:
            resp = self.createTokenHandler(macId,upi)
            if resp["status"] not in range(200,300):
                responseDict[macId] = resp['status']

        if not responseDict:
            return {
                "status": 200,
                "response":{
                    "message": "all tokens successfully created"
                }
            }
        else :
            return {
                "status": 400,
                "response":{
                    "message": "Token creation Failed",
                    "List of macIds with failed token creation":[k for k in responseDict ]
                }

            }

    def deleteTokenHandler(self, macId:str):
        if not databaseOpsManager.checkTokenExists(macId):
            return {
                "status": "400",
                "message" : "token does not exist"
            }
        if deleteToken(macId):
            databaseOpsManager.deleteTokenInfo(macId)
            return {
                "status": 200,
                "message": "deleted token successfully"
            }
        else:
            return {
                "status": 400,
                "message": "token was not deleted"
            }


    def deleteBulkTokenHandler(self, macIdList:list):
        responseDict = {}
        for macId in macIdList :
            resp = self.deleteTokenHandler(macId)
            if resp["status"] not in range(200,300):
                responseDict[macId] = resp['status']

        if not responseDict:
             return {
                 "status": 200,
                 "response":{
                     "message": "all tokens deleted successfully"
                 }
             }
        else :
             return {
                 "status": 400,
                 "response":{
                    "message": "Token deletion Failed",
                    "List of macIds with failed token deletion":[k for k in responseDict ]
                  }
             }

    def sensorFetchHandler(self,macId:str):
        if not databaseOpsManager.checkTokenExists(macId):
            return {
                "status":400,
                "response":{
                    "Error":"MacId does not exist"
                }
            }

        token =  databaseOpsManager.sensorFetch(macId)
        if token is None:
            return {
                "status":400,
                "response":{
                    "message":"token not found",
                    "token":""
                }

            }

        return {
            "status": 200,
            "token":{
                "token":token
            }

        }

    def fetchSensorListHandler(self):
        return databaseOpsManager.fetchAllMacIds()


class UsagePlanManager:
    def __init__(self) -> None:
        pass

    def createUsagePlanHandler(self, name, description, burstLimit, rateLimit, quotaLimit, period):
        if databaseOpsManager.customerExists(name):
            return {
                "status": 400,
                "message":"Customer already exists"
            }

        validPeriods = ['DAY', 'WEEK', 'MONTH']
        if period not in validPeriods:
            return {
                "status":400,
               "message": f"Error: Invalid period. Valid periods are: {', '.join(validPeriods)}"
            }
        #change api stage as required
        apiStages = [
                {
                    'apiId': os.getenv('APIID'),
                    'stage': os.getenv('STAGE')
                }
            ]
        throttleSettings = {
            'burstLimit': burstLimit,
            'rateLimit': rateLimit
        }

        quotaSettings = {
            'limit': quotaLimit,
            'period': period
        }

        resp =  createUsagePlan(name, description, apiStages, throttleSettings, quotaSettings)
        if resp['ResponseMetadata']['HTTPStatusCode'] == 201:
            upi = resp['id']
            databaseOpsManager.insertUsagePlan(name, upi, burstLimit, rateLimit, quotaLimit, period,datetime.now(), activated=True)
            return {
                "status" : 200,
                "message": "Usage Plan Created "
            }
        else:
            return {
                "status": 400,
                "message": "aws error"
            }


    def fetchUsagePlansHandler(self):
        return databaseOpsManager.fetchAllUsagePlans()



class UserManager:

    def __init__(self) -> None:
        self.validRoles = ['USER','MANAGER','ADMIN']

    def createUser(self,username:str,password:str,role:str):
        if role not in self.validRoles:
            return {
                "status":400,
                "response":{
                    "message":f"Valid role not selected from {self.validRoles}"
                }
            }
        if databaseOpsManager.userExists(username):
            return {
                "status":400,
                "response":{
                    "message":f"{username} not available, user another one."
                }
            }

        resp = databaseOpsManager.createUser(username,password,role)
        if resp:
            return {
                "status":200,
                "response":{
                    "message":f"{username} successfully created"
                }
            }

        else:
            return {
                "status":500,
                "response":{
                    "message":f"Error in creating {username} "
                }
            }

    def deleteUser(self,username:str):
        if not databaseOpsManager.userExists(username):
            return {
                "status":400,
                "response":{
                    "message":f"{username} does not exist."
                }
            }
        resp = databaseOpsManager.deleteUser(username)
        if resp:
            return {
                "status":200,
                "response":{
                    "message":f"{username} successfully deleted"
                }
            }

        else:
            return {
                "status":500,
                "response":{
                    "message":f"Error in deleting {username} ."
                }
            }

    def fetchUsers(self):
        return databaseOpsManager.fetchAllUsers()

    def fetchUserLogin(self,username:str):
        if not databaseOpsManager.userExists(username):
            return {
                "status":500
            }
        resp = databaseOpsManager.fetchUser(username)
        if resp:
            return {
                "status":200,
                "details": resp
            }
        else:
            return {
                "status":400,
                "message":"No information available"            }

    def updateRole(self,username:str,role:str):
        if role not in self.validRoles:
            return {
                "status":400,
                "response":{
                    "message":f"Valid role not selected from {self.validRoles}"
                }
            }

        resp = databaseOpsManager.updateRole(username,role)
        if resp:
            return {
                "status":200,
                "message":f"Role for {username} updated to {role}"
            }
        else:
            return {
                "status":400,
                "response":{
                    "message":f"could not update role"
                }
            }
