import requests
#import json
#import jsonify


class Request_error:
    pass

URL = 'https://online-exam-pi.vercel.app'
#URL = 'http://localhost:5000'

def get_questions():
    req = requests.get(URL+'/questions')
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
        return req.text
    else:
        raise Request_error

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
        "email": "Harsh",
        "name": "Harsh",
        "responses": {
            "101": "1",
            "201": "2",
            "301": "4",
            "401": "3"
        },
        "timestamp": "2020-10-20 21:19:04.190268",
        "uid": "5f8f06f08efd58423bedc2c5"
    },
    {
        "email": "Harsh",
        "name": "Harsh",
        "responses": {
            "101": "1",
            "201": "2",
            "301": "4",
            "401": "3"
        },
        "timestamp": "2020-10-20 21:19:58.667720",
        "uid": "5f8f07267a259a5192fc2cbe"
    },
    {
        "email": "Harsh",
        "name": "Harsh",
        "responses": {
            "101": "1",
            "201": "2",
            "301": "4",
            "401": "3"
        },
        "timestamp": "2020-10-20 21:44:29.756754",
        "uid": "5f8f0ce5b5350ade22e49de4"
    },
    {
        "email": "Harsh",
        "name": "Harsh",
        "responses": {
            "101": "1",
            "201": "2",
            "301": "4",
            "401": "3"
        },
        "timestamp": "2020-10-20 21:46:40.983758",
        "uid": "5f8f0d6829175530e1142e70"
    },
    {
        "email": "Harsh",
        "name": "Harsh",
        "responses": {
            "101": "1",
            "201": "2",
            "301": "4",
            "401": "3"
        },
        "timestamp": "2020-10-21 11:59:59.718253",
        "uid": "5f8fd567cfd89ead5df53327"
    },
    {
        "email": "Harsh",
        "name": "Harsh",
        "responses": {
            "101": "1",
            "201": "2",
            "301": "4",
            "401": "3"
        },
        "timestamp": "2021-01-28 16:11:52.597323",
        "uid": "6012e248ac4b558ced8cf1f1"
    },
    {
        "email": "Harsh",
        "name": "Harsh",
        "responses": {
            "101": "1",
            "201": "2",
            "301": "4",
            "401": "3"
        },
        "timestamp": "2021-01-31 06:48:31.346862",
        "uid": "601652bf8f4cdf16a1ade555"
    },
    {
        "email": "Harsh",
        "name": "Harsh",
        "responses": {
            "101": "1",
            "201": "2",
            "301": "4",
            "401": "3"
        },
        "timestamp": "2021-01-31 12:27:19.419715",
        "uid": "601654cfbc4e71937190d94b"
    },
    {
        "email": "Harsh",
        "name": "Harsh",
        "responses": {
            "101": "1",
            "201": "2",
            "301": "4",
            "401": "3"
        },
        "timestamp": "2021-01-31 12:30:21.435059",
        "uid": "60165585bc4e71937190d94c"
    }
]