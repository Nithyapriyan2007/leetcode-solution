class Solution:
    def canPartition(self, nums):

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = {0}

        for num in nums:
            new_dp = set()

            for s in dp:
                new_dp.add(s + num)

            dp = dp | new_dp

        return target in dp