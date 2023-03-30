print("="*25)
print("화성까지 걸리는 시간 계산")
print("="*25)

distance = 54600000
speed = 299792
time = distance / speed

ten = time // 60
one = time % 600

print("%d분 %d초" %(ten, one))
