from __future__ import print_function

if __name__ == "__main__":
    n = int(input())
    for i in range(1,n+1): # range ()의 최대 값은 마지막 단계에서 i 가 n과 같도록 n + 1 이다.
        print(i,end="") # end옵션을 사용하면 그 뒤의 출력값과 이어서 출력한다.(즉, 줄바꿈을 하지 않게 된다.)
