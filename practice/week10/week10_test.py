#print("hello world")

fp = open("./week10_test.txt","r",encoding="utf8")
lines =fp.readlines()
print("Readlines의 결과 : ", lines)
print()
for line in lines:
    print("\t각 line 들: ", line)
    tokens = line.split()
    print("\t\tline내 토큰들: ", tokens)