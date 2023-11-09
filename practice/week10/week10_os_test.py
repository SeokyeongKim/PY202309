import os

in_fp = None
file_name, in_lines, in_str = "",[],""

file_name = "./test_files/file1.txt"
if os.path.exists(file_name) == True:
    in_fp = open(file_name,"r",encoding="utf8")

    in_lines = in_fp.readlines()
    for in_str in in_lines:
        print(in_str,end="")

    in_fp.close()
else:
    print("파일이 없습니다.",file_name)