def sj_calculate_all(sj_num1: int, sj_num2: int) -> tuple:
    """
    두 숫자에 대해 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하고 결과를 튜플로 반환합니다.
    두 번째 숫자가 0인 경우 나눗셈 결과는 'division_error'를 반환합니다.
    """
    sj_add = sj_num1 + sj_num2
    sj_subtract = sj_num1 - sj_num2
    sj_multiply = sj_num1 * sj_num2
    
    # 0으로 나누는 경우 예외 처리
    if sj_num2 == 0:
        sj_divide = 'division_error'
    else:
        # 일반 나눗셈 (결과는 float)
        sj_divide = sj_num1 / sj_num2
        
    return (sj_add, sj_subtract, sj_multiply, sj_divide)

# --- 테스트 환경 --- 
sj_test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
sj_test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

print("--- 사칙연산 함수 테스트 결과 ---")
# 실행 로직
for sj_idx in range(len(sj_test_a)):
    sj_a = sj_test_a[sj_idx]
    sj_b = sj_test_b[sj_idx]
    
    # 함수 호출
    sj_result = sj_calculate_all(sj_a, sj_b)
    
    # 결과 출력
    print(f"Input: {sj_a}, {sj_b} | Output: {sj_result}")