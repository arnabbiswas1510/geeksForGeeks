"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzIwOQ%3D%3D
Uses Moore's voting algorithm
"""


def mooresVote(arr):
    maj = arr[0]
    vote = 1
    for i in range(1,len(arr)):
        if maj == arr[i]:
            vote +=1
        else:
            vote -= 1
        if vote == 0:
            maj = arr[i]
            vote = 1 #Remember this
    return maj

def majorityElement(arr):
    maj=mooresVote(arr)
    cnt=0
    for num in arr:
        if num == maj:
            cnt += 1
            if cnt > len(arr)//2: #Note not gt eq
                return maj
    return "No Majority element found"

print(majorityElement([3, 3, 4, 2, 4, 4, 2, 4]))
