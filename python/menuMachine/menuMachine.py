import random
import time

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
while True:
    item = input("음식을 추가해주세요 : ")
    if(item == 'q'):
        break
    else: 
        lunch.append(item)

print(lunch)

#집합으로 변경
set_lunch = set(lunch)

while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요 : ")
    if (item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item])

# 쉼표 넣으면 한줄로 쭉 이어짐
print(set_lunch, "중에서 선택합니다.")

#5초 쉼
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

#집합을 리스트 형태로 변환하고, 랜덤으로 하나를 뽑아내 출력
print(random.choice(list(set_lunch)))