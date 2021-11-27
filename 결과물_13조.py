#함수직접 만들기
import random

computer_number=[]
guess=[]
target=[]
number=[]

#게임난이도 정하기
while 1:
    level=input("난이도를 선택해주세요: e / m / h :  ")
    if level=="e":
        maxl=4
        break
    elif level=="m":
        maxl=6
        break
    elif level=="h":
        maxl=8
        break
        
#숫자 아무거나 고르기
while 1:
    for i in range(0,2):
        computer_number.append(random.randint(1,maxl))
    if computer_number[0]!=computer_number[1]:
        break


#함수만들기
def is_same(target,number):
    count1=0
    count2=0
    index1=0
    index2=0
    for i in range(0,2):
        if target[i]==number[0]:#입력한 첫 번째 숫자 맞았을 때
            print()
            print("입력한 1번째 숫자 정답.")
            count1=1
            index1=i 
        if target[i]==number[1]:#입력한 두 번째 숫자 맞았을 때
            print()
            print("입력한 2번째 숫자 정답.")
            count2=1
            index2=i
            
    if count1==1 and count2==0: #첫번째로 입력한 숫자만 맞았을 때 ->
        if index1==0:            #두 번째로 입력한 숫자 vs index1이 아닌 target비교
                index1=1
        else : index1=0
        if target[index1]<number[1]:
                print()
                print("입력하신 2 번째 숫자보다 작은 숫자를 생각하십시오.")
        else :
            print()
            print("입력하신 2 번째 숫자보다 큰 숫자를 생각하십시오.")
        result="Lose"

    elif count1==0 and count2==1: #두번째로 입력한 숫자만 맞았을 때 ->
        if index2==0:            #첫 번째로 입력한 숫자 vs index2이 아닌 target비교
                index2=1
        else : index2=0
        if target[index2]<number[1]:
                print()
                print("입력한 1번째 숫자보다 작은 숫자 입력.")
        else :
            print()
            print("입력한 1번째 숫자보다 큰 숫자 입력.")
        result="Lose"
   
    elif count1==0 and count2==0: #입력한 숫자 모두 틀렸을 때
        print()
        print("입력한 1,2번째 숫자 모두 틀렸습니다.")
        result="Lose"
    
    else:
        result="Win" #입력한 두 개의 숫자 모두 맞았을 때
    return result 

#게임 시작하기
print()
print("게임이 시작되었습니다. 각 참가자는 1부터 %d까지 숫자 중 2가지를 차례대로 입력하십시오.  "%maxl)
gg = int(input("당신의 학번을 기재해주십시오: "))

#사용자가 추측한 숫자를 인수로 받기
for k in range(0,2):
    if k==0:
        print()
        guess.append(int(input("첫 번째 숫자 입력: ")))
    if k == 1:
        print()
        guess.append(int(input("두 번째 숫자 입력: ")))
#print(guess)

#is_same 함수 사용하기
count=1
higher_or_lower = is_same(computer_number,guess)
while 1:
    if higher_or_lower=="Lose":
        guess.clear()
        for k in range(0,2):
            if k == 0:
                print()
                guess.append(int(input("첫 번째 숫자 입력: ")))
            elif k == 1:
                print()
                guess.append(int(input("두 번째 숫자 입력: ")))
        higher_or_lower = is_same(computer_number, guess)
        count+=1
    else:
        break

if count<=5:
    print()
    print("%d번 만에 성공했습니다. %d는(은) 생존하였습니다."%(count,gg))
else:
    print()
    print("%d번 만에 성공했습니다. %d는(은) 탈락입니다."%(count,gg)) 

#게임을 끝냅니다
#input("게임을 마치려면 엔터키를 누르세요")