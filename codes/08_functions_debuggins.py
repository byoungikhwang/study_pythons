# 문제 1
def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius  # return 문 추가

result = to_celsius(77)
print(result)

# 문제 2
def convert(temp):
    # 변수 오타 : temps -> temp
    return (temp - 32) * 5 / 9  # 섭씨 공식은 -32 수정.

print(convert(95))

# 문제 3
def to_celsius(temp):
    return (temp - 32) * 5 / 9

# 함수 호출 시 값이 없음(77) 줘야 함.
value = to_celsius(77)
print(value)

# 문제 4
def to_celsius(temp):
    return (temp - 32) * 5 / 9  # 공식 오류: 섭씨 변환 (temp - 32) * 5 / 9

# 함수 호출시 문자열을 정수(int)로 변환
print(to_celsius(int("77")))

# 문제 5
def to_celsius(temp):
    return (temp - 32) * 5 / 9 # 공식 오류 (temp - 32) * 5 / 9

temps = [77, 95, 50]
results = []

for t in temps:     # 반복문
    result = to_celsius(t)  # 1. 변수명 오류 : t 사용
    results.append(result)   # 2. 결과 값 추가 를 리스트에 저장

print(results)      # 3. 루프 종료 결과 값 출력


# 문제 5
def to_celsius(temp):
    return (temp - 32) * 5 / 9 

def convert_temps(temps_list):      # 온도 리스트의 값들을 섭씨로 변환.
    results = []
    for t in temps_list:
        results.append(to_celsius(t))
    return results

temps = [77, 95, 50]
results = convert_temps(temps)
print(results)