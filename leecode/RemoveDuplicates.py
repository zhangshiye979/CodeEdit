# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
nums = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6]

i = 0
j = 0
while j < len(nums):
    if nums[i-1] != nums[j]:
        nums[i] = nums[j]
        i += 1
        j += 1
    # 相等的时候
    else:
        j += 1
print(min(i, len(nums)))
print(nums)
