#리스트

a = ["강아지","고양이","토끼","코끼리"]

del a[0]

print(a)


#리스트에 요소추가

a.append("에바양")

print(a)

#sort를 쓰면? 정렬을 해줘용

b = ["가","다","나"]
c = [1,5,3]
b.sort()
c.sort()
print(b)
print(c)


#뒤집기 함수

b.reverse()
print(b)

#index 있는지 없는지 검사

print(c.index(5))

#삽입 insert
c.insert(2,7) #2번째 인덱스에 4를 넣어라.
print(c)


#remove 값 제거
c.remove(7)

#맨 마지막 리스트값 제거 pop
print(c.pop()) #사라진 리스트값출력
print(c) #리스트 전체 출력

#리스트 확장 extend
c.extend([7,5])
print(c)