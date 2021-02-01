import requests

class Request_error:
    pass

URL = 'https://texam.projects.harshsinghvi.com'
# URL = 'http://localhost:5000'

def test_connection():
    req = requests.get(URL+'/test-connection')
    if req.status_code == 200: 
        return req.text
    else:
        raise Request_error

def get_questions():
    req = requests.get(URL+'/questions')
    if req.status_code == 200:
        return req.json()
    else:
        raise Request_error

def post_responses(data):
    req = requests.post(URL+'/store-responses',json=data)
    if req.status_code == 200:  
        return req.json()
    else:
        raise Request_error

# post_responses
sample_data={

    "email"    : "email@email.com",
    "name"      : "Sample Data",
    "responses" : {
                    "101": "Error", 
                    "201": "34.0000", 
                    "301": "7.2", 
                    "401": "Clss",
                    "501": "!"
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
    }  
]