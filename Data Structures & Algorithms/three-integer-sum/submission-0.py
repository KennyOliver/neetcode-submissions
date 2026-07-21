class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        TARGET = 0
        triplets = []

        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if ((nums[i] + nums[j] + nums[k]) == TARGET) and (i != j != k):
                        triplets.append([nums[i], nums[j], nums[k]])
        
        # triplets_no_dupes = set([set(t) for t in triplets])

        unique = [list(x) for x in {tuple(sorted(a)) for a in triplets}]

        return unique
