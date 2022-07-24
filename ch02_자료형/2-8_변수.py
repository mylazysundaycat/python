#1. 변수
#자료형의 값을 저장하는 공간

a=1
b='hello'
c=[1,2,3] #여기서 a,b,c를 변수라고 한다

print(id(a)) #a변수가 가리키는 메모리의 주소

a=[1,2,3]
b=a #변수b에 변수a가 참조하는 메모리의 주소를 대입

print(a is b) #a와 b가 가리키는 객체는 동일한가?


#2. a변수의 값을 가져오며 a와 다른 주소를 가리키도록만들기
#[:] 이용
a=[1,2,3]
b=a[:]

print(a is b)

#copy 모듈 이용
from copy import copy

a=[1,2,3]
b=copy(a)

print(a is b)


#3. 변수를 만드는 여러가지 방법
a, b=('1','a')
print(1)
[a,b]=['1','a']
print(a)

a=3
b=5
print(a,b)
a,b=b,a # 두 변수의값을 바꾸기
print(a,b)