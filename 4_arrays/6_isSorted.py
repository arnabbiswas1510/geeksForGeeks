"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzA4OA%3D%3D
"""

def isSorted(arr):
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

print(isSorted([20,21,45,89,89,90]))
print(isSorted([20,20,45,89,89,90]))
print(isSorted([20,20,78,98,99,97]))
