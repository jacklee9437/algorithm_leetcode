from random import shuffle

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.origin = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.origin[:]
        return self.nums
        
    def shuffle(self) -> List[int]:
        shuffle(self.nums)
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()