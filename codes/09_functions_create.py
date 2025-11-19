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
print(f"[32, 212, 68] 화씨를 섭씨로: {to_celsius_list([32, 212, 68])}") 
print(f"[77, 95] 화씨를 섭씨로: {to_celsius_list([77, 95])}") 
print(f"[14, 50] 화씨를 섭씨로: {to_celsius_list([14, 50])}") 

# 문제 6    조건 반복문
def check_weather(temp_f):
    """
    화씨 온도를 섭씨로 변환하고, 그 값에 따라 날씨 상태를 문자열로 반환합니다.
    """
    # 섭씨 변환 공식: (F - 32) * 5 / 9
    celsius = (temp_f - 32) * 5 / 9
    
    if celsius <= 5:
        condition = "춥다"
    elif 5 < celsius <= 15:
        condition = "쌀쌀하다"
    elif 15 < celsius <= 25:
        condition = "좋다"
    else:  # celsius > 25
        condition = "덥다"
        
    return f"섭씨 {celsius:.1f}°C, 날씨: {condition}"

# --- 함수 실행 및 변수 사용 ---

## 1️⃣ 첫 번째 호출
temp_f1_a = 77  # 25.0°C (좋다)
temp_f1_b = 32  # 0.0°C (춥다)
temp_f1_c = 59  # 15.0°C (쌀쌀하다)

print("--- 호출 1 ---")
print(f"화씨 {temp_f1_a}°F 결과: {check_weather(temp_f1_a)}")
print(f"화씨 {temp_f1_b}°F 결과: {check_weather(temp_f1_b)}")
print(f"화씨 {temp_f1_c}°F 결과: {check_weather(temp_f1_c)}")

## 2️⃣ 두 번째 호출
temp_f2_a = 95  # 35.0°C (덥다)
temp_f2_b = 60.8 # 16.0°C (좋다)
temp_f2_c = 41  # 5.0°C (춥다)

print("\n--- 호출 2 ---")
print(f"화씨 {temp_f2_a}°F 결과: {check_weather(temp_f2_a)}")
print(f"화씨 {temp_f2_b}°F 결과: {check_weather(temp_f2_b)}")
print(f"화씨 {temp_f2_c}°F 결과: {check_weather(temp_f2_c)}")

## 3️⃣ 세 번째 호출
temp_f3_a = 104 # 40.0°C (덥다)
temp_f3_b = 68  # 20.0°C (좋다)
temp_f3_c = 50  # 10.0°C (쌀쌀하다)

print("\n--- 호출 3 ---")
print(f"화씨 {temp_f3_a}°F 결과: {check_weather(temp_f3_a)}")
print(f"화씨 {temp_f3_b}°F 결과: {check_weather(temp_f3_b)}")
print(f"화씨 {temp_f3_c}°F 결과: {check_weather(temp_f3_c)}")