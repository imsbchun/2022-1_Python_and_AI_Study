from __future__ import division 
# 구버전의 언어를 써야하지만 최신버전의 기능을 써야되는 상황에서
#모듈을 import하듯이 __future__를 통해 상위 버전의 기능을 쓸수 있도록함.
#이를 통해 구버전에서도 미래버전의 기능을 사용가능

if __name__ == "__main__":
#메인 함수의 선언, 시작을 의미
#__name__이라는 변수에 __main__이라는 값이 할당됨
#모듈에 위와 같은 조건문을 넣어주고 그 아래는 직접 실행 했을때만 실행되길 원하는 코드들을 넣어주는 것
#실제 import 될때는 출력X -> 모듈에 포함된 기능만을 포함할 수 있다.
    a = int(input()) # int()는 숫자나 문자열을 정수형(integer)로 변환 가능
    b = int(input())

    int_result = int(a/b) # integer division의 결과 a//b로 쓸 수 있다.
    float_result = a/b # float division의 결과 float는 숫자나 문자열을 실수형(float)으로 변환 가능
    print(int_result)
    print(float_result)
