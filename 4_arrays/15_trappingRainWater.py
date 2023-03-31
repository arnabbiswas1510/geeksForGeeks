"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzIwNA%3D%3D
First follow the solution with extra space and then go to the optimal one
See optimal expln here: https://youtu.be/ZI2z5pq0TqA?t=833
"""


def trappingRainWaterExtraSpace(arr):
    l,r=arr[0],arr[len(arr)-1]
    left,right=[l],[r]
    #First create left and right arrays
    for i in range(1,len(arr)):
        l=max(l,arr[i])
        left.append(l)
        r=max(r,arr[len(arr)-1-i])
        right.insert(0,r)
    water=0
    for i in range(len(arr)):
        water+=min(left[i],right[i])-arr[i] #Understand this
    return water

def trappingRainWater(arr):
    l,r=0,len(arr)-1
    leftMax, rightMax = arr[l], arr[r]
    water=0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, arr[l])
            water += leftMax - arr[l]
        else:
            r -= 1
            rightMax = max(rightMax, arr[r])
            water += rightMax - arr[r]
    return water

print(trappingRainWater([2, 0, 2]))
print(trappingRainWater([3, 0, 2, 0, 4]))
print(trappingRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
