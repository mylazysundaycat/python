a = "i eat %d apples." %3 # %d 는 밖에 %3과 꺼내서 쓸수 있다
print(a)

b= "i eat " + str(3) + " apples."
print(b)

number = 10
day = "three"
c = "i eat %d apples. so i was sick fo %s days." %(number, day)
print(c)

d = "하하하ㅏ {name} 하하하 {age}".format(name="무한도전",age=3)
print(d)