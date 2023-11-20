my_string = "파이썬은 재미있어요, 파이썬만 매일 하고 싶어요."
str_pos_list = []
index = 0

while True:
    try:
        index = my_string.index("파이썬",index)
        str_pos_list.append(index)
        index = index + 1
    except:
        break

print("파이썬 글자 위치 모음 : ",str_pos_list)
