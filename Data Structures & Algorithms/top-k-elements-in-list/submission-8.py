class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        COUNT = [[] for i in range(len(nums)+1)]
        myHash = {}
        
        for i in nums:
            myHash[i] = 1 + myHash.get(i, 0)
        for key, value in myHash.items():
            COUNT[value].append(key)
        
        res = []
        for i in range(len(COUNT)-1, -1, -1):
            for ele in COUNT[i]:
                res.append(ele)
                if len(res) == k:
                    return res
