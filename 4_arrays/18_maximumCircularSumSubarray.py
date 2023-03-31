"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/video/MTQ2NDU%3D

Intuition:
Max sum may lie completely within the array or may wrap around and lie from j to i where j > i. Hence we need to find
max sum for both scenarios and return the max between the two scenarios.

For the second j to i scenario we find max sum subarray as:
Array sum - (Max Sum subarray of Inverse array) as shown below.

Other two approaches
1. Nested loop and compute current index =  (i+j)%n. Naive O(n^2)
2. You can concatenate two arrays and find max sum subarray for MAX WINDOW SIZE of N. O(2N)

"""


def kadane(arr):
    currSum, maxSum = 0, -float('inf')
    for i in range(len(arr)):
        currSum=max(arr[i], currSum+arr[i])
        maxSum=max(currSum,maxSum)
    return maxSum

def maximumCircularSumSubarray(arr):
    maxOrig = kadane(arr)
    if maxOrig < 0: #Boundary case when every element in array is -ve
        return maxOrig #Kadane is good enough for this boundary case
    arrSum=0
    for i in range(len(arr)):
        arrSum += arr[i]
        arr[i] = -arr[i] #Inverse array
    maxCircular = arrSum + kadane(arr) #Remember this step
    return max(maxOrig, maxCircular)

print(maximumCircularSumSubarray())
