class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for words in strs:
            COUNT = [0] * 26  # a-z [0,0,0,0,...,0]
            
            for i in words:
                COUNT[ord(i)-ord("a")] += 1 # a-a =0, b-a=1, c-a=2, d-a=3, ... , z-a=25
            
            if tuple(COUNT) not in hashMap:
                hashMap[tuple(COUNT)] = []

            hashMap[tuple(COUNT)].append(words)
        
        return list(hashMap.values())