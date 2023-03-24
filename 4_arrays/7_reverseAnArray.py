"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzE5Mg%3D%3D
Remember len(arr)-i-1, line 8
"""

def reverseAnArray(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    return arr

print(reverseAnArray([1, 2, 3]))
print(reverseAnArray([4, 5, 1, 2]))
