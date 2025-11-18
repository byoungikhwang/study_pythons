# 문제 1

second = "Python is fun"

# "Python"이 second 문자열에 포함되어 있는지 확인
is_included = "Python" in second

# 결과 출력 (포함 여부와 합쳐진 문자열)
# 문제의 요구사항은 합쳐서 출력하는 것이므로, 포함 여부 확인 후 f-string 사용
combined_string = f"Welcome! {second}"
print(combined_string)

# 보너스: 포함 여부도 출력하고 싶다면:
# print(f"Includes 'Python': {is_included}")


# 문제 2
first = 5

while first >= 1:
    if first == 2:
        print("special")
    
    # 현재 first 값 출력 (선택 사항)
    # print(first)
    
    # 변수 값을 감소시키는 것이 중요
    first -= 1

    # 문제 3
    kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

total_scores = []
avg_scores = []

# zip()을 사용하여 kor와 eng의 요소를 쌍으로 묶어 순회
for k, e in zip(kor, eng):
    total = k + e
    average = total / 2  # 두 과목이므로 2로 나눔
    
    # 총점과 평균을 각 리스트에 추가
    total_scores.append(total)
    # 평균은 실수형(float)으로 저장 (문제 출력이 80.0, 55.0이므로)
    avg_scores.append(average) 

print(f"total_scores = {total_scores}")
print(f"avg_scores = {avg_scores}")

# 문제 4
kor = [70, 80, 90, 40, 50]

total_sum = 0

# for문을 사용하여 리스트 순회
for score in kor:
    # 점수가 60점 이상인지 조건 확인
    if score >= 60:
        # 조건에 맞는 점수만 누적 합계에 추가
        total_sum += score

print(f"누적합 = {total_sum}")