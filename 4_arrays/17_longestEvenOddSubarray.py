"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzIwNw%3D%3D
See the trick in line 12
Also see lines 18 and 19 for arrays without any alternating pairs
"""


def longestEvenOddSubarray(arr):
    cnt=1
    maxCnt=0
    for i in range(1,len(arr)):
        #if (arr[i]%2 == 1 and arr[i-1]%2 == 0) or (arr[i]%2 == 0 and arr[i-1]%2 == 1):
        if arr[i]%2 != arr[i-1]%2:
            cnt+=1
        else:
            maxCnt=max(maxCnt,cnt)
            cnt=1
    if maxCnt == 1:
        maxCnt = 0
    return maxCnt

print(longestEvenOddSubarray([1, 2, 3, 4, 5, 7, 9]))
