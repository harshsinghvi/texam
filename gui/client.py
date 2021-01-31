import requests
import json 
import jsonify 
class Request_error:
    pass

URL = 'https://online-exam-pi.vercel.app'
# URL="xyz"
# r =requests.get(URL+'/get-data')

# data = json.loads(r.json())

# print(data)
# r.ok()
# r.close()
# r.text()

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
        return req.json()
    else:
        raise Request_error

def post_responses(data):
    req = requests.post(URL+'/store-responses',data=jsonify.json(data))
    if req.status_code == 200: 
        return req.text()
    else:
        raise Request_error
sample_data={
    "email:"    : "email@email.com",
    "name"      : "Sample Data",
    "responses" : {
                    "101": "1", 
                    "201": "2", 
                    "301": "4", 
                    "401": "3"
                } 
}