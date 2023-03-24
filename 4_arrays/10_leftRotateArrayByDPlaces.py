"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzE5NA%3D%3D

First strategy is to rotateBy1 and then call that function d times. But the cost of this is O(n^2)
Below strategy has cost of n time but also n space
Efficent strategy has cost of n time and 1 space but needs to be memorized
"""


def leftRotateArrayByDPlaces(arr,d):
    temp=[None]*d
    for i in range(len(arr)):
        if i < d:
            temp[i] = arr[i]
        else:
            arr[i-d]=arr[i]
    for i in range(len(arr)-d, len(arr)):
        arr[i]=temp[len(temp)-(len(arr)-i)]
    return arr


def reverse(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    return arr


def leftRotateArrayByDPlacesBest(arr,d):
    arr[0:d]=reverse(arr[0:d])
    arr[d:]=reverse(arr[d:])
    reverse(arr)
    return arr

print(leftRotateArrayByDPlaces([1, 2, 3, 4, 5, 6, 7],2))
print(leftRotateArrayByDPlacesBest([1, 2, 3, 4, 5, 6, 7],2))
