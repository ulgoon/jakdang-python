for i in range(1,100+1):
    # 조건문의 시작
    # % ==> 나머지 연산
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
