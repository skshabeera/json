import json
name=input("enter the name")
password=int(input("enter the password"))
d={}
while True:
    d["name"]=name
    d["password"]=password
    c=json.dumps(d,indent=4)
print(c)

