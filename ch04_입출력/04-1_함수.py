#1. 함수
#함수란 반복적으로 사용되는 가치있는 부분을
#한 뭉치로 엮어주는 것이다.

def add(a,b):
    return a+b
#이 함수이름은 add이고 2개의 값을 받아서
#결과값은 2개의 값을 더해서 돌려준다.

print(add(1,3))




#------------------------------------------------------#




#2. 매개변수와 인수
#매개변수(parameter): 함수에 입력으로 전달된 값을 받는 변수 a,b
#인수(arguments): 함수를 호출할때 전달하는 입력값 1,3
#함수는 입력값을 받아 어떤 처리를 하여 결괏값을 돌려준다




#------------------------------------------------------#





#3. 입력값과 결괏값에 따른 함수의 형태
#1) 일반적인 함수
def add(a,b):
    return a+b

#2) 입력값이 없는 함수
def say():
    return "Python"
print(say())

#3) 결괏값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다."%(a,b,a+b))
    #return값이 없음
a=add(1,3)
print(a)

#4) 입력값도 결괏값도 없는 함수
def say():
    print('Hi')
say()




#------------------------------------------------------#




#4. 매개변수 지정하여 호출하기
def add(a,b):
    return a+b

result=add(a=3,b=7)
print(result)
result=add(b=5,a=7) #매개변수를 지정하면 변수 순서에 구애받지 않는다.
print(result)




#------------------------------------------------------#




#5. 입력값이 몇개가 될지 모를 때는 어떻게 해야할까?
def add_many(*args):
    result=0
    for i in args:
        result=result+i
    return result
# *args처럼 매개변수 이름 앞에 *를 붙이면
# 입력값을 전부 모아서 튜플로 만들어준다. [중복 삭제]

result = add_many(1,5,7,1,23,453,5,)
print(result)

def add_mul(choice,*args):
    if choice == "+":
        result = 0
        for i in args:
            result = result + i
    elif choice == "x":
        result = 1
        for i in args:
            result = result * i
    return result


a = add_mul("+",1,3,5,6,1,3,3,4)
print(a)
b = add_mul("x",3,5,78,3,2)
print(b)
    



#------------------------------------------------------#




#6. 키워드 파라미터 kwargs
def print_kwargs(**kwarge):
    print(kwarge)
print_kwargs(a=1) #딕셔너리 형태로 출력해줌
#key=value 형태




#------------------------------------------------------#




#7. 함수의 결괏값은 언제나 하나이다.
def add_and_mul(a,b):
    return a+b, a*b
print(add_and_mul(1,3))
#return에 두개를 넣었어도 하나의 튜플로 출력됨




#------------------------------------------------------#




#8. 매개변수에 초깃값 미리 설정하기
def say_myself(name,old,man=True): #매개변수=True
    print("나의 이름은 %s입니다."%name)
    print("나이는 %d살입니다."%old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("김석진",30)
say_myself("비비",27,False)
#초기화 시키고싶은 매개변수를 항상 뒤쪽에 놓을것




#------------------------------------------------------#




#9. 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a=a+1
vartest(a)
print(a)




#------------------------------------------------------#




#10. 함수 안에서 함수 밖의 변수를 변경하는 방법
#return 명령어 사용
a = 1
def vartest(a):
    a=a+1
    return a
a = vartest(a)
print(a)

#global 명령어 사용
a = 1
def vartest():
    global a
    a = a+1
vartest()
print(a)
#global a 문장은 함수 안에서 함수 밖의 변수 a를
#직접 사용하겠다는 뜻이다.




#------------------------------------------------------#




#11. lambda
# 함수를 생성할때 사용하는 예약어로 def와 동일한
# 역할을 한다.
# lambda 매개변수1, 매개변수2 : 표현식

add = lambda a, b : a+b
print(add(3,2))
#return 명령어가 있는것과 마찬가지이다