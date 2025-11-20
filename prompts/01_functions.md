```
# 정리본
# def sj_calculate_all(sj_num1: int, sj_num2: int) -> tuple:
#     # TODO: 요구사항에 따라 덧셈, 뺄셈, 곱셈, 나눗셈 로직을 구현하시오.
#     pass
# 
# # --- 테스트 환경 --- 
# sj_test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
# sj_test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]
# 
# # 실행 로직
# print("--- 사칙연산 함수 테스트 시작 ---")
# for sj_idx in range(len(sj_test_a)):
#     sj_a = sj_test_a[sj_idx]
#     sj_b = sj_test_b[sj_idx]
#     sj_result = sj_calculate_all(sj_a, sj_b)
#     print(f"Input: {sj_a}, {sj_b} | Output: {sj_result}")
```


```
초안
{
  "project_name": "Function_Implementation_Workshop",
  "prompt_id": "SJ-CALC-001",
  "title": "다중 연산 처리기 (Multi-Operation Calculator) 구현",
  "level": "Intermediate",
  "problem_statement": "두 개의 정수 리스트를 입력받아 
  **사칙연산** 결과를 튜플 형태로 반환하는 핵심 함수를 완성하시오. 
  모든 식별자는 **'sj_' 이니셜**을 사용해야 합니다.",
  "task": {
    "type": "Code_Refinement",
    "language": "python",
    "target_file": "prompts/01_functions.py",
    "function_name": "sj_calculate_all",
    "constraints": [
      "모든 변수 및 함수명은 소문자와 언더스코어 조합이며 'sj_'로 시작해야 합니다 
      (예: `sj_add_result`).",
      "두 번째 입력 값(`sj_num2`)이 **0**일 경우, 나눗셈 결과는 소수점 형태 대신 
      **'division_error'** 문자열을 반환해야 합니다.",
      "테스트 데이터(`sj_test_a`, `sj_test_b`)는 10개의 요소를 가진 리스트로 제공됩니다."
    ],
    "return_specification": {
      "data_type": "tuple",
      "format": "(덧셈 결과, 뺄셈 결과, 곱셈 결과, 나눗셈 결과)",
      "example": "(15, 5, 50, 2.0) 또는 (7, 7, 0, 'division_error')"
    },
    "skeleton_code": "def sj_calculate_all(sj_num1: int, sj_num2: int) -> tuple:\n    
    # TODO: 요구사항에 따라 덧셈, 뺄셈, 곱셈, 나눗셈 로직을 구현하시오.\n    
    pass\n\n# --- 테스트 환경 --- \nsj_test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]\nsj_test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]\n\n# 실행 로직\nfor sj_idx in range(len(sj_test_a)):\n    sj_a = sj_test_a[sj_idx]\n    sj_b = sj_test_b[sj_idx]\n    sj_result = sj_calculate_all(sj_a, sj_b)\n    print(f\"Input: {sj_a}, {sj_b} | Output: {sj_result}\")"
  },
  "expected_behavior": {
    "case_1": "정상 나눗셈 (10, 5) -> (15, 5, 50, 2.0)",
    "case_2": "0으로 나누는 경우 (7, 0) -> (7, 7, 0, 'division_error')"
  },
  "solution_guide": {
    "recommended_approach": "조건문(if-else)을 사용하여 나눗셈 연산 전 0으로 나누는 예외를 처리하는 것이 효율적입니다.",
    "code_snippet": "def sj_calculate_all(sj_num1: int, sj_num2: int) -> tuple:\n    sj_add = sj_num1 + sj_num2\n    sj_subtract = sj_num1 - sj_num2\n    sj_multiply = sj_num1 * sj_num2\n    \n    if sj_num2 == 0:\n        sj_divide = 'division_error'\n    else:\n        sj_divide = sj_num1 / sj_num2\n        \n    return (sj_add, sj_subtract, sj_multiply, sj_divide)"
  }
}
```
