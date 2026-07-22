class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = []
        pick = [False]*len(nums)
        
        def backtrack():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return 
            
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    backtrack()
                    perm.pop()
                    pick[i] = False
        backtrack()
        
        return ans


