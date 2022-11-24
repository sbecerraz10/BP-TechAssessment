import pytest
import lib.app as app
import requests
from flask import jsonify
import json

SERVER_URL = "http://192.168.1.7:8080"
bearer_token = 0


def post_login():
    response = requests.post(SERVER_URL + "/login", data=json.dumps({"name":"Lorde", "password": "Team"}), headers={'Content-Type': 'application/json','X-Parse-REST-API-Key':'2f5ae96c-b558-4c7b-a590-a501ae1c3f6c'})
    json_obj = response.json()
    bearer_token = json_obj['access_token']
    return response, bearer_token


def test_login():
    with app.app.app_context(): 
        global bearer_token
        response, bearer_token = post_login()
        test = {}
        assert response.status_code == 200
        #if 200 == response.status_code:
        #    test = {"status" : "passed"}
        #else:
        #    test = {"status" : "failed"}
        
        #return test
        




def test_getDevOps():
    with app.app.app_context():    
        global bearer_token
        data = json.dumps({"message" : "This is a test", "to": "Juan Perez","from": "Rita Asturia","timeToLifeSec" : 45})
        response_login, bearer_token = post_login()
        bearer = "Bearer " + str(bearer_token)
        headers = {'Content-Type': 'application/json','X-Parse-REST-API-Key':'2f5ae96c-b558-4c7b-a590-a501ae1c3f6c',"Authorization": bearer}
        response = requests.post(SERVER_URL + "/DevOps", data=data, headers=headers)
        test = {}
        print(bearer)
        if response.status_code == 422:
            assert False, "Unprocessable entity"
        else:
            assert response.status_code == 200
        #if 200 == response.status_code:
        #    test = {"status" : "passed"}
        #else:
        #    test = {"status" : "failed"}
        
        #return test


def test_me():
    a = 3
    b = 3
    result = app.me(a,b)
    assert result == True

def test_always_passes():
    assert True


