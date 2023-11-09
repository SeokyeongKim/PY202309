import shutil
import os

source_file_path = "./test_files/file1.txt"
new_file_path = "./shutil_file1.txt"

shutil.copy(source_file_path, new_file_path)
print("첫 번째 copy 완료")

os.mkdir("./copied_files/")
source_file_path = "./test_files/file1.txt"
new_file_path = "./copied_files/shutil_file1.txt"
shutil.copy(source_file_path, new_file_path)
print("두 번째 copy 완료") 