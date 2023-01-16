"""
문자열 다듬기
소문자와 대문자로 구성된 무자열 s가 주어집니다.

올바른 문자열은 두 개의 인접한 문자 s[i]와 s[i + 1]가 아래의 경우가 없는 문자열입니다.

0 <= i <= s.length - 2
s[i]는 소문자이고 s[i + 1]은 동일한 문자이지만 대문자이거나 그 반대입니다.
문자열을 올바르게 만들기 위해 문자열이 잘못된 두 개의 인접 문자를 선택하고 제거할 수 있습니다. 문자열이 올바르게 될 때까지 계속 이 작업을 수행하면 됩니다.
문자열을 올바륵 만든 후 반환합니다. 주어진 제약 조건 하에서 답은 고유할 것을 보장합니다.

빈 문자열 또한 올바릅니다.
"""

def making_the_string_great(s):
    s = list(s)
    result = []

    while len(s) != 0:
        if len(result) == 0:
            result.append(s.pop(0))
            if len(s) == 0:
                break
        if (result[len(result)-1].islower() and s[0] == result[len(result)-1].upper()) or (result[len(result)-1].isupper() and s[0] == result[len(result)-1].lower()):
            result.pop()
            s.pop(0)
        else:
            result.append(s.pop(0))

    return ''.join(result)


if __name__ == '__main__':
    print(making_the_string_great('s'))