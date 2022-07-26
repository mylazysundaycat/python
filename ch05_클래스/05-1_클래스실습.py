class FourCal:
    def __init__(self, first, second): # 생성자 init
        self.first = first
        self.second = second

    def setdata(self,first,second):#클래스 안의 함수를 메서드라고 부른다
        self.first = first #여기서 self는 받은 객체 그자체이다
        self.second = second
    
    def add(self):return self.first + self.second

    def sub(self):return self.first-self.second    

    def mul(self):return self.first*self.second

    def div(self):return self.first/self.second
    
#값 입력
print(type(FourCal))
a=FourCal(7,4)
a.setdata(7,4)
print(a.first)

#더하기 기능
print(a.add())

#그 외 기능 구현
print(a.sub())
print(a.mul())
print(a.div())


# 클래스 상속
class MoreFourCal(FourCal):
    def pow(self): #기존 클래스는 냅두고 기능 확장시에 사용
        return self.first**self.second

# 클래스 오버라이딩
class SafeFourCal(FourCal):
    def div(self): # 부모클래스에 있는 메서드를 동일한 이름으로 다시 만듬
        if self.second == 0:
            return 0
        else:
            return self.first/self.second


# 클래스 변수
class Family:
    lastname = "권"
print(Family.lastname)
Family.lastname = "김" # 클래스 변수값은 클래스로 만든
#모든 객체에 공유된다는 특징이 있다.
print(Family.lastname)

