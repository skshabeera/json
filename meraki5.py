import json
data='{"name":"shabeera","age":20,"marks":80.0,"bool":true}'
b=json.loads(data)
print(type(b))