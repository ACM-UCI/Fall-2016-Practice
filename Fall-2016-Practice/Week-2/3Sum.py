import collections

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = set()
        numCounter = collections.Counter(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                valNeeded = -1*(nums[i] + nums[j])
                if (valNeeded in numCounter):
                    if (not valNeeded == nums[i] and not valNeeded == nums[j]):
                        newList = [nums[i], nums[j], valNeeded]
                        newList.sort()
                        triplets.add(tuple(newList))
                        
                    elif (valNeeded == nums[i] and valNeeded == nums[j] and numCounter[valNeeded] > 2):
                        newList = [nums[i], nums[j], valNeeded]
                        newList.sort()
                        triplets.add(tuple(newList))
                    
                    elif (valNeeded == nums[i] and not valNeeded == nums[j] and numCounter[valNeeded] > 1):
                        newList = [nums[i], nums[j], valNeeded]
                        newList.sort()
                        triplets.add(tuple(newList))
                        
                    elif (valNeeded == nums[j] and not valNeeded == nums[i] and numCounter[valNeeded] > 1):
                        newList = [nums[i], nums[j], valNeeded]
                        newList.sort()
                        triplets.add(tuple(newList))
                        
        return list(triplets)
