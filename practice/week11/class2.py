class 참치선물세트():
    일반 = 0
    야채 = 0
    고추 = 0

    def 출력(self, 이름):
        print(f"** {이름} **")
        print(f"일반 참치 : {self.일반}")
        print(f"야채 참치 : {self.야채}")
        print(f"고추 참치 : {self.고추}")
    
    def 출력2(self):
        self.출력("참치종합세트")


    def 총합(self,이름):
        합 = self.일반 + self.야채 + self.고추
        return 이름 + str(합)

참01호 = 참치선물세트()
참01호.일반 = 12
참01호.야채 = 3
참01호.고추 = 3

출력값 = 참01호.출력("참치종합세트")
출력값2 = 참01호.출력2()
print(출력값2)