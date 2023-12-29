s_username="Anandan"
s_password="123"
uname=input("Enter a username : ")
password=input("Enter a password : ")

def validate():
    if(uname==s_username and password==s_password):
        return "True"
    else:
        return "False"
msg = validate()
print(msg)


