"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/MjI1NA%3D%3D
"""


def slidingWindowTechnique(arr, k):
    maxSum=0
    for i in range(k):
        maxSum += arr[i]
    currSum=maxSum
    for i in range(k, len(arr)):
        currSum -= arr[i-k]
        currSum += arr[i]
        maxSum=max(currSum,maxSum)
    return maxSum

print(slidingWindowTechnique([100, 200, 300, 400],2))
