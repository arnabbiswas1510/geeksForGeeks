"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzE5NA%3D%3D
Messed this up while writing. Had to lookup the logic
"""

def fillZerosFromIndex(arr, n):
    for i in range(n,len(arr)):
        arr[i]=0

def moveZerosToEnd(arr):
    i,j=0,0
    while j < len(arr):
        if arr[j] != 0:
            arr[i] = arr[j]
            i+=1
        j+=1
    fillZerosFromIndex(arr,i)
    return arr

print(moveZerosToEnd([1, 2, 0, 0, 0, 3, 6]))
print(moveZerosToEnd([0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]))
