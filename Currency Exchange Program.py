print("="*20)
print("지폐 교환 프로그램")
print("="*20)

money = int(input("금액: "))

오천원 = money // 5000
천원 = money % 5000 // 1000
오백원 = money % 1000 // 500
백원 = money % 500 // 100
십원 = money % 100 // 10

print("오천원 : %d장\n천원 : %d장\n오백원 : %d개\n백원 : %d개\n십원 : %d개" %(오천원, 천원, 오백원, 백원, 십원))
