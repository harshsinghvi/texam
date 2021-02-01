import flask
import json
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo,ObjectId
from flask import render_template

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
def index():
    return render_template("index.html")

@app.route('/responses', methods=['GET'])
def responses():
    return render_template("responses.html")

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
        elif temp['responses'][i] == '':
            pass
        else: 
            sc = sc -1

    score={ "name":temp["name"],"score":str(sc),"penalties": str(pen),"total":str( sc - int(pen / 3)) }
    if que.insert_one(temp).acknowledged and scores.insert_one(score).acknowledged:
        score["uid"]=str(score["_id"])
        score.pop("_id")
        return score,200
    return "ERROR",404

@cross_origin()
@app.route('/get-data',methods=['GET'])
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
    dict.reverse()
    return jsonify(dict)


@app.route('/delete/<resource_type>/<resource_uid>',methods=['GET','POST'])
def delete(resource_type,resource_uid):
    res=str(resource_type)+" "+str(resource_uid)
    if resource_type in ["question","que"]:
        mongo.db.questions.delete_one({"_id" : ObjectId(resource_uid)})
    elif resource_type in ["answer","ans"]:
        mongo.db.answers.delete_one({"_id" : ObjectId(resource_uid)})
    elif resource_type in ["score","sc"]:
        mongo.db.scores.delete_one({"_id" : ObjectId(resource_uid)})
    elif resource_type in ["response","res"]:
        mongo.db.responses.delete_one({"_id" : ObjectId(resource_uid)})
    else: 
        return res+ ": NO Resource found",400
    return  res + ": Delete OK",200   

@app.route('/delete/<resource_type>',methods=['POST'])
def delete(resource_type):
    res=str(resource_type)+" "+str(resource_uid)
    pattern=request.get_json()
    if resource_type in ["question","que"]:
        mongo.db.questions.delete_many(pattern)
    elif resource_type in ["answer","ans"]:
        mongo.db.answers.delete_many(pattern)
    elif resource_type in ["score","sc"]:
        mongo.db.scores.delete_many(pattern)
    elif resource_type in ["response","res"]:
        mongo.db.responses.delete_many(pattern)
    else: 
        return res+ ": NO Resource found",400
    return  res + ": Delete OK",200   

@app.route('/test-connection',methods=['GET','POST'])
def func():
    return "OK",200

@app.route('/delete-sample-data',methods=['GET','POST'])
def delete_sample_data():
    scores = mongo.db.scores.delete_many({"name":"Sample Data"})
    responses = mongo.db.responses.delete_many({"name":"Sample Data"})
    return "Delete OK",200

@cross_origin()
@app.route('/scores',methods=['GET'])
def scores():
    scores=mongo.db.scores.find()
    data={ "scores": [] }
    for i in scores:
        i['uid']=str(i["_id"])
        i.pop("_id")
        data['scores'].append(i)
    data["scores"] = sorted(data['scores'] , key= lambda k:( int(k['total']), int(k['score']) ), reverse=True)
    data["max_marks"] =  20
    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0")
