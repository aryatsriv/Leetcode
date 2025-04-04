
# Code


# Testcase
# Testcase
# Test Result
# 540. Single Element in a Sorted Array
# Solved
# Medium
# Topics
# Companies
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        s=0
        e=len(nums)-1

        

        while s<=e:
            mid=(s+e)//2
            if (mid>0 and mid<len(nums)-1 and nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]) or (mid==0 and mid<len(nums)-1 and nums[mid]!=nums[mid+1]) or (mid>0 and mid==len(nums)-1 and nums[mid]!=nums[mid-1]):
                return nums[mid]
            elif(mid%2==0 and mid<len(nums)-1 and nums[mid]==nums[mid+1]) or (mid%2==1 and mid>0 and nums[mid]==nums[mid-1]):
                s=mid+1
            else:
                e=mid-1
        

        return -1