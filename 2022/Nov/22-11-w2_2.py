"""
정렬된 배열에서 중복 제거
내림차순으로 정렬된 정수 배열 번호가 주어지면 각 고유 요소가 한 번만 나타나도록 중복 항목을 제자리에서 제거합니다. 요소의 상대적 순서는 동일하게 유지되어야 합니다.

일부 언어에서는 배열의 길이를 변경할 수 없으므로 결과를 배열 nums의 첫 번째 부분에 배치해야 합니다. 좀 더 형식적으로,
중복을 제거한 후 k요소가 있으면 nums의 처음 k 요소가 최종 결과를 보유해야 합니다. 처음 k개 요소를 넘어 무엇을 남겨두는지는 중요하지 않습니다.

nums의 처음 k 슬롯에 최종 결과를 배치한 후 k를 반환합니다.

다른 배열에 추가 공간을 할당하지 마세요. O(1)의 추가 메모리를 사용하고 제자리에서 입력 배열을 수정하여 이 작업을 수행해야 합니다.

<사용자 정의 판단>

판단은 다음 코드로 솔루션을 테스트합니다.

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
"""
from collections import OrderedDict

def removeDuplicates(nums):
    expected = list(map(int, OrderedDict.fromkeys(nums)))
    for i in range(len(nums)):
        if len(expected) <= i:
            nums.pop()
            continue
        nums[i] = expected[i]
    return len(expected)


if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    #k, expectedNums = removeDuplicates(num)
    print(removeDuplicates(nums), nums)

