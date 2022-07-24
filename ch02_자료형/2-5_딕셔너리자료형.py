#1. 딕셔너리란?
#Key와 Value를 한 쌍으로 갖는 자료형이다
#대응관계를 가진 이 자료형을 Hash라고 부름.
#딕셔너리는 Key를 통해서 Value를 얻는것이 가장 큰 특징이다.


dic={'name':'Jin','phone':'01012345678','birth':'1204'}
ex1={'a':[1,2,3]} #value에 리스트도 넣을수 있음


#2. 딕셔너리 쌍 추가, 삭제
a={1:'a'}
a[2]='b'#추가
print(a)
a['3']='c'
print(a)

del a[1]#삭제
print(a)


#3. 딕셔너리에서 Key값으로 Value얻기
job={'김연아':'피겨스케이팅','강호동':'예능인'}
print(job['김연아'])

#key에 리스트를 넣을 수 없다.
#그러나 튜플은 가능하다.

#4. Key리스트 만들기
print(job.keys())
print(list(job.keys()))


#5. value리스트 만들기
print(job.values())


#6. key,value 쌍 얻기
print(job.items())


#7. key:value 쌍 모두 지우기
print(a.clear())


#8. key로 value 얻기(get 함수)
print(job.get('이하이'))


#9. 해당 key가 딕셔너리 안에 있는지 조사하기
print('이하이' in job)
print('강호동' in job)