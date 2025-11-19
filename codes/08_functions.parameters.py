# def to_celsius(temp):
#     celsius = (temp - 32) * 5 / 9
#     return celsius      

# pass

# print(to_celsius(50))

# 함수 사용
# def function_namd

kor = 60
eng = 70
math = 80
# sum = kor + eng 

# 파라메터의 갯 수가 중요

# def get_sum(korea, english, mathematics=0): # mathematics에 기본값 0 설정, 변수에 파라메타를 넣치 않아도 된다.
    
#     summation = korea + english  + mathematics# 변수명을 바꿔도 내부에서만 사용되므로 이상없고, 파라메터 순서에 의해서 변수에 저장된다

#     return summation

# sum = get_sum(kor, eng, math)
# print(f"총점: {sum}")
# sum = get_sum(kor, eng)
# print(f"총점: {sum}")

# kor_scores = [60, 70, 80, 60, 50]
# eng_scores = [85, 75, 65, 55, 45]
# math_scores = [88, 78, 48, 58, 48]

# length = len(kor_scores)        # len()함수는 내장함수로 리스트의 길이를 반환
# len_list = range(length)

# range(len(kor_scores))

# pass

# for i in len_list:
#     kor = kor_scores[i]
#     eng = eng_scores[i]
#     math = math_scores[i]

# def get_for_sum(korea_scores, english_scores, mathematics_scores):

#     for i in len_list:
#         kor = korea_scores[i]
#         eng = english_scores[i]
#         math = mathematics_scores[i]
#         sum = get_sum(kor, eng, math)
#         print(f"{i+1}번 학생 총점: {sum}")
#     return 0
# get_for_sum(kor_scores, eng_scores, math_scores)   
# sum = kor + eng

def get_sum(korean, english, mathatics=0):
    # 실행할 코드
    summation = korean + english + mathatics
    return summation
# for문 함수 작성
kor_scores = [90, 80, 70, 60, 50]
eng_scores = [85, 75, 65, 55, 45]
math_scores = [88, 78, 68, 58, 48]
length = len(kor_scores)
len_list = range(length)
def get_for_sum(korean_scores, english_scores, mathematics_scores):
    # 실행할 코드
    for i in range(len(korean_scores)):
        kor = korean_scores[i]
        eng = english_scores[i]
        math = mathematics_scores[i]
        sum = get_sum(kor, eng, math)
        print(f"{i+1}번 학생 총점: {sum}")
    return 0
get_for_sum(kor_scores, eng_scores, math_scores)


