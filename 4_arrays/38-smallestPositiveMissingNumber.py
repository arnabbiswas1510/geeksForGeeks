"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/problem/smallest-positive-missing-number-1587115621

Easiest way is to sort and traverse. But that is an NLogN solution. Below does this in N
Understand why smallest missing number has to lie in the range 1..N for array of size N
"""


def smallestPositiveMissingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within
         the range [1,...,l+1]
    """
    nums.append(0) #This is needed since
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
    # After this loop the array looks like [13,9,0,6,5]
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            return i
    return n

print(smallestPositiveMissingNumber([3,4,-1,1]))
