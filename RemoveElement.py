#https://leetcode.com/problems/remove-element/description/
nums=[0,1,2,2,3,0,4,2]
val=2
i=0
j=0
for num in nums:
    if num!=val:
        nums[i]=nums[j]
        i+=1
        j+=1
    else:
        j+=1
print(i)
print(nums)
