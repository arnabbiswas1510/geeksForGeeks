"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/problem/maximum-index-1587115620
First instinct is to think this is a variation of Kadane - NOT AT ALL though deceptively similar
left Array needs to be monotonically decreasing and right array needs to be mono increasing from right.
Visualize and debug the problem to understand why.
"""

# The solution below with O(n) space is enough
def maximumIndex(arr):
    l,r=arr[0],arr[len(arr)-1]
    left,right=[l],[r]
    #First create left and right arrays
    for i in range(1,len(arr)):
        l=min(l,arr[i])
        left.append(l)
        r=max(r,arr[len(arr)-1-i])
        right.insert(0,r)
    maxDiff=-float('inf')
    i,j=0,0
    while i <len(arr) and j< len(arr):
        if left[i] < right[j]:
            maxDiff = max(maxDiff, j-i)
            j+=1
        else:
            i+=1
    return maxDiff

#This solution with no extra space is similar to trapping rain water
#TODO revisit
def maximumIndex2(A):
    i = 0
    N=len(A)
    j = N - 1
    mx = start = 0
    while i < N:
        if i <= j:
            if A[i] <= A[j]:
                diff = j - i
                if diff > mx:
                    mx = diff
                start += 1
                i = start
                j = N - 1
            else:
                j -= 1
        else:
            start += 1
            i = start
            j = N - 1
    return mx

A=[34, 8, 10, 3, 2, 80, 30, 33, 1]
print(maximumIndex(A))
