# # 함수 실습 위한  기본 코드
# # 화씨 온도를 섭씨 온도로 변환하는 코드

# # temp1 = 77
# # celsius1 = (temp1 - 32) * 5 / 9
# # print(celsius1)
# # temp2 = 95
# # celsius2 = (temp2 - 32) * 5 / 9
# # print(celsius2)
# # temp3 = 50
# # celsius3 = (temp3 - 32) * 5 / 9
# # print(celsius3)

# # 변수 재사용
# # temp = 77
# # celsius = (temp - 32) * 5 / 9
# # print(celsius)
# # temp = 95
# # celsius = (temp - 32) * 5 / 9
# # print(celsius)
# # temp = 50
# # celsius = (temp - 32) * 5 / 9
# # print(celsius)

# # 함수 사용
# # 2원칙 : parameter(매개변수)와, return(반환값)
# #def function_name(paramet_first, paramet_second,):
# #    execute codes(변수 + 약속어)
# #    reeturn result(변수)

# def function_name(param_first,):
#     execute codes (temp - 32) * 5 / 9
#     return result(celsius)



# temp = 77
# celsius = (temp - 32) * 5 / 9
# print(celsius)
# temp = 95
# celsius = (temp - 32) * 5 / 9
# print(celsius)
# temp = 50
# celsius = (temp - 32) * 5 / 9
# print(celsius)

# 파라메타 갯수만큼 주어야 한다.
# 함수 호출 전에 정의 해야 한다.

def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius

pass
to_celsius(120)                 # 함수 호출
temp1 = to_celsius(77)          # 변수 저장
print(temp1)                    # 

temp2 = (100)                     # 함수 호출
result2 = to_celsius(temp2)     # 변수 저장
print(result2)                  # 
pass


# print(to_celsius(77))
# print(to_celsius(95))
# print(to_celsius(50))   

