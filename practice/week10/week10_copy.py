# 1. 파일 읽기
fp = open("./week10_test.txt","r",encoding="utf8")
lines =fp.readlines()
fp.close()

# 2. 파일 쓰기 with write
writer_fp = open("./week10_test_copy_write.txt","w",encoding="utf8")
for line in lines:
    writer_fp.write(line)
writer_fp.close()

# 3. 파일 쓰기 with writelines
writer_fp = open("./week10_test_copy_writelines.txt","w", encoding="utf8")
writer_fp.writelines(lines)
writer_fp.close()


