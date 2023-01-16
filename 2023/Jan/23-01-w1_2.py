"""
길이가 모두 같은 n 문자열로 이루어진 strs배열이 주어집니다.
문자열은 각 줄에 하나씩 배열되어 그리드를 만들 수 있습니다.

예를 들어 strs = ["abc", "bce", "cae"]은 다음과 같이 배열할 수 있습니다.
abc
bce
cae

사전순으로 정렬되지 않은 열을 삭제하려고 합니다. 위 예에서 (0-인덱스) 열 0('a', 'b', 'c')와 2('c', 'e', 'e')는 정렬되어 있지만 열 1('b', 'c', 'a')는 그렇지 않습니다. 따라서 1번 열을 삭제해야합니다.

삭제해야 할 열 수를 반환하세요.
"""

from typing import List

def minDeletionSize(strs:List[str]):
    del_col = 0
    test_list = []
    for i in range(0, len(strs[0])):
        for j in range(0,len(strs)):
            test_list.append(strs[j][i])
        if test_list != sorted(test_list):
            del_col+=1
        test_list = []

    return del_col

if __name__ == '__main__':
    strs = ["zyx","wvu","tsr"]

    print(minDeletionSize(strs))