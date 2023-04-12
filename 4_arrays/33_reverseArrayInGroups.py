"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/problem/reverse-array-in-groups0255
"""

def reverseAnArray(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    return arr
def reverseArrayInGroups(arr, k):
    for i in range(0,len(arr),k):
        arr[i:min(i+(k),len(arr))]=reverseAnArray(arr[i:min(i+(k),len(arr))])
    return arr

print(reverseArrayInGroups([5,6,8,9],3))
