#1. 집합자료형 set
s1=set([1,2,3])
print("s1 : "+str(s1))

s2=set("Hello")
print("s2 : " + str(s2))


#2. 집합자료형의 특징 
#중복을 허용하지 않는다
#순서가 없다
#따라서 set은 중복을 제거하는 필터역할로 종종 사용됨

#3. 교집합,합집합,차집합 구하기
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#교집합
print(s1&s2)
print(s1.intersection(s2))
#합집합
print(s1|s2)
print(s1.union(s2))#이때 중복된 값은 한개씩 표현됨
#차집합
print(s1-s2)
print(s1.difference(s2))
print(s2-s1)


#4. 집합자료형 관련 함수들
s1=set([1,2,3]) #값 1개 추가
s1.add(4)
print(s1)

s1.update([5,6,7]) #값 여러개 추가
print(s1)

s1.remove(2)
print(s1)