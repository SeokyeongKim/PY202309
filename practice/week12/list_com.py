# a = [1,2,3,4]
# res = [num*3 for num in a if num%2 ==0] 
# print(res)

# res = [x*y for x in range(2,10) for y in range(1,10)]
# print(res)

# def mul(m):
#     def wrapper(n):
#         return m*n
#     def wrapper_2(n):
#         return m*n*n
    
#     return wrapper, wrapper_2

# if __name__ == "__main__":
#     mul3, mul33 = mul(3)
#     # mul5 = mul(5)

#     print(mul3(10))
#     print(mul33(10))

# import time

# def elapsed(original_func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = original_func(*args, **kwargs)
#         end = time.time()
#         print("함수 수행 시간 : %f초" %(end-start))
#         return res
#     return wrapper

# @elapsed
# def test(msg):
#     print("%s 을 출력합니다." %msg)

# test("You need Python")

class Mylterator:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result
    
if __name__ == "__main__":
    i = Mylterator ([1,2,3])
    for item in i:
        print(item)