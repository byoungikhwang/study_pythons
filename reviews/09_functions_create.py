# 문제 1 
# 섭씨 온도 3개를 받아 평균을 반환하는 함수 avg_celsius(t1, t2, t3) 를 작성하시오.
def avg_celsius(t1, t2, t3):
    average = (t1 + t2 + t3) / 3
    return average
print(avg_celsius(20, 30, 40))
print(avg_celsius(15, 25, 35))
print(avg_celsius(10, 20, 30))

# 문제 2
# 이름과 좋아하는 언어 2개를 받아 아래 형식으로 출력하는 함수를 작성하시오.
# 홍길동님의 선호 언어는 Python, Java 입니다.
def favorite_language(name, lang1, lang2):
    print(f"{name}님의 선호 언어는 {lang1}, {lang2} 입니다.")
favorite_language("홍길동", "Python", "Java")
favorite_language("김철수", "C++", "JavaScript")
favorite_language("이영희", "Java", "C#")

# 문제 3
# 점수 리스트를 받아 60점 이상 점수만 누적한 합계를 반환하는 함수를 작성하시오
def sum_above_60(scores):
    total = 0
    for score in scores:
        if score >= 60:
            total += score
    return total

print(sum_above_60([55, 65, 75, 45, 85]))
print(sum_above_60([60, 70, 80, 90, 50]))
print(sum_above_60([40, 50, 60, 70, 80]))

# 문제 4
#문자열 두 개를 받아 하나의 문장으로 이어 붙이는 함수 combine(str1, str2) 작성
def combine(str1, str2):
    combined = str1 + " " + str2
    return combined
print(combine("Hello", "World"))
print(combine("Python", "Programming"))
print(combine("Function", "Creation"))

# 문제 5
# 온도 리스트를 받아 모두 섭씨로 변환해 새로운 리스트로 반환하는 함수 작성.
def to_celsius(temp_list):
    celsius_list = []
    for temp in temp_list:
        celsius = (temp -32) * 5 / 9
        celsius_list = celsius_list + [celsius]  
    return celsius_list
print(to_celsius([32, 68, 100]))
print(to_celsius([50, 77, 86]))
print(to_celsius([0, 32, 212]))