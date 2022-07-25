# 1. 파일 생성하기
# 파일 객체 = open(파일이름, 파일열기모드)
# r 읽기모드 : 파일을 읽기만 할 때 사용
# w 쓰기모드 : 파일에 내용을 쓸 때 사용
# a 추가모드 : 파일의 마지막에 새로운 내용을 추가시킬때 사용

f = open("C:/code/새파일.txt", 'w')
f.close()




#------------------------------------------------------#




# 2. 파일을 쓰기 모드로 열어 출력값 적기
f = open("C:/code/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()




#------------------------------------------------------




# 3. 저장된 파일을 읽는 여러가지 방법
# 1) readline 함수 이용
f = open("C:/code/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("C:/code/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

#while True:
#    data = input()
#    if not data: break
#    print(data)


# 2) readlines 함수 사용하기
f = open("C:/code/새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
# 파일의 모든 줄을 읽어준다

f = open("C:/code/새파일.txt",'r')
lines = f.readlines()
for line in lines:
    line = line.strip() # 줄바꿈 \n문자를 제거함
    print(line)
f.close()


# 3) read 함수 사용하기
f = open("C:/code/새파일.txt",'r')
data=f.read()
print(data)
f.close()




#------------------------------------------------------#




# 4. 파일에 새로운 내용 추가하기
# for 문으로 추가
f = open("C:/code/새파일.txt",'a')
for i in range(11,21):
    data = "%d번째 줄입니다.\n"%i
    f.write(data)
f.close()

f = open("C:/code/새파일.txt", 'r')
while True:
    data = f.readline()
    if not data: break
    print(data)
f.close()




#------------------------------------------------------#




# 5. with문과 함께 사용하기
# 파일을 열면 항상 close해주는 것이 좋다. 하지만 이렇게
# 파일을 열고닫고 하는것을 자동으로 할수있다면 편리할것이다

with open("C:/code/새파일2.txt",'w') as f:
    f.write("Life is too short")

with open("C:/code/새파일2.txt",'r') as f:
    data=f.read()
    print(data)