import requests 

r = requests.get(url="https://texam.projects.harshsinghvi.com/scores")

data=r.json()

sorted_data = sorted(data['scores'] , key= lambda k:( int(k['total']), int(k['score']) ), reverse=True)


for i in range(40):
    print(data['scores'][i]['name'] + " " + data['scores'][i]['score'] + " " + data['scores'][i]['total'] + "  |   " + sorted_data[i]['name'] + " " + sorted_data[i]['score'] + " " + sorted_data[i]['total'] )