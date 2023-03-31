"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzIwNg%3D%3D
"""


def kadane(arr):
    currSum, maxSum = 0, -float('inf')
    for i in range(len(arr)):
        currSum=max(arr[i], currSum+arr[i])
        maxSum=max(currSum,maxSum)
    return maxSum

print(kadane([1, -2, 3, -2]))
