import json
b=open("text.txt","r")
c=b.readlines()
with open("meraki7.json","w")as file:
    json.dump(c,file,indent=4)
