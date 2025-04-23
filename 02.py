def rotar(nums, k):
    k %= len(nums)
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]

