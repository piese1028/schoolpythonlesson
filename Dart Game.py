sum = 0
set = 0

while sum < 20:
    score = int(input("점수 입력"))

    if score < 0 or score > 10:
        print("잘못된 점수 입력")
        continue

    sum += score
    print("합계점수 : ", sum)
    set += 1

    if sum == 5:
        break

print("프로그램 종료")
