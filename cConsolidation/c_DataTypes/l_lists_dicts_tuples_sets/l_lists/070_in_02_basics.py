# -*- coding: utf-8 -*-
"""
"""

# ALL members fit the condition?
nums=[55,44,33,22,11]

if all([i>10 for i in nums]):
    print("All larger than ",10)
    
nums_gt_10 = [i>0 for i in nums]; print(nums_gt_10)

print(all(nums_gt_10))

# ANY member fits the condition?
nums=[55,44,33,22,11]
if any([i>50 for i in nums]):
    print("At least one larger than ",50)

print(any(nums_gt_10))
