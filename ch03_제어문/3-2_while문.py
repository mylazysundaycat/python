#1. while문의 기본구조
#반복해서 문장을 수행해야할 경우 사용한다
#while <조건문>:
#   수행해야할 문장1
#   수행해야할 문장2
#조건문이 참인 경우 아래 문장들이 반복해서 수행됨

treeHit=0
while treeHit<10:
        treeHit=treeHit+1
        print("나무를 %d번 찍었습니다."%treeHit)
        if treeHit == 10:
            print("나무 넘어갑니다.")


#2. while문 만들기
prompt = """
1.Add
2.Del
3.List
4.Quit

Enter number : 
"""
number=0
while number!=4 :
    print(prompt)
    number = int(input())
    if number==4 :
        print("시스템이 종료됩니다.")



#3. while문 강제탈출

coffee=10

while True:
    print("100원 커피샵에 오신것을 환영합니다.")
    money = int(input("돈을 넣어주세요 : "))
    if money == 100:
        coffee=coffee-1
        print("주문하신 커피 나왔습니다.")
        print("남은 커피는 %d잔 입니다."%coffee)
    elif money > 100:
        coffee=coffee-1
        print("주문하신 커피 나왔습니다.")
        print("거스름돈은 %d입니다."%(money-100))
        print("남은 커피는 %d잔 입니다."%coffee)
    else:
        print("잔액이 부족합니다.")
    if coffee == 0:
        print("커피가 다 떨어졌습니다.")
        break


#4. while문 처음으로 돌아가기(continue)
a=0
while a < 10 :
    a = a+1
    if a%2 == 0: continue
    print(a)
