from admin import * 

data = get_response_data()
scores = get_scores()

i = 0
NAME_SIZE = 20
EMAIL_SIZE = 25
TOTAL_SIZE = 5
print("_"*(NAME_SIZE+EMAIL_SIZE+TOTAL_SIZE+12))
while True:
    try :
        print("|-> {} | {} | {} |".format(data[i]['name']+" "*(NAME_SIZE - len(data[i]['name'])), data[i]['email']+" "*(EMAIL_SIZE - len(data[i]['email'])),scores['scores'][i]['total']+" "*(TOTAL_SIZE - len(scores['scores'][i]['total']))))
        i = i + 1
    except IndexError: 
        break
print("-"*(NAME_SIZE+EMAIL_SIZE+TOTAL_SIZE+12))
