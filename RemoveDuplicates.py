#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
nums = [1,1,2]

for num in nums[:]:
    while num in nums:
        nums.remove(num)

