"""
문자열의 첫 번째 고유 문자
문자열 s가 주어질 때, 그 안에서 반복되지 않는 첫 번째 문자를 찾고 해당 인덱스를 반환합니다. 존재하지 않으면 -1을 반환합니다.
"""


def firstUniqChar(s):
    for t in s:
        if s.count(t) == 1:
            return s.find(t)
    return -1


if __name__ == '__main__':
    s = "aabb"
    # k, expectedNums = removeDuplicates(num)
    print(firstUniqChar(s))
