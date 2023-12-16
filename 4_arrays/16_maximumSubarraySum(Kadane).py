"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzIwNg%3D%3D

Difference between this problem and stock buy sell is that this problem can have negative values. Only then will this
algo be exercised. Stock prices can never be negative
"""


def kadane(arr):
    currSum, maxSum = 0, -float('inf')
    for i in range(len(arr)):
        currSum=max(arr[i], currSum+arr[i])
        maxSum=max(currSum,maxSum)
    return maxSum

# print(kadane([1, -2, 3, -2]))
# print(kadane([100, 180, 260, 310, 40, 535, 695]))
# print(kadane([4, 2, 2, 2, 4]))
print(kadane( [-2, -3, 4, -1, -2, 1, 5, -3]))
