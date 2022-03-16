import json
data=[{"id":21,"name":"shabeera","college":"mallikarjuna college"},{"id":21,"name":"shailaja","college":"sri chaitanya college"},{"id":23,"name":"thanjum","college":"ng college"}]
index=int(input("enter the position"))
id=int(input("enter the id"))
name=input("enter the name")
college=input("enter the college")
c=json.loads(data)
for i in data[index]:
        if i=="id":
            print(data["id"]["index"])=id
        if i=="name":
            print([data]["index"])=name
        if i=="college":
            print([data]["index"])=college
print(c)
