import json
data = '''{
    "name":"Chuck",
    "phone":{
        "type":"int1",
        "number":"+13456787654"
    }
    "email":{
        "hide":"yes"
    }
}'''

info = json.loads(data)
print(info)
# print('Name:',info["name"])
# print('Hide:',info["email"]["hide"])
