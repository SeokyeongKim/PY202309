fp = open("./test_files/file1.txt","r",encoding="utf8")
lines =fp.readlines()
print("file1.txt 결과")
print("Readlines의 결과 : ", lines)
print()
for line in lines:
    print("\t각 line 들: ", line)
    tokens = line.split()
    print("\t\tline내 토큰들: ", tokens)
print()

fp = open("./test_files/file2.csv","r",encoding="utf8")
lines =fp.readlines()
print("file2.csv 결과")
print("Readlines의 결과 : ", lines)
print()
for line in lines:
    print("\t각 line 들: ", line)
    tokens = line.split()
    print("\t\tline 내 토큰을 공백으로 자르면.. :", tokens)
    tokens = line.split(",")
    print("\t\tline 내 토큰을 ,(쉼표)로 자르면.. :", tokens)
print()