kor = [70, 80 ,90, 40, 50]							# 리스트 선언
eng = [90, 80 ,70, 70, 60]
sum1, sum2, sum3, sum4 = 0, 0, 0, 0				    # 누적 변수 초기화

# for 단일변수. in 리스트   
#   반복
#   실행문1
#   실행문2
#   ...:
for index in range(5):					# 0~4 반복
    kor[index]+ eng[index]
    sum3 = kor[index] + eng[index]+ sum3
print(f'국어 영어 누적값:, {sum3}')								# 국어 합계 출력)


# range(5))

#for score in kor:							# 0~4 반복
#    print(score, end=" ")								# 국어 점수 출력
#    sum1 += score + sum1
#print('\n 국어 합계:', sum1)
												# 줄바꿈 출력
#for score in kor:							# 0~4 반복
#    print(score, end=" ")								# 영어 점수 출력
#    sum2 = score + sum2
#print('\n 영어 합계:', sum2)
