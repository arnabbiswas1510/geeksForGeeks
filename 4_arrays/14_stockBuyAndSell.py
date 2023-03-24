"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzIwMw%3D%3D
First solution is identical to maxDiffProblemWithOrder (https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzE5Nw%3D%3D)
But it only gives you the single largest profit, not the sum of all profits (without buying and selling on same day)
Second implementation gives sum of all profits using valley peak approach (this is a diff problem). Valley peak is V Easy
Third implementation uses Kadane's algo (max subarray sum) - For this you need to compute and provide pnl array
pnl will have +ve and -ve nos similar to max subarray sum problem.
Note kadane returns same results as valley peak approach. To alter this to true Kadane make line 44:
currSum=max(arr[i], currSum+arr[i])
"""


def stockBuyAndSell1(arr):
    i,j=0,1
    maxDiff = -float('inf')
    currDiff=0
    while j < len(arr):
        if arr[i] < arr[j]:
            currDiff = max(currDiff,arr[j]-arr[i])
            maxDiff=max(maxDiff,currDiff)
        else:
            i=j
        j+=1
    return maxDiff

#Valley Peak approach, very simple
def stockBuyAndSell2(arr):
    maxDiff = 0
    for j in range(1,len(arr)):
        if arr[j-1] <= arr[j]:
            maxDiff += arr[j]-arr[j-1]
    return maxDiff


def generatePnl(arr):
    pnl=[0]
    for i in range(1,len(arr)):
        pnl.append(arr[i]-arr[i-1])
    return pnl


def kadaneValleyPeak(arr):
    currSum, maxSum = 0, -float('inf')
    for i in range(len(arr)):
        currSum=max(currSum, currSum+arr[i])
        maxSum=max(currSum,maxSum)
    return maxSum

print(kadaneValleyPeak(generatePnl([100, 180, 260, 310, 40, 535, 695])))
print(kadaneValleyPeak(generatePnl([4, 2, 2, 2, 4])))
