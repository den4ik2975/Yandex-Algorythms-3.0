nums = []
n = int(input())
for i in range(n):
    nums.append(int(input()))

cnt = 0
ans = 0
for i in range(len(nums) - 1):
    if nums[i + 1] >= nums[i]:
        cnt += nums[i]
    if nums[i + 1] < nums[i]:
        cnt += nums[i + 1]

print(cnt)