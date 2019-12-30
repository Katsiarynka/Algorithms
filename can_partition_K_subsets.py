# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/submissions/

from typing import List


def can_partition_k_subsets(nums: List[int], k: int) -> bool:
    target, rest = divmod(sum(nums), k)
    if rest:
        return False

    def search(groups):
        if not nums: return True
        v = nums.pop()
        for i, group_sum in enumerate(groups):
            if group_sum + v <= target:
                groups[i] += v
                if search(groups): return True
                groups[i] -= v
            if not group_sum: break
        nums.append(v)
        return False

    nums.sort()
    if nums[-1] > target: return False
    while nums and nums[-1] == target:
        nums.pop()
        k -= 1
    return search([0] * k)


assert(can_partition_k_subsets([1, 2, 3, 4, 5, 2, 1, 5, 7, 9, 2, 3, 4, 6], 6) == True)
