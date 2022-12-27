"""
Flood Fill

이미지는 m x n 정수 그리드  image로 표현되며 여기서 image[i][j]는 이미지 픽셀 값을 나타냅니다.
또한 세 개의 정수  sr, sc 및 color가 제공됩니다. 픽셀 image[sr][sc]에서 시작하여 이미지에 플러드 필을 수행해야 합니다.
플러드 필을 수행하려면 시작 픽셀과 시작 픽셀과 동일한 색상의 시작 픽셀에 4방향으로 연결된 픽셀,
그리고 해당 픽셀에 4방향으로 연결된(동일한 색상)을 고려합니다. 앞서 언급한 모든 픽셀의 색상을 color로 바꿉니다.
플러드 필을 수행한 후 수정된 이미지를 반환합니다.
"""
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        select = image[sr][sc]

        def dfs(sr,sc):
            if image[sr][sc] != select:
                return
            else:
                if image[sr][sc] == color:
                    return
                image[sr][sc]=color
                if sr - 1 >= 0:
                    dfs(sr - 1, sc)
                if sc - 1 >= 0:
                    dfs(sr, sc-1)
                if sr + 1 < len(image):
                    dfs(sr + 1, sc)
                if sc + 1 < len(image[0]):
                    dfs(sr, sc+1)
                return

        dfs(sr,sc)
        return image


if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    test = Solution()
    print(test.floodFill(image, sr, sc, color))
