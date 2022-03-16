import json
list1=["neelam","programer","24","2400"]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"] 
list=["name","desigination","age","salary"]
dict1={}
dict2={}
dict3={}
dict4={}
dic={}
i=0
while i<len(list1):
    dict1[list[i]]=list1[i]
    dict2[list[i]]=list2[i]
    dict3[list[i]]=list3[i]
    dict4[list[i]]=list4[i]
    i+=1
dic["em1"]=dict1
dic["em2"]=dict2
dic["em3"]=dict3
dic["em4"]=dict4
c=json.dumps(dic)
print(c)
print(type(c))
with open("meraki8.json","w") as file:
    json.dump(dic,file,indent=4)