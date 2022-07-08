def is_leap(year): # is_leap(year)이라는 함수 정의
    leap = False # leap가 거짓이라고 조건 설정후 문장 수행
    if(year % 4) == 0: # year을 4로 나눴을때 0이면 leap이 참
        leap = True
    if(year % 100) == 0: # year을 100으로 나눴을때 0이면 leap이 거짓
        leap = False
    if(year % 400) == 0: # year을 400으로 나눴을때 0이면 leap이 참
        leap = True
    return leap # return 함수를 이용하여 반환

year = int(input())
print(is_leap(year))
