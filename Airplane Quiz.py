print("-----------------------------")
print("항공 관련 퀴즈 프로그램")
print("-----------------------------")

round = 1;

#첫번째 퀴즈
print("\nRound : %d\n" %(round))

while True:
    print("비행기가 떠오르는 원리는 무엇일까요? [난이도 : ★]")
    print("1. 부력\t2. 양력\t3. 힘력\t4. 자력")
    answer = input("정답 : ")

    if answer == "2" or answer == "양력":
        print("정답입니다")
        print("\n항공기는 날개에서 발생하는 양력으로 떠오르게 됩니다")
        round += 1
        break
    else:
        print("오답입니다. 다시 시도해주세요\n")

#두번째 퀴즈
print("\nRound : %d\n" %(round))

while True:
    print("항공기가 이착륙을 하는 장소의 이름은? [난이도 : ★★]")
    print("1. 유도로(Taxi Way)\t2. 이륙점(Clearing Spot)\t3. 접근점(Approach Way)\t4. 활주로(Runway)")
    answer = input("정답 : ")

    if answer == "4" or answer == "활주로" or answer == "Runway":
        print("정답입니다")
        print("\n비행기가 이륙하고 착륙하는 곳을 활주로, 다른 말로 런웨이라고도 부른답니다")
        round += 1
        break
    else:
        print("오답입니다. 다시 시도해주세요\n")

#세번째 퀴즈
print("\nRound : %d\n" %(round))

while True:
    print("세계에서 가장 큰 엔진의 지름은? [난이도 : ★★★★★]")
    print("1. 2.3m\t2. 3.7m\t3. 4.4m\t4. 5.1m")
    answer = input("정답 : ")

    if answer == "3" or answer == "4.4m":
        print("정답입니다")
        print("\n세계에서 가장 큰 엔진은 GE사에서 만든 GE9X라는 엔진으로 보잉 777X에 탑재되었으며 엔진의 지름이 중형 비행기 동체 크기와 맞먹는 크기입니다")
        round += 1
        break
    else:
        print("오답입니다. 다시 시도해주세요\n")

#네번째 퀴즈
print("\nRound : %d\n" %(round))

while True:
    print("항공기의 속도 측정 단위는? [난이도 : ★★★]")
    print("1. Knot\t2. km/h\t3. Mach\t4. Mile")
    answer = input("정답 : ")

    if answer == "1" or answer == "Knot" or answer == "노트":
        print("정답입니다")
        print("항공기의 속도 측정 단위는 미국에서 만든 노트(Knot)라는 단위를 사용합니다")
        round += 1
        break
    else:
        print("오답입니다. 다시 시도해주세요\n")

#다섯번째 퀴즈
print("\nRound : %d\n" %(round))

while True:
    print("항공기의 높이를 제어하는 부분의 이름은 [난이도 : ★★★★]")
    print("1. 방향타\t2. 앵글 에디터\t3. 고도 변환기\t4. 엘리베이터")
    answer = input("정답 : ")

    if answer == "4" or answer == "엘리베이터":
        print("정답입니다")
        print("\n항공기의 높이를 제어하는 엘리베이터는 항공기의 꼬리 부분에 위로 사다리꼴 처럼 생긴 부분에 있습니다")
        round += 1
        break
    else:
        print("오답입니다. 다시 시도해주세요\n")

#여섯번째 퀴즈
print("\nRound : %d\n" %(round))

while True:
    print("상업용 항공기 자격증을 취득하기 위한 최소 비행시간은? [난이도 : ★★★★]")
    print("1. 800시간\t2. 1200시간\t3. 1500시간\t4. 1700시간")
    answer = input("정답 : ")

    if answer == "3" or answer == "1500" or answer == "1500시간":
        print("정답입니다")
        print("대한민국에서 상업용 항공기 자격증을 취득하기 위한 최소 비행시간은 1500시간입니다")
        round += 1
        break
    else:
        print("오답입니다. 다시 시도해주세요\n")

#일곱번째 퀴즈
print("\nRound : %d\n" %(round))

while True:
    print("항공기에서 사용하는 블랙박스의 색깔은? [난이도 : ★★★★★]")
    print("1. 주황\t2. 노랑\t3. 검정\t4. 하양\t5. 빨강")
    answer = input("정답 : ")

    if answer == "1" or answer == "주황색" or answer == "주황":
        print("정답입니다")
        print("항공기에서 사용하는 블랙박스는 사고 발생 시 가장 눈에 띄게 보이는 주황(Orange)색을 사용합니다")
        round += 1
        break
    else:
        print("오답입니다. 다시 시도해주세요\n")

print("\n퀴즈가 모두 끝났습니다")
