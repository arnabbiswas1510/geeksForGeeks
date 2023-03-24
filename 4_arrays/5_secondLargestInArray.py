"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzA4Nw%3D%3D
Order of lines 10 and 11 mattered
Dont forget and num != largest in line 13
"""

def secondLargestInArray(arr):
    largest, secondLargest = -float('inf'), -float('inf')
    for num in arr:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondLargest = num
    return secondLargest

print(secondLargestInArray([12, 35, 1, 10, 34, 1]))
print(secondLargestInArray([10, 5, 10]))
print(secondLargestInArray([10, 10, 10]))

