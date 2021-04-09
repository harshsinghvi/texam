import requests
#import json
#import jsonify

QUESTION = 'que'
SCORES = 'sc'
RESPONSES = 'res'
ANSWER = 'ans'

class Request_error:
    pass

URL = 'https://texam.projects.harshsinghvi.com'
# URL = 'http://localhost:5000'

def get_questions():
    req = requests.get(URL+'/questions')
    if req.status_code == 200:
        return req.json()['questions']
    else:
        raise Request_error

def get_admin_data():
    req = requests.get(URL+'/admin-data')
    if req.status_code == 200:
        return req.json()
    else:
        raise Request_error
    
def get_response_data():
    req = requests.get(URL+'/get-data')
    if req.status_code == 200: 
        return req.json()
    else:
        raise Request_error

def test_connection():
    req = requests.get(URL+'/test-connection')
    if req.status_code == 200: 
        return req.text
    else:
        raise Request_error

def post_responses(data):
    req = requests.post(URL+'/store-responses',json=data)
    if req.status_code == 200:  
        return req.json()
    else:
        raise Request_error
def get_scores():
    req = requests.get(URL+'/scores')
    if req.status_code == 200:  
        return req.json()
    else:
        raise Request_error

def delete_sample_data():
    req = requests.get(URL+'/delete-sample-data')
    if req.status_code == 200:  
        return req.text
    else:
        raise Request_error

def delete_one(resource_type, resource_uid):
    req = requests.post(URL+'/delete/{}/{}'.format(resource_type,resource_uid))
    if req.status_code == 200:  
        return req.text
    else:
        raise Request_error

def delete_many(resource_type, data):
    req = requests.post(URL+'/delete/{}'.format(resource_type),json=data)
    if req.status_code == 200:  
        return req.text
    else:
        raise Request_error

def delete_data(data):
    print(delete_many(RESPONSES,data))
    print(delete_many(ANSWER,data))
	
# post_responses
sample_data={

    "email"    : "email@email.com",
    "name"      : "Sample Data",
    "responses" : {
                    "101": "[1, 2, ‘hello’]", 
                    "201": "34.000000", 
                    "301": "27.2", 
                    "401": "Class",
                    "501": "^"
                },
    "penalties": "2"
}

# get questions

questions=[
    {
        "choices": [
            "[1, 0, 2, ‘hello’, '', []]",
            "Error",
            "[1, 2, ‘hello’]",
            "[1, 0, 2, 0, ‘hello’, '', []]"
        ],
        "id": "101",
        "que": "What will be the output of the following Python code? \nl=[1, 0, 2, 0, 'hello', '', []] \nlist(filter(bool, nl))"
    },
    {
        "choices": [
            "34.00",
            "34.000000",
            "34.0000",
            "34.00000000"
        ],
        "id": "201",
        "que": "What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)"
    },
    {
        "choices": [
            "30.8",
            "27.2",
            "28.4",
            "30.0"
        ],
        "id": "301",
        "que": "What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10"
    },
    {
        "choices": [
            "Tuples",
            "Dictionary",
            "Lists",
            "Class"
        ],
        "id": "401",
        "que": "Which of these in not a core data type?"
    },
    {
        "choices": [
            "&",
            "!",
            "^",
            "|"
        ],
        "id": "501",
        "que": "Which of the following represents the bitwise XOR operator?"
    }
]
# Get Response data

response_data = [
    {
        "email": "email@email.com",
        "name": "Sample Data",
        "penalties": "2",
        "responses": {
            "101": "[1, 2, ‘hello’]",
            "201": "34.000000",
            "301": "27.2",
            "401": "Class",
            "501": "^"
        },
        "timestamp": "2021-01-31 13:21:21.244648",
        "uid": "6016617922d40e8cc43159bf"
    },
    {
        "email": "email@email.com",
        "name": "Sample Data",
        "penalties": "2",
        "responses": {
            "101": "[1, 2, ‘hello’]",
            "201": "34.000000",
            "301": "27.2",
            "401": "Class",
            "501": "^"
        },
        "timestamp": "2021-01-31 13:22:26.432631",
        "uid": "601661ba22d40e8cc43159c0"
    }
]
