from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token



app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

#Endpoints
@app.route("/login", methods = ['POST'])
def login():
    headers = request.headers
    auth = headers.get("X-Parse-REST-API-Key")
    response = jsonify()
    if auth == '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c':
        request_data = request.get_json()
        name = request_data["name"]
        password = request_data["password"]
        if name == "Lorde" and password == "Team":
            access_token =  create_access_token(identity=name)
            response = jsonify(access_token=access_token), 200
    else:
        response =  jsonify({"message": "ERROR: Unauthorized"}), 401
    
    return response





@app.route("/DevOps", methods=['POST'])
@jwt_required()
def getDevOps():
    headers = request.headers
    auth = headers.get("X-Parse-REST-API-Key")
    response = jsonify()
    if auth == '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c':
        request_data = request.get_json()
        message = request_data['message']
        to = request_data['to']
        from_sender = request_data['from']
        timeToLifeSec = request_data['timeToLifeSec']    
        message_back = "Hello " + to + " your message will be send"
        response =  jsonify({"message" : message_back}), 200
    else:
        response =  jsonify({"message": "ERROR: Unauthorized"}), 401
    
    return response

#health check

@app.route("/health")
def health():
    return jsonify(status = "UP")

#Error handler

@app.errorhandler(405)
def method_not_allowed(error):
    return "ERROR", 405

def me(number1, number2):
    if number1 == number2:
        return True
    else: 
        return False



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)