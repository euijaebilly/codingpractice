"""
Fizz Buzz
정수 n이 주어지면 무자열 배열 응답(1 - 인덱스)을 반환합니다.

i가 3과 5로 나누어 떨이진다면 answer[i] == "FizzBuzz"
i가 3으로 나누어 떨어진다면 answer[i] == "Fizz"
i 가 5으로 나누어 떨어진다면 answer[i] == "Buzz"
위의 조건 중 어느 것도 참이 아닌 경우 answer[i] == i (문자열)
"""

def fizzBuzz(n):
    r = []
    for m in range(n):
        if (m+1) % 15 == 0:
            r.append("fizzbuzz")
            continue
        if (m+1) % 3 == 0:
            r.append("fizz")
            continue
        if (m+1) % 5 == 0:
            r.append("buzz")
            continue
        else:
            r.append(str(m+1))
            continue
    return r


if __name__ == '__main__':
    print(fizzBuzz(17))