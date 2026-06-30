class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0
        # move all non- zero elements to the front 
        for num in nums:
            if num != 0:
                nums[insert_pos] = num 
                insert_pos += 1

        # fill the remaining position with zero 
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
        



        """
        Do not return anything, modify nums in-place instead.
        """
        