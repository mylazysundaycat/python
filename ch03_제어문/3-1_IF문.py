#1. if문
#if 조건문 : 수행문장.... else : 수행문장....

money = True
if money:
    print("택시를 타고")
    print("가세요!")
else:
    print("돈 없으니 걸어가세요!")
    #조건문이란 참과 거짓을 판단하는 문장이다.
    #money=True가 조건문이 된다.



#2. 비교연산자
#x==y : x와 y가 같다
#x!=y : x와 y가같지않다



#3. and or not 연산자
#x or y : x와 y 둘중에 하나만 참이어도 참이다
#x and y : x와 y 모두 참이여야 참이다
#not x : x가 거짓이면 참이다

money = 2000
card = True

if money >= 3000 or card:
    print("택시를 타라")
else:
    print("걸어가라")

if money >= 3000 or card:
    pass
else:
    print("걸어가라")


#elif

pocket = ['buds2','coin']
card = True

if money in pocket:
    print("택시를 타고 가라")
elif card:
    print("버스를 타고가라")
else:
    print("걸어가라")



#4. 조건부 표현식
score=95
message = "A+" if score>=90 else "F"
print(message)
#조건문이 참인경우 if 조건문 else 조건문이 거짓인 경우