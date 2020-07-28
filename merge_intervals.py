# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
# class Solution:
#     def mergeInterval(self, interval,newinterval):
#         if (len(interval)== 0):
#             return newinterval
#
#         i = 0
#         while i<len(interval):
#             if interval[i].start > newinterval.start:
#                 break
#                 i += 1
#         interval.insert(i, newinterval)
#         res = [interval[0]]
#
#         for i, e in enumerate(interval, start=1):
#             if e.start <= res[-1].end:
#                 res[-1].end = max(res[-1].end, e.end)
#             else:
#                 res.append(e)
#         return res
#
# if __name__ == '__main__':
#     g = Solution()
#     intervals = [Interval(1,3),Interval(6,9)]
#     newinterval = Interval(2,5)
#     print(g.mergeInterval(intervals,newinterval))

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#
#
# class Solution:
#
#     def insert(self, intervals, newInterval):
#         if len(intervals) == 0:
#             return [newInterval]
#
#         i = 0  # Find the right location, insert a new interval, regardless of the overlap problem
#         while i < len(intervals):
#             if intervals[i].start > newInterval.start:
#                 break
#             i += 1
#
#         intervals.insert(i, newInterval)  # Insert new interval
#
#         res = [intervals[0]]  # Define the result list and put the first element in it
#
#         for i, e in enumerate(intervals, start=1):  # Add new elements in turn, and consider overlapping issues
#             if e.start <= res[-1].end:
#                 res[-1].end = max(res[-1].end, e.end)
#             else:
#                 res.append(e)
#         return res
#
#
# if __name__ == '__main__':
#
#     solu = Solution()
#     intervals = [Interval(1, 3), Interval(6, 9)]
#     newInterval = Interval(2, 5)
#     print(solu.insert(intervals, newInterval))


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution:
    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        right = left = 0
        while right < len(intervals):
            if start <= intervals[right].end:
                if end < intervals[right].start:
                    break
                start = min(start, intervals[right].start)
                end = max(end, intervals[right].end)
            else:
                left += 1
            right += 1
        return intervals[:left] + [Interval(start, end)] + intervals[right:]

if __name__ == '__main__':
    solu = Solution()
    intervals = [Interval(1, 3), Interval(6, 9)]
    newInterval = Interval(2, 5)
    print(solu.insert(intervals, newInterval))
    #answer = solu.insert(intervals, newInterval)
    #for ans in answer:
     #   print(ans.start, ans.end)

