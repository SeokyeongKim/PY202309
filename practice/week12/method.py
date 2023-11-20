할일 = ["기상", "식사","책읽기","식사"]

print("책읽기의 인덱스는 {} 입니다.".format(할일.index("책읽기")))
print("할일 중 식사는 {}번 있습니다.".format(할일.count("식사")))

할일.append("운동")
print(할일)

할일.extend(['게임','잠'])
print(할일)