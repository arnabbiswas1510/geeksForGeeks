"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzE5Nw%3D%3D
Remember to have currDiff and maxDiff
Diff from Kadane in that Kadane doesnt require two pointers. But both are O(n)
"""


def maxDiffProblemWithOrder(arr):
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


print(maxDiffProblemWithOrder([2, 3, 10, 6, 4, 8, 1]))
print(maxDiffProblemWithOrder([7, 9, 5, 6, 3, 2]))
