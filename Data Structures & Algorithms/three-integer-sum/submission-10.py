class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()

        for i in range(len(nums)):
            hashMap = {}
            for j in range(i+1,len(nums)):
                y = -nums[i]-nums[j]
                if y in hashMap:
                    output.add(tuple(sorted([nums[i],nums[j],y])))
                hashMap[nums[j]] = j

        return [list(x) for x in output]  
        