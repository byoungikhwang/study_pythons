# 문제 1         섭씨 온도 3개를 받아 평균 값.

def avg_celsius(t1, t2, t3): 
    return (t1 + t2 + t3) / 3

            # 함수 3회 
print(f"10°C, 20°C, 30°C의 평균: [avg_celsius(10, 20, 30)]°C")
print(f"5°C, 15°C, 25°C의 평균: [avg_celsius(5, 15, 25)]°C")
print(f"-5°C, 0°C, 5°C의 평균: [avg_celsius(-5, 0, 5)]°C")

pass

# 문제 2     이름과 선호 언어 2개를 지정된 형식으로 출력.
            
def print_languages(name, lang1, lang2):
   
    print(f"{name}님의 좋아하는 과목은 {lang1}, {lang2} 입니다.")

            # 함수 실행 (최소 3회 호출)
print_languages("홍길동", "국어", "수학")
print_languages("김철수", "영어", "체육")
print_languages("이영희", "과학", "음악")

pass

# 문제 3    점수 리스트에서 60점 이상인 점수들의 합계.
            
def sum_passing_scores(scores):
    
    passing_sum = 0
    for score in scores:
        if score >= 60:
            passing_sum += score
    return passing_sum

            # 함수 실행 (최소 3회 호출)
print(f"[70, 50, 80, 90] 중 합격 점수 합계: {sum_passing_scores([70, 50, 80, 90])}점")
print(f"[50, 40, 55] 중 합격 점수 합계: {sum_passing_scores([50, 40, 55])}점")
print(f"[60, 100, 60, 40] 중 합격 점수 합계: {sum_passing_scores([60, 100, 60, 40])}점")

pass

# 문제 4     문자열 두 개를 하나의 문자열로.
  
def combine(str1, str2):
    
    return str1 + str2

            # 함수 실행 (최소 3회 호출)
print(f"결합 결과 1: {combine('안녕', ' 하세요?')}")
print(f"결합 결과 2: {combine('파이썬', ' 재미 없다.')}")
print(f"결합 결과 3: {combine('시작', '과 종료')}")

pass

# 문제 5    화씨 온도 리스트를 받아 섭씨로 변환된 출력.
            
def to_celsius_list(temps_f):
    
    celsius_list = []
    for temp_f in temps_f:      
        celsius = (temp_f - 32) * 5 / 9     # 섭씨 변환 (F - 32) * 5 / 9
        celsius_list.append(celsius)
    return celsius_list

                                            # 함수 3회 
print(f"[32, 212, 68] 화씨를 섭씨로: {to_celsius_list([32, 212, 68])}") # [0.0, 100.0, 20.0]
print(f"[77, 95] 화씨를 섭씨로: {to_celsius_list([77, 95])}") # [25.0, 35.0]
print(f"[14, 50] 화씨를 섭씨로: {to_celsius_list([14, 50])}") # [-10.0, 10.0]

