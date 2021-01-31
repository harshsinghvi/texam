import flask
import json
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo

from datetime import datetime
import settings

#  APP CONFIG 
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['MONGO_URI'] = settings.MONGODB_URI

mongo = PyMongo(app)
CORS(app, support_credentials=True)


# API resourses
@app.route('/', methods=['GET'])
def home():
    return "<h1>Doccumentation</h1><p>This site is a prototype API for online assisment and forms collection.</p><br><h2>Use Following Resources:- </h2> <h3>/questions</h3><h3>/store-responses</h3><h3>/get-data</h3><h3>/test-connection</h3><h3>/scores</h3><h3>/delete</h3>"

@app.route('/questions',methods=['GET'])
def questions():
    que=mongo.db.questions.find()
    dict=[]
    for i in que:
        temp={
            'uid':str(i['_id']),
            'id':i['id'],
            'que':i['que'],
            'choices':i['choices']
        }
        dict.append(temp)
    return jsonify(dict)

@app.route('/store-responses',methods=['GET','POST'])
def store_responses():
    que=mongo.db.responses
    ans=mongo.db.answers.find()[0]
    scores=mongo.db.scores
    temp=request.get_json()
    temp['timestamp']=str(datetime.now())

    sc=0
    pen= int(temp['penalties'])

    for i in temp['responses']:
        if temp['responses'][i] == ans[i]:
            sc = sc + 4
        else: 
            sc = sc -1

    score={ "name":"Sample data","score":str(sc),"penalties": str(pen),"total":str( sc - int(pen / 3)) }
    if que.insert_one(temp).acknowledged and scores.insert_one(score).acknowledged:
        score.pop("_id") 
        return score,200
    return "ERROR",404

@app.route('/get-data',methods=['GET','POST'])
def get_data():
    dbResponses=mongo.db.responses.find()
    dict=[]
    for i in dbResponses:
        temp={
            'uid':str(i['_id']),
            'name':i['name'],
            'email':i['email'],
            'timestamp':i['timestamp'],
            'responses':i['responses'],
            'penalties':i['penalties']
        }
        dict.append(temp)
    return jsonify(dict)

@app.route('/delete/<resource_type>/<resource_uid>',methods=['DELETE'])
def delete(resource_type,resource_uid):
    # try:
    if resource_type in ["question","que"]:
        mongo.db.questions.delete_one({"_id" : resource_uid})
        message=str(resource_type)+" "+str(resource_uid)+": Delete OK"
        return message,400        
    if resource_type in ["response","res"]:
        mongo.db.responses.delete_one({"_id" : resource_uid})
        message=str(resource_type)+" "+str(resource_uid)+": Delete OK"
        return message,400
    else: 
        raise
    # except None:
    #     message=str(resource_type)+" "+str(resource_uid)+": Is invalid"
    #     return message,400
    return "Unexpected Error",400
    
@app.route('/test-connection',methods=['GET','POST'])
def func():
    return "OK",200

@app.route('/scores',methods=['GET','POST'])
def scores():
    scores=mongo.db.scores.find()
    data={"scores": [] }
    for i in scores:
        i.pop("_id")
        data['scores'].append(i)
    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0")
