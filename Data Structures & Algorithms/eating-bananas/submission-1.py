class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # fastest eating rate = max(piles)  
        l,r = 1, max(piles)
        k = 0

        while l <= r:
            m = (l+r)//2
            totalHour = 0
            for p in piles:
                hour = math.ceil(p/m)
                totalHour += hour

            if totalHour <= h:
                r = m - 1
                k = m
            
            elif totalHour >= h:
                l = m + 1
        return k         