# from practice.week12.참치공장.참치선물세트클래스 import *
# from practice.week12.참치공장.공장설명 import *
#import 참치선물세트클래스 as 참클
#import 공장설명 as 공설
import 참치공장.참치선물세트클래스 as 참클
import 참치공장.공장설명 as 공설



공설.인사말출력()
print('공장 설립은 {}에 했습니다.'.format(공설.공장설립연도))

참01호 = 참클.참치선물세트(12,3,3)
참01호.출력('참치선물세트 01호')