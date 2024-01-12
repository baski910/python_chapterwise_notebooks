# example for consuming a rest end point

# rest end point - https://reqres.in/api/users?pag2=2
# to install requests 
#       go to cmd
#       python -m pip install requests
import requests
import json

response = requests.get("https://reqres.in/api/users?page=2")

# http code for success - 200
# page not found - 404
# internal server error - 500

#print(response.status_code)
if response.status_code == 200:
    result = json.loads(response.text)
    #print(type(result))
    #print(result.get("data")) # result.get("data") returns a list and each element is a dictionary
    #print(result["page"])
    #print(result.get("page"))
    for obj in result.get('data'):
        #print(obj)
        print(obj["id"],obj['email'],obj['first_name'],obj['last_name'])
else:
    print("error acceessing the url")
