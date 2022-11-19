'''
숫자가 높은지 낮은지 추측하기
우리는 추측 게임을 하고 있습니다. 게임은 다음과 같습니다.

제가 1에서 n까지의 숫자 중 하나를 선택합니다. 당신은 제가 선택한 숫자를 추측해야 합니다.

당신이 틀릴 때마다 내가 선택한 숫자가 당신의 추측보다 높은지 낮은지 알려줄 것입니다.

-1: 당신의 추측이 제가 선택한 숫자보다 높습니다(즉, num > pick).
1: 당신의 추측이 제가 선택한 숫자보다 낮습니다(즉, num < pick).
0: 당신의 추측이 제가 선택한 숫자와 같습니다(즉, num == pick).
제가 선택한 번호를 반환합니다.
'''

pick = 1


def guess(num):
    global pick
    if num > pick:
        return -1
    elif num < pick:
        return 1
    elif num == pick:
        return 0


def guessNumber(n):
    global pick
    start = 1
    end = n
    while start <= end:
        mid = (start + end) // 2
        check = guess(mid)
        if check == -1:
            end = mid - 1  # 함수를 끝내버린다.
        elif check == 1:
            start = mid + 1
        else:
            return mid




if __name__ == '__main__':
    print(guessNumber(2))