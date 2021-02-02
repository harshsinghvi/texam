from admin import * 

data = get_questions()

resp={    
    "email"    : "email@email.com",
    "name"      : "Sample Data",
    "responses" : {},
    "penalties": "2"
    }

for i in data:
    print("QUESTION "+ i['id'] +" : "+ i['que'])
    for j in i['choices']:
        print("                                 "+j)
    print("enter choice ")
    c = input()
    resp['responses'][i['id']]=c

print(resp)

post_responses(resp)