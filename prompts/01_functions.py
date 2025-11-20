# 함수: sjh_calculate_all
# 설명: 두 숫자(sj_num1, sj_num2)에 대한 사칙연산 결과를 튜플로 반환합니다.
#       나눗셈 시 sj_num2가 0인 경우 'division_error'를 반환합니다.

def sjh_calculate_all(sj_num1, sj_num2):
    
    # 덧셈 (sj_* 변수 사용)
    sj_sum = sj_num1 + sj_num2
    
    # 뺄셈
    sj_diff = sj_num1 - sj_num2
    
    # 곱셈
    sj_prod = sj_num1 * sj_num2
    
    # 나눗셈 (0 예외 처리)
    if sj_num2 == 0:
        sj_div = "division_error"
    else:
        # 일반 나눗셈 (float 결과)
        sj_div = sj_num1 / sj_num2
        
    # (덧셈, 뺄셈, 곱셈, 나눗셈) 순서로 튜플 반환
    return (sj_sum, sj_diff, sj_prod, sj_div)


# 테스트 리스트 (변수명 sj_* 규칙 적용)
sj_test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
sj_test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

# 테스트 실행
print("--- 사칙연산 함수 테스트 결과 ---")
for sj_i in range(len(sj_test_a)):
    sj_a = sj_test_a[sj_i]
    sj_b = sj_test_b[sj_i]
    
    # 함수 sjh_calculate_all 호출
    sj_result = sjh_calculate_all(sj_a, sj_b) 
    
    print(f"입력: {sj_a}, {sj_b} => 결과: {sj_result}")
