import json
data={"Name":"Ram", 
     "Class":"IV", 
     "Age":9}
b=json.dumps(data)
print(b)
print(type(b))