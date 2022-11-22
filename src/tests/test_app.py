import pytest
import lib.app as app
import requests

SERVER_URL = "192.168.1.7:8080"
bearer_token = 0

@pytest.fixture(scope="module", autouse=True)
def test_app(self):
    app = app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app
    #login(app)
    #getDevOps(app)

    # clean up / reset resources here

@pytest.fixture(scope="module", autouse=True)
def test_login(self):
    global bearer_token
    response = requests.post(SERVER_URL + "/login", data={"name":"Lorde", "password": "Team"}, headers={'Content-Type': 'application/json','X-Parse-REST-API-Key':'2f5ae96c-b558-4c7b-a590-a501ae1c3f6c'})
    test = {}
    json_obj = response.json()
    bearer_token = json_obj['access_token']
    assert response.status_code == 200
    #if 200 == response.status_code:
    #    test = {"status" : "passed"}
    #else:
    #    test = {"status" : "failed"}
    
    #return test
        



@pytest.fixture(scope="module", autouse=True)
def test_getDevOps(self):
    global bearer_token
    data = {"message" : "This is a test", "to": "Juan Perez","from": "Rita Asturia","timeToLifeSec" : 45}
    headers = {'Content-Type': 'application/json','X-Parse-REST-API-Key':'2f5ae96c-b558-4c7b-a590-a501ae1c3f6c',"Authorization": "Bearer " + bearer_token}
    response = requests.post(SERVER_URL + "/DevOps", data=data, headers=headers)
    test = {}
    assert response.status_code == 200
    #if 200 == response.status_code:
    #    test = {"status" : "passed"}
    #else:
    #    test = {"status" : "failed"}
    
    #return test

