#문자열 포매팅
#1. 바로대입

a="i eat %d apples." %3
print(a)
b="i eat %s apples" %"four"
print(b)

#2. 두개 이상 값 넣기
number=10
day="three"
talk="i ate %d apples. so i was sick for %s days." %(number, day)
print(talk)




#포맷 코드
#1. 정렬과 공백
c="%10s"%"hi"
print(c)

#2. 소수점 표현
d="%0.4f"%3.41238387 #4번째 짜리까지만 표현
print(d)




#format함수 이용
#1. 변수대입
e="i eat {0} apples".format(3)
print(e)

#2. 정렬
f="{0:>20}".format("hi") #오른쪽정렬
print(f)
g="{0:^10}".format("hi") #가운데정렬
print(g)
h="{0:♡<10}".format("hi") #공백 원하는 문자로 채우기
print(h)
