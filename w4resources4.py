import json
data={
    '4': 5, 
    '6': 7,
    '1': 3, 
    '2': 4}
b=json.dumps(data,sort_keys=True)
print(b)  