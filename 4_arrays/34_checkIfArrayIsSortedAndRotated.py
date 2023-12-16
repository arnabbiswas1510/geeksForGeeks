"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/problem/check-if-array-is-sorted-and-rotated-clockwise-1587115620
Note that in below one liner the scenario nums[0] < nums[-1] is also considered
"""

def checkIfArrayIsSortedAndRotated(nums):
    return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1

print(checkIfArrayIsSortedAndRotated([3,4,1,2]))
