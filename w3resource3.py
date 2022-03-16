import json
dict={"name":"shabeera","age":21,"marks":80}
list=[20,30,40,50,60]
tuple=(5,10,15,20,25)
num=60
float=20.5
str="shabeera"
json_dict=json.dumps(dict)
json_list=json.dumps(list)
json_tuple=json.dumps(tuple)
json_num=json.dumps(num)
json_float=json.dumps(float)
print(json_dict,type(json_dict))
print(json_list,type(json_list))
print(json_tuple,type(json_tuple))
print(json_num,type(json_num))
print(json_float,type(json_float))
