# 문제 6
def to_celsius(temp):

    celsius = (temp - 32) * 5 / 9     # celsius로 오류
    return celsius

print(to_celsius(77)) 

# 문제 7
def to_celsius(temp):
    if temp > 0:
        celsius = (temp - 32) * 5 / 9
    else:               # temp가 0 이하일 경우 celsius가 정의되지 않았을 경우의 설정.
        celsius = (temp - 32) * 5 / 9
        
    return celsius       # return,celsius 위치가 동일 선상에 있어야 함.

print(to_celsius(50))

# 문제 8
def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9 # 공식 값 수정 temp - 3) -> (temp - 32)
    return celsius

temp = 77
result1 = to_celsius(temp)

temp = 95                
result2 = to_celsius(temp)  # 변수 누락 : to_celsius() -> to_celsius(temp)

temp = 50
result3 = to_celsius(temp)

print(result1, result2, result3)

# 문제 9
def to_celsius(temp):
    
    return (temp - 32) * 5 / 9      # 공식 누락  32로 수정)

temps = [77, 95, 50]
celsius_temps = [] # 변수 값 오류, 변환된 값을 저장할 새 리스트

# 반복문을 사용해 리스트의 각 요소를 하나씩 함수에 전달
for temp in temps:
    celsius_temps.append(to_celsius(temp))  # 반복문으로 변화된 값 추가

print(celsius_temps)        # 추가된 전체 리스트를 출력합니다.

# 문제 10
def to_celsius(temp):
    return (temp - 32) * 5 / 9

if to_celsius(77) > 20:   # 조건문 오류 : 20으로 수정 
    print("warm")           # warm의 값은 25.0C true
else:
    print("cold")
    
