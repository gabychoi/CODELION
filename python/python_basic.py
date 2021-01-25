import random

#for문
for x in range(30):
    print(random.choice(["된장찌개","제육볶음","치킨","떡볶이","라면"]))

#변수 지정
lunch = random.choice(["된장찌개","피자","제육볶음"])
#변수 재지정 : 따로 지우지 않아도 새롭게 지정된다.
lunch = "냉장고"
dinner = random.choice(["김밥","쫄면","돈까스"])

#변수 출력
print(lunch)
print(dinner)

#Dictionary
information = {'고향' : '수원', '취미' : '코딩', '좋아하는 음식' : '짬뽕'}
print(information)
print(information.get('취미'))

information = {'특기' : '가무', '사는 곳' : '서울'}
print(information.get('특기'))
print(information.get('사는 곳'))

#List와 Dictionary
information = {'고향' : '수원', '취미' : '코딩', '좋아하는 음식' : '짬뽕'}
foods = ["된장찌개","피자","제육볶음"]

print(information.get('취미'))
information['특기'] = '가무'
information['사는 곳'] = '서울'
#값 삭제
del information['좋아하는 음식']
print(information)
#묶음 개수 세기
print(len(information))
#딕셔너리 전부 비우기
information.clear()
print(information)

#리스트 인덱싱
print(foods[0])
print(foods[-1])

#값 추가
foods.append('김밥')
print(foods)
del foods[-1]
print(foods)

#for문 응용
for x in range(30):
    print(x)

foods = ["된장찌개", "피자", "제육볶음"]
print(foods)

for x in range(3):
    print(foods[x])

#리스트 안의 모든 요소를 출력
for x in foods:
    print(x)

#for문 활용 딕셔너리 출력
information = {'고향' : '수원', '취미' : '코딩', '좋아하는 음식' : '짬뽕'}

for x, y in information.items():
    print(x)
    print(y)

#집합 : 순서X, 중복X
foods = ['된장찌개', '피자', '제육볶음', '된장찌개']
foods_set1 = set(foods)
foods_set2 = set(['된장찌개', '피자', '제육볶음', '된장찌개'])
print(foods_set1)
print(foods_set2)

foods_set = set(foods)
print(foods)
#집합은 알아서 중복이 제거돼 출력됨
print(foods_set) 

menu1 = set(['된장찌개', '피자', '제육볶음'])
menu2 = set(['된장찌개', '떡국', '김밥'])
#합집합
menu3 = menu1 | menu2 
print(menu3)
#교집합
menu4 = menu1 & menu2
print(menu4)
#차집합
menu5 = menu1 - menu2
print(menu5)

#if문
import random
food = random.choice(['된장찌개', '피자', '제육볶음'])

if(food == '제육볶음'):
    print("곱빼기 주세요!")
print("종료")

#if~else문
if(food == '제육볶음'):
    print("곱빼기 주세요!")
else:
    print("그냥 주세요.")
print('종료')

#if ~elif ~else문
season = input("계절을 입력하세요 :")

if season == "봄" :
	print("가디건")
elif season == "여름" :
	print("반팔")
elif season == "가을" :
	print("코트")
elif season == "겨울" :
	print("패딩")
else :
    print("잘못 입력하셨습니다.")

#함수
def make_dolcelatte():
    print("1. 얼음을 넣는다.")
    print("2. 연유를 30ml 넣는다.")
    print("3. 찬 우유를 넣는다.")
    print("4. 에스프레소 샷을 넣는다.")

def make_blueberry_smoothie():
    print("1. 블루베리 20g을 넣는다.")
    print("2. 우유 300ml를 넣는다.")
    print("3. 얼음을 넣는다.")
    print("4. 믹서기에 간다.")

def make_simple_latte():
    print("1. 커피를 넣는다.")
    print("2. 우유를 넣는다.")
    print("3. 신나게 섞는다.")

make_dolcelatte()
print("*" * 30)
make_blueberry_smoothie()
print("*" * 30)
make_simple_latte()