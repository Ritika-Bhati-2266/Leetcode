class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        count = 0
        for i in nums:
            if target==i:
                break
            count+=1
        return count