"""
퇴플리츠 행렬
m x n 행렬이 주어졌을 때, 이 행렬이 퇴플리츠일 경우 true를 그렇지 않을 경우 false를 반환하세요.

행렬이 왼쪽 위부터 오른쪽 아래까지의 모든 대각선이 동일한 요소를 갖는 경우 토플리츠에요.
"""


def left_shifter(matrix):
    for i in range(1,len(matrix)):
        for j in range(len(matrix[i])):
            if i <= 0 or j <= 0:
                continue
            if matrix[i-1][j-1] != matrix[i][j]:
                return False
    return True


if __name__ == '__main__':
    matrix = [[1,2,3,4],
              [5,1,2,3],
              [9,5,1,2]]
    print(left_shifter(matrix))