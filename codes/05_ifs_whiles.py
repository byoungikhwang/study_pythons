first = 5   # 오타

# while first > 0:
#    print(f"while 값 : {first}")
#    first = first - 1


# while first > 0:
#    print(f"while 값 : {first}")  # 들여쓰기 문제
#    first = first - 1


while first > 0:
    print(f"while 값 : {first}")
    if first == 3:     # 실제로는 first == 3 에서 break해야 하는 문제 조건
        print("break 실행")
        break
    first = first - 1
