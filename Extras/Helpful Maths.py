str1 = '2'#input()
nums = list(map(int,(str1.split('+'))))
nums.sort()
nums = [str(x) for x in nums]
nums = "+".join(nums)
print(nums)