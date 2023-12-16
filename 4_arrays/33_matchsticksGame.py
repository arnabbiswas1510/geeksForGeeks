"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/problem/-matchsticks-game4906

The intuition in this question is that 1+k (assuming 1 to k matchsticks) would be the target sum in each round of play
You can always add upto k in 2 rounds if your range is till k+1
"""


def matchsticksGame(n,k):
    return n%(k+1) if n%(k+1) != 0 else -1


print(matchsticksGame(16,4))
