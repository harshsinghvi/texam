temp = {
        "email": "email@email.com",
        "name": "Sample Data",
        "penalties": "3",
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

ans = {
    
    "101": '[1, 2, ‘hello’]', 
    '201': '34.000000', 
    '301': '27.2',
    '401': 'Class',
    '501': '^'
}



sc=0
pen= int(temp['penalties'])

for i in temp['responses']:
    if temp['responses'][i] == ans[i]:
        print(temp['responses'][i] + " correct")
        sc = sc + 4
    elif temp['responses'][i] == None:
        pass
    else: 
        print(temp['responses'][i] + " wrong")
        sc = sc -1

score={ 
    "name":"Sample data",
    "score":str(sc),
    "penalties": str(pen),
    "total":str( sc - int(pen / 3) )
}

print(score)