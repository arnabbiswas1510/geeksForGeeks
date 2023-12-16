"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/problem/-rearrange-array-alternately-1587115620

Another variation of storing 2 elements in same cell. See method below for max and min array
"""

def rearrangeArrayAlternately(A):
    N=len(A)
    max_idx = N - 1
    min_idx = 0

    mx = A[N-1] + 1

    for i in range(0, N) :
        if i % 2 == 0 :
            A[i] += (A[max_idx] % mx ) * mx
            max_idx -= 1

        else :
            A[i] += (A[min_idx] % mx ) * mx
            min_idx += 1

    for i in range(0, N) :
        A[i] = A[i] // mx
    return A

print(rearrangeArrayAlternately([10,20,30,40,50,60,70,80,90,100,110]))
