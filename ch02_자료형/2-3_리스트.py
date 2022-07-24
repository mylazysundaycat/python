
#리스트
odd=[1,3,5,7,9] # 리스트명=[요소1,요소2,요소3]
a=[] # a=list()
b=[1,2,3]
c=['life','is','too','short']
d=[1,2,['life','is']]



#리스트 인덱싱
a=[1,2,3]
print(a[0])
print(a[0]+a[2])

a=[1,2,3,['a','b','c']] #리스트 안의 리스트
print(a[-1])
print(a[-1][0]) #a[-1][0] < 리스트 안의 리스트의 첫번째 요소 꺼냄




#리스트 연산
print(str(a[2])+"hi") #리스트형인 a를 string으로 변형 후 문자열과 연산




#리스트 수정과 삭제
a=[1,2,3]
a[2]=7
print("a : "+str(a))
del a[2] #삭졔: del 객체
print("a : "+str(a))



#리스트 요소 추가
a=[1,2,3]
a.append(4)
print("a : "+str(a))
a.append([5,6])
print("a : "+str(a))



#리스트 정렬
a=[1,6,3,9,8,7]
a.sort() #sort()
print(a)



#리스트 뒤집기
a.reverse() #reverse()
print(a)



#위치 찾아주기
a=[1,2,3]
b=a.index(2) #index()
print("숫자 2의 위치는 "+str(b)+" 번째")



#요소 삽입
a=[1,2,3]
a.insert(0,"POP") #insert(a,b) a번째에 b를 삽입함
print(a)



#리스트 요소 제거
a.remove(2) #remove(a) a가 있으면 삭제하라는 뜻이다.
print(a)



#리스트 맨 마지막 요소 끄집어내기
a=[1,2,3]
a.pop()
print(a)

b=[1,2,3,4,5,6]
b.pop(1) #pop(x) x번째 요소 꺼내버림, 그리고 요소를 삭제함
print(b)



#리스트에 포함된 요소 x의 갯수 세기
a=[1,2,3,4,6,7,1,2,5,1,1,6,2,3]
print("1의 갯수 : "+str(a.count(1)))



#리스트 확장
a=[1,2,3]
a.extend([4,5]) #extend 함수에는 리스트만 들어갈 수있다.
print(a)