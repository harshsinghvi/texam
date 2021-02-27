from datetime import datetime 

while True: 
    d = datetime.now()
    if (d.second == 2 or d.second == 34 ) and  d.microsecond == 0:
        print(d.time())
