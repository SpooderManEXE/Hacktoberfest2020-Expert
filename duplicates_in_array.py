class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for key, val in dic.items():
            if val == 2:
                res.append(key)
        return res
        
        
