from collections import Counter
import copy


def shared_chars(s1, s2):
    return sum((Counter(s1) & Counter(s2)).values())


def findlongeststring(sentences):
    result = {}
    for i in sentences:
        result[i] = len(i)
        temp1 = copy.deepcopy(result)
        for j in temp1:
            if shared_chars(j, i) == 0:
                result[j+i] = len(j+i)
    result = dict((x, y) for x, y in sorted(result.items(), key=lambda item: item[1], reverse=True))
    print(result)
    return list(result.keys())[0], list(result.values())[0]


if __name__ == '__main__':
    count = int(input("문자열의 갯수(1~16): "))
    sentences = []
    for i in range(count):
        sentences.append(input("문자열: "))
    r1, r2 = findlongeststring(sentences)
    print("최대 문자열:", r1, ", 최대 길이:", r2)


