set_lunch = set(["된장찌개", "피자", "제육볶음", "짜장면"])
item = "짜장면"
#차집합
print(set_lunch - set([item]))

#요소 삭제 후 변수 재정의
set_lunch = set_lunch - set([item])
print(set_lunch)

#응용
set_dinner = set(["된장찌개", "피자", "제육볶음", "짜장면"])
food = "짜장면"
set_dinner = set_dinner - set([food])
print(set_dinner)