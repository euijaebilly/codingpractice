"""
문자열의 모음 뒤집기
문자열 s가 주어질 때, 문자열의 모든 모음만 뒤집은 문자열을 반환하세요.

모음은 'a', 'e', 'i', 'o', 'u'이며, 대문자와 소문자 모두 한 번 이상 나타날 수 있습니다.
"""

def vowelsreplacerV1(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    temp = ''
    vowels_in = []
    # for 문을 이용해서 모음을 따로 리스팅 한 후 리버스하여 배치
    for i in range(len(s)):
        if s[i] in vowels:
            vowels_in.append(s[i])
            result.append(temp)
            temp = ''
            continue
        temp += s[i]
    result.append(temp)
    temp = ''
    for chars in result:
        temp += chars
        if len(vowels_in) == 0:
            break
        temp += vowels_in.pop()
    print(temp)


def vowelsreplacerV2(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


if __name__ == '__main__':
    vowelsreplacerV1('leeeuijae')