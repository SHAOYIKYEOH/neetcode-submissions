class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(numbers)):
            a = target - numbers[i]
            if a in hashMap:
                return [hashMap[a] + 1, i+1]
            else:
                hashMap[numbers[i]] = i