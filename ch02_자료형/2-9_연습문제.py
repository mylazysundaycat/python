#Q1
a=80
b=75
c=55
sum=(a+b+c)/3
print(sum)

#Q2
a=13
cal=a%2

#Q3
a="881120-1068234"
b=a[:6]
c=a[7:]
print(b,c)

#Q4
pin = "881120-1068234"
sex = pin[7]
print(sex)

#Q5
a = "a:b:c:d"
a.replace(':','#')
print(a)

#Q6
num = [1,3,5,4,2]
num.reverse()
print(num)

#Q7
text = ['Life','is','too','short']
song = " ".join(text)
print(song)
print(text)
print(text[1])

#Q8
a=(1,2,3)
b=(4,)
c=a+b
print(c)

#Q9
#답은 3번으로 Key엔 불변하는 값만 들어갈 수있다.

#Q10
a={'a':90,'b':80,'c':70}
print(a['b'])
print(a.get('b'))


#Q11
a=[1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b=set(a)
print(b)


#Q12
#a와 b가 가리키는 객체의 주소가 같아서
#a[1]=4로 하면 b의 값도 변하게된다.
