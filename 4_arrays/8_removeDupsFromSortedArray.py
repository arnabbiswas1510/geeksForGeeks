"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzE5Mw%3D%3D
"""

def removeDupsFromSortedArray(arr):
    i,j=0,1
    while j < len(arr):
        if arr[i] != arr[j]:
            i+=1
            arr[i]=arr[j]
        j+=1
    return arr[:i+1]


print(removeDupsFromSortedArray([2, 2, 2, 2, 2]))
print(removeDupsFromSortedArray([1, 2, 2, 3, 4, 4, 4, 5, 5]))
