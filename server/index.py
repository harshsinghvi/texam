import flask
import json
from flask import make_response, request, jsonify
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo,ObjectId
from flask import render_template
from pytz import timezone
from datetime import datetime

import settings

IST = timezone('Asia/Kolkata') 

#  APP CONFIG 
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['MONGO_URI'] = settings.MONGODB_URI

mongo = PyMongo(app)
CORS(app, support_credentials=True)

# API resourses
@app.route('/', methods=['GET'])
def result():
    return render_template("result.html")

@app.route('/admin', methods=['GET'])
def admin():
    return render_template("admin.html")

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
    return {"questions":dict}

@app.route('/store-responses',methods=['GET','POST'])
def store_responses():
    que=mongo.db.responses
    ans=mongo.db.answers.find()[0]
    scores=mongo.db.scores
    temp=request.get_json()
    temp['timestamp']=str(datetime.now(IST))

    sc=0
    pen=int(temp['penalties'])

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
def delete_pattern(resource_type):
    pattern=request.get_json()
    res=str(resource_type)+" with "+str(pattern)
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

@app.route('/test-client-auth',methods=['GET','POST'])
def test_client_auth():
    auth=mongo.db.keys.find({"type":"client"})[0]
    if 'auth' not in request.args:
        return "<H1 style=\"color : red;\" > Unauthenticated </H1> "
    if auth['auth'] == request.args["auth"]:
        return "<H1 style=\"color : green;\" > Authenticated </H1> ",200
    return  "<H1 style=\"color : red;\" > wrong Authenticated </H1> ",200

@app.route('/test-admin-auth',methods=['GET','POST'])
def test_admin_auth():
    auth=mongo.db.keys.find({"type":"admin"})[0]
    if 'auth' not in request.args:
        return "<H1 style=\"color : red;\" > Unauthenticated </H1> "
    if auth['auth'] == request.args["auth"]:
        return "<H1 style=\"color : green;\" > Authenticated </H1> ",200
    return  "<H1 style=\"color : red;\" > wrong Authenticated </H1> ",200

@cross_origin()
@app.route('/new-question',methods=['GET','POST'])
def new_question():
    data=json.loads(request.data)
    que = {
        "id": data['id'],
        "que": data['que'], 
        "choices": data['choices']
    }
    ans = mongo.db.answers.find_one()

    ans[data['id']] = data['answer']

    if mongo.db.questions.insert_one(que).acknowledged and mongo.db.answers.update_one({"_id":ans["_id"]},{"$set":ans}):
        return "OK",200
    else:
        return "not OK", 500

@cross_origin()
@app.route('/delete-question',methods=['GET','POST'])
def del_question():
    data=json.loads(request.data)
    ans = mongo.db.answers.find_one()
    if mongo.db.questions.delete_many({"id":data['id']}).acknowledged and mongo.db.answers.update_one({"_id":ans["_id"]},{"$unset":{data["id"]:''}}):
        return "OK",200
    else:
        return "not OK", 500

@app.route('/delete-sample-data',methods=['GET','POST'])
def delete_sample_data():
    scores = mongo.db.scores.delete_many({"name":"Sample Data"})
    responses = mongo.db.responses.delete_many({"name":"Sample Data"})
    return "Delete OK",200

@cross_origin()
@app.route('/scores',methods=['GET'])
def scores():
    scores=mongo.db.scores.find()
    que=list(mongo.db.questions.find())
    data={ "scores": [] }
    for i in scores:
        i['uid']=str(i["_id"])
        i.pop("_id")
        data['scores'].append(i)
    data["scores"] = sorted(data['scores'] , key= lambda k:( int(k['total']), int(k['score']) ), reverse=True)
    data["max_marks"] =  4*(len(que))
    return data

@cross_origin()
@app.route('/admin-data',methods=['GET'])
def admin_data():
    que=list(mongo.db.questions.find())
    scores=list(mongo.db.scores.find())
    dbResponses=list(mongo.db.responses.find())
    ans=mongo.db.answers.find_one()
    answers = []
    
    for x in ans: 
        if x != '_id':
            answers.append({"id":x, "answer":ans[x]})
    for i in que:
        i.pop('_id')
    for i in scores:
        i.pop('_id')
    for i in dbResponses:
        temp = i['_id']
        i['id'] = str(temp)
        i.pop("_id")

    data = {
        "questions":que,
        "responses":dbResponses,
        "scores":scores,
        "answers":answers
    }
    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0")
