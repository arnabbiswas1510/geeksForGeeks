"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzIxMg%3D%3D

Remember the algo below doesnt actually perform the flips. It only prints them

A Naive Solution is to traverse do two traversals of the array. We first traverse to find the number of groups of 0s
and the number of groups of 1.  We find the minimum of these two.  Then we traverse the array and flip the 1s if groups
of 1s are less. Otherwise, we flip 0s.

How to do it with one traversal of array?

An Efficient Solution is based on the below facts :

There are only two types of groups (groups of 0s and groups of 1s)
Either the counts of both groups are same or the difference between counts is at most 1. For example, in
{1, 1, 0, 1, 0, 0} there are two groups of 0s and two groups of 1s.  In example, {1, 1, 0, 0, 0, 1, 0, 0, 1, 1},
count of groups of 1 is one more than the counts of 0s.
Based on the above facts, we can conclude that if we always flip the second group and other groups that of the same
type as the second group, we always get the correct answer.  In the first case, when group counts are the same, it does
not matter which group type we flip as both will lead to the correct answer.  In the second case, when there is one
extra, by ignoring the first group and starting from the second group, we convert this case to first case
(for subarray beginning from the second group) and get the correct answer.
"""

def minimumConsecutiveFlips(arr):
    for i in range(1,len(arr)):
        #If it is same as first element then it is starting of the interval to be flipped.
        if arr[i] != arr[i-1]:
            if arr[i] != arr[0]:
                print("from %s to " %(i),end="")
                #If it is not same as previous and same as first element, then previous element is end of interval
            else:
                print(i-1) #Remember i-1

minimumConsecutiveFlips([1, 0, 0, 0, 1, 0, 0, 1, 0, 1])
