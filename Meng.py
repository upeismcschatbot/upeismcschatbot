from wit import Wit
AT = "5Z3CEHTOAGRSHCA5MU7CFWHXSOAPDBM2"
client = Wit(access_token = AT)

def tableselecter():
    """ an function of table selecter, choose which table need to be use"""
    return "table1"
    

while True: 
    MT = "who is the teacher of CS-111"

    resp = client.message(MT)

    print(resp)
    print()
    i = 0
    while 1:
        try:
            print(resp['entities']['pname'][i]['value'])
            i+=1
        except:
            break

    i = 0
    while 1:
        try:
            print(resp['entities']['course'][i]['value'])
            i+=1
        except:
            break
        

    i = 0
    while 1:
        try:
            print(resp['entities']['intent'][i]['value'])
            i+=1
        except:
            break
"""
    i = 0
    while 1:
        try:
            resp['entities']['pname'][i]['value']
            i+=1
            intent = "professorname"
            
        
            

    i = 0
    while 1:
        try:
            limit = "course = "+resp['entities']['course'][i]['value']
            i+=1
            
            
        except:
            break
            
    query = "select " + intent + " from " + tableselecter() + " where " + limit
"""

   
