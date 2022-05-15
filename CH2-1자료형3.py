a="hobby"
print(a.count('b'))
print(a.find('x'))

b=","
c=b.join('abcd') #문자열 각각에삽입

print(c)

#대문자를 소문자로 바꾸기 lower
d= "HI"
print(d.lower())

#양쪽공백지우기 strip
e= " HI "
e.strip()
print(e.strip())


#외울필요가 없음 그냥 있었구나 하고 생각해야됨!

f = "Life is too short"
f.replace("Life","Mind")
print(f)

#문자열 기준자르는 함수
print(f.split(" "))