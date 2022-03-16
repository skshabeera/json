import json
json_dict={"name":'shabeera',"age":20,"marks":80}
list=[2,3,5,7,9,10]
string="shabeera"
float=20.0
num=9
py_dict=json.loads(json_dict)
py_list=json.loads(list)
py_str=json.loads(string)
py_float=json.loads(float)
py_num=json.loads(num)
print(py_dict)
print(py_list)
print(py_str)
print(py_float)
print(py_num)
