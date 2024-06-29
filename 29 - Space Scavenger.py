rules = [
  input(),
  input(),
  input(),
  input(),
  input(),
  input()
]
letter, number = input().split()
hlp = {
  'N': 0,
  'S': 1,
  'W': 2,
  'E': 3,
  'U': 4,
  'D': 5
}
dp = [[0] * int(number) for i in range(6)]

for i in range(int(number)):
  for j in range(6):
    cnt = 0
    for k in rules[j]:
      cnt += dp[hlp[k]][i - 1]
    dp[j][i] = 1 + cnt

print(dp[hlp[letter]][int(number) - 1])