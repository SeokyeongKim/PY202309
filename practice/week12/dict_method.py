name = input("name : ")
age = int(input("age : "))

iden = {"name":name , "age":age}

for k in iden.keys():
    print("- key : ", k)


for v in iden.values():
    print("- value : ", v)

addr = input("address : ")
iden["addr"] = addr
print(iden)