# Necessery to design algorithm for generating row with index in Pascal triangle, example below
#  1
#  11
#  121
#  1331
#  14641
# for 0 row result is [1]

from typing import List


def get_row(A: int) -> List:
  # @param A : integer
  # @return a list of integers
	i = 0
	result = [1]
	while i < A:
		result = get_prev_row(result)
		i += 1
	return result

def get_prev_row(prev_row: List) -> List:
	if len(prev_row) < 2:
		return [1, 1]
	result = []
	for i in range(len(prev_row) - 1):
		result.append(prev_row[i] + prev_row[i+1])
	return [1] + result + [1]

assert(get_row(0) == [1])
assert(get_row(1) == [1, 1])
assert(get_row(2) == [1, 2, 1])
assert(get_row(3) == [1, 3, 3, 1])
assert(get_row(4) == [1, 4, 6, 4, 1])
