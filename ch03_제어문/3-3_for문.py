#for문
#for 변수 in 리스트(튜플, 문자열):
#   수행할 문장1
#   수행할 문장2

#1. 예제를 통해 for문 이해하기
from turtle import st


test_list=['1','2','3']
for i in test_list:
    print(i)

a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first,last)
    print(first+last)



#2. for문의 응용
#총 5명의 학생이 시험을 보았는데, 시험점수가 60점이
#넘어야 합격이다. 합불결과를 보여주시오
student=[15,33,59,70,97]

for i in student:
    if i>60:
        print("당신의 시험 점수는 %s입니다." %i)
        print("따라서 합격입니다!")
    else:
        print("불합격입니다.")

num=0
for i in student:
    num = num + 1
    print("%d번 학생은"%num)
    if i>60:
        print("합격입니다.")
        print("제1회 토익성적은 %s점입니다"%i)
    else:
        print("불합격입니다.")

#60점 이상인 사람에게는 축하메세지를 보내기!
student=[15,33,59,70,97,46,100,52]
num=0
for i in student:
    num=num+1
    if i<60:
        continue
    print("%s번학생 축하드립니다!.합격입니다"%num)



#3. range함수
a = range(10) #0부터 10미만의 숫자를 포함하는 range객체를 만듬
a = range(1,11) #시작숫자는 포함되나 끝숫자는 안포함됨

add=0
for i in range(11):
    add = add+i
print(add)

student=[15,33,59,70,97,46,100,52]
for i in range(len(student)):
    if student[i]<60:
        continue
    print("당신은 %s점으로 합격입니다!"%student[i])


#4. 구구단만들기
num=1
for i in range(2,10):
    for v in range(1,10):
        print(i*v, end=" ")
    print("")
#sep키워드로 구분자 결정(생략시 공백으로 구분하여 출력)
print("2022","07","25",sep="-")
#end키워드로 줄 끝에 넣을 문자 결정(생략시 \n을 기본으로 함)



#5. for를 이용하여 리스트에 내포시키기
a=[1,2,3,4]
b=[]

for i in a:
    b.append(i)
print(b)