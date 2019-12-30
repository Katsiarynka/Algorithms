
def deletion_distance(str1: str, str2: str) -> int:
  if str1 == str2:
    return 0
  if not str1 or not str2:
    return len(str1) or len(str2)
  
  memo = [[0] * (len(str1) + 1)] * (len(str2) + 1)
  for i in range(1, len(str2) +1):
    for j in range(1, len(str1) +1):
      
      if str2[i - 1] == str1[j - 1]:
        memo[i][j] = memo[i-1][j-1] + 1
      else:
        memo[i][j] = max(memo[i-1][j], memo[i][j-1])
  return len(str1) + len(str2) - memo[len(str2)][len(str1)] * 2


assert(deletion_distance('task', 'ask') == 1)
assert(deletion_distance('hint', 'hit') == 1)
assert(deletion_distance('cat', 'c') == 2)
