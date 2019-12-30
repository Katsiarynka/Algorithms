
from typing import List


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '%s-%s' %(self.start, self.end)

    def __eq__(self, others):
        return (self.start, self.end)  == (others[0].start, others[0].end)


def insert(intervals, new_interval):
    # Possible cases:
    # 1) inside existing interval
    # 2) inside empty
    # 3) outside existing interval
    start, end = new_interval.start, new_interval.end
    left = right = 0

    while right < len(intervals):
        if intervals[right].end >= start:
            if intervals[right].start > end:
                break

            start = min(intervals[right].start, start)
            end = max(intervals[right].end, end)
        else:
            left += 1
        right += 1
    return intervals[:left] + [Interval(s=start, e=end)] + intervals[right:]

assert(insert([Interval(1, 5), Interval(6, 9)], Interval(3, 10)) == Interval(1, 10))