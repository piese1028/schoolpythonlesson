print("="*20)
print("Grade Calculator Program")
print("="*20)

name = input("이름 입력 : ")

korean = int(input("국어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
computer = int(input("정보 점수 입력 : "))


sum = korean + math + computer
average = sum / 3


print("%s의 성적\n총점 : %d, 평균 : %.2f)" %(name, sum, average))
