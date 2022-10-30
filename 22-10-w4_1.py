from collections import Counter
import copy

def shared_chars(s1, s2):
    return sum((Counter(s1) & Counter(s2)).values())


# 일반 버전
def findlongeststring(sentences):
    result = {}
    for i in sentences:
        result[i] = len(i)
        temp1 = copy.deepcopy(result)
        for j in temp1:
            if shared_chars(j, i) == 0:
                result[j+i] = len(j+i)
    result = dict((x, y) for x, y in sorted(result.items(), key=lambda item: item[1], reverse=True))
    return list(result.keys())[0], list(result.values())[0]


# 재귀 버전
def findlongestcombination(recursionsentence, sentences):
    if len(sentences) == 0:
        return
    comp_sentence = sentences.pop(0)
    if len(comp_sentence) == len(set(comp_sentence)):
        recursionsentence[comp_sentence] = len(comp_sentence)
        for result in list(recursionsentence.keys()):
            if shared_chars(result, comp_sentence) == 0:
                recursionsentence[result + comp_sentence] = len(result + comp_sentence)
    findlongestcombination(recursionsentence, sentences)


def recursion_longest(sentences):
    recursionsentence = {}
    findlongestcombination(recursionsentence, sentences)
    if len(list(recursionsentence.items())) == 0:
        return 0
    else:
        result = dict((x, y) for x, y in sorted(recursionsentence.items(), key=lambda item: item[1], reverse=True))
        return list(result.values())[0]


if __name__ == '__main__':
    origin_sentences = []
    count = int(input("문자열의 갯수(1~16): "))

    for i in range(count):
        origin_sentences.append(input("문자열: "))

    # print(findlongeststring(origin_sentences))
    print(recursion_longest(origin_sentences))
    # print("최대 문자열:", r1, ", 최대 길이:", r2)


