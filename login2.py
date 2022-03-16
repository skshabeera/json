import json
n=int(input("enter that what you want to chose 1.signup ,2.login"))
def signup():
    name=input("enter the name")
    password=input("enter the password")
    con_password=input("enter the confirm password")
    def strong_password():
        l,u,p,d=0,0,0,0
        if len(password)>=8:
            for i in password:
                if (i.isupper()):
                    l=l+1
                if (i.islower()):
                    u=u+1
                if (i.isdigit()):   
                    p=p+1
                if (i=="@" or i=="#" or i=="$"):
                    d=d+1
        if(l>=1 and u>=1 and p>=1 and d>=1):
            print("valid password")
            file=open("user.json","r")
            a=json.load(file) 
            print(a)
        else:
            print("invalid password")
            print("your password should have one capital letter and small letter,numeric value,special character")
    strong_password()
    if password==con_password:
        print("your sign in is successfull")  
        user_name=input("enter the name")
        password=input("enter the password")
        gender=input("enter the female or male")
        description=input("enter the description")
        Dob=input("enter the date of birth")
        hobbies=input("enter the hobbies")
    details={"user":[{"user_name":user_name,"password":password,"con_password":con_password,"profile":{"gender":gender,"description":description,"Dob":Dob,"hobbies":hobbies}}]}
    details["user"].append(details)
    with open("details.json","w") as file:
        json.dump(details,file,indent=4)

def user_exit(data,user_name,password):
    for i in data["user"]:
        if user_name==i["user_name"] and password==i["password"]:
                 return True
def login():
    user_name=input("enter the username")
    password=input("enter the password" )
    with open("details.json","r") as file:
        data=json.load(file)
    print(data)
    check=user_exit(data,user_name,password)
    if check==True:
        print("your login is suceessful")
    else:
        print("your login is failed please try again")
if n==1 or n=="signup":
    signup()
if n==2 or n=="login":
    login()

    







    
                