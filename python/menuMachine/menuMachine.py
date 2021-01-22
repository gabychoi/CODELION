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