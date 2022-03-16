import json
shopping={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
item=input("enter the item:")
no=int(input("how many item:"))
c=shopping["shopping_list"][item]
rem=int(c)-no
shopping["shopping_list"][item]=rem
b=json.dumps(shopping,indent=4)
print(b)