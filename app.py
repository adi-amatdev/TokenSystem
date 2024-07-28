from flask import Flask, request, jsonify, render_template,redirect
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt

from datetime import datetime,timedelta
from flask.helpers import make_response
from HandlerClass import TokenManager,UsagePlanManager,UserManager
import pandas as pd
from flask_cors import CORS,cross_origin
from werkzeug.security import check_password_hash,generate_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)  # Token expires in 1 hour


CORS(app)

# JWT Initialization
jwt = JWTManager(app)
# Initialize Manager instances
tokenManager = TokenManager()
usagePlanManager = UsagePlanManager()
users = UserManager()


@app.route('/',methods=['GET'])
@jwt_required()
def home():
    print(get_jwt_identity())
    return render_template('index.html')

#USER APIs


# Route to create a new user (accessible by admin and manager)
@app.route('/signup', methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    username = data.get('username',None)
    password = data.get('password',None)
    #every new user is a normal user by default. Privilege escalation can only be done by an admin
    role = 'ADMIN'

    if not username or not password or not role:
        return jsonify({'error': 'Username, password are required'}), 400

    password = generate_password_hash(password=password)
    print(password)
    resp = users.createUser(username=username,password=password,role=role)

    if resp['status'] == 200:
        return jsonify({"message":f"{resp['response']['message']}"})

    return jsonify({"Error":f"{resp['response']['message']}"}),400


#NEED TO RETURN JWT HERE
@app.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username',None)
    password = data.get('password',None)

    #returns tuple in the format (username,hashedPass,role)
    userInfo = users.fetchUserLogin(username=username)
    if userInfo['status'] == 500:
        return jsonify({"Error":f"Username or Password incorrect"}),400
    phash = userInfo['details']
    if check_password_hash(pwhash=phash[1],password=password):
        #verify next line
        sToken = create_access_token(identity={"username":phash[0],"role":phash[2]})
        resp = make_response(jsonify({'MESG':"login success"}),200)
        # resp.set_cookie('jwt', sToken, httponly=True, secure=True)
        resp.headers['Authorization'] = f'Bearer {sToken}'
        return resp

    return jsonify({"mesg":"Username or Password incorrect"}),401

@app.route("/list_users",methods=['GET'])
@jwt_required()
def listUsers():
    resp = users.fetchUsers()
    if resp:
        return jsonify(dict(resp)),200
    return jsonify({"Error":"not able to fetch users"}),400

@app.route('/update_role',methods=['PUT'])
@jwt_required()
def updateRole():
    data = request.get_json()
    username = data.get('username',None)
    role = data.get('role',None)

    resp = users.updateRole(username=username,role=role)
    if resp['status'] == 200:
        return jsonify({"message":f"{resp['message']}"})

    return jsonify({"Error":f"Failure: {resp['response']['message']}"})



@app.route("/delete_user/<username>",methods=['DELETE'])
@jwt_required()
def deleteUser(username):

    resp = users.deleteUser(username)
    if resp:
        return jsonify(dict(resp['response'])),200
    return jsonify({"Error":f"not able to delete user:{resp['response']}"}),400



# TOKEN APIs

# Endpoint for creating a single token
@app.route('/create_token', methods=['POST'])
@jwt_required()
@cross_origin(origins='*')
def createSingleToken():
    data = request.get_json()
    macId = data.get('macId',None)
    upi = data.get('upi',None)
    if  not macId or not upi:
        return jsonify({"Error": "macId and upi are required"}), 400

    resp = tokenManager.createTokenHandler(macId, upi)
    if resp['status']== 200:
        return jsonify({"message":resp['message']}),200

    return jsonify({"message":resp['message']}),400

# Endpoint for deleting a single token
@app.route('/delete_token/', methods=['DELETE'])
@jwt_required()
def deleteSingleToken():
    data = request.get_json()
    macId = data.get('macId',None)

    if 'macId' not in data or not macId:
        return jsonify({"Error":"macId required"}),400
    resp = tokenManager.deleteTokenHandler(macId)
    if resp['status'] == 200:
        return jsonify({"message":resp['message']})

    return jsonify({"message":resp['message']}),400


# Endpoint for creating tokens in bulk
@app.route('/create_tokens_bulk/<usagePlan>', methods=['POST'])
@jwt_required()
def createTokensBulk(usagePlan):

    if 'csv_file' not in request.files:
            return jsonify({"Error": "No file part"}), 400

    file = request.files['csv_file']

    if file.filename == '':
            return jsonify({"Error": "No selected file"}), 400

    if file and file.filename.endswith('.csv'):
            try:
                # Read the CSV file into a pandas DataFrame
                df = pd.read_csv(file)

                # Convert DataFrame to list of dictionaries
                dataList = df.to_dict(orient='records')
                if not dataList:
                    raise Exception("No macIds were provided")
                #Append the information to a list
                resultList = []
                for item in dataList:
                     resultList.append(item['macId'])

                resp = tokenManager.createBulkTokenHandler(resultList,usagePlan)
                if resp['status'] == 200:
                    return jsonify(resp['response']),200

                return jsonify(resp['response']),400

            except Exception as e:
                return jsonify({"Error": str(e)}), 500

    return jsonify({"Error": "Invalid file format, must be .csv"}), 400


# Endpoint for deleting tokens in bulk
@app.route('/delete_tokens_bulk', methods=['DELETE'])
@jwt_required()
def deleteTokensBulk():
    if 'csv_file' not in request.files:
            return jsonify({"Error": "No file part"}), 400

    file = request.files['csv_file']

    if file.filename == '':
            return jsonify({"Error": "No selected file"}), 400

    if file and file.filename.endswith('.csv'):
            try:
                # Read the CSV file into a pandas DataFrame
                df = pd.read_csv(file)

                # Convert DataFrame to list of dictionaries
                dataList = df.to_dict(orient='records')
                if not dataList:
                    raise Exception("No macIds were provided")
                #Append the information to a list
                resultList = []
                for item in dataList:
                     resultList.append(item['macId'])

                resp = tokenManager.deleteBulkTokenHandler(resultList)
                if resp['status'] == 200:
                    return jsonify(resp['response']),200

                return jsonify(resp['response']),400

            except Exception as e:
                return jsonify({"Error": str(e)}), 500

    return jsonify({"Error": "Invalid file format, must be .csv"}), 400

#for sensors to hit and gain token
@app.route('/sensor_fetch',methods = ['GET'])
@jwt_required()
def sensorFetch():
    data = request.get_json()
    macId = data.get('macId',None)
    resp = tokenManager.sensorFetchHandler(macId)
    if resp['status'] == 200:
        return jsonify(resp['token']),200
    return jsonify(resp['response']),400

#to fetch all sensors and their activated status
@app.route('/sensor_list' ,methods=['GET'])
@jwt_required()
def sensorListFetch():
    sensorList = tokenManager.fetchSensorListHandler()
    if sensorList:
        return jsonify(dict(sensorList)),200
    return jsonify({"Error":"Not able to fetch list"}),500


#USAGE PLANS APIs

#create usage plan per customer
@app.route('/create_usage_plan',methods=['POST'])
@jwt_required()
def createUsagePlan():
    data = request.get_json()
    if not data:
        return jsonify({"Error":"No details provided"}),400
    batchName = data.get('name',None)
    description = data.get('description',None)
    burstLimit = data.get('burst_limit',None)
    rateLimit = data.get('rate_limit',None)
    quotaLimit = data.get('quota_limit',None)
    period = data.get('period',None)

    resp = usagePlanManager.createUsagePlanHandler(batchName,description,burstLimit,rateLimit,quotaLimit,period)
    if resp['status'] == 200:
        return jsonify({"Success":f"{resp['message']}"}),200

    return jsonify({"Error":f"Could not create usage plan: {resp['message']}"}),400

#fetch all customers and usage plan Id's
@app.route("/fetch_usage_plans",methods=['GET'])
@jwt_required()
def fetchUsagePlans():
    usagePlanList = usagePlanManager.fetchUsagePlansHandler()
    if usagePlanList:
        return jsonify(dict(usagePlanList)),200
    return jsonify({"Error":"no Batches to fetch"}),400

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0",port=5000)
