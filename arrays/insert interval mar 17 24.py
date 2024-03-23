'''
57. Insert Interval
Solved
Medium
Topics
Companies
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.'''
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        x=[]
        for i in intervals:
            if i[1]< newInterval[0]:
                x.append(i)
            elif i[0]>newInterval[1]:
                x.append(newInterval)
                newInterval=i
            elif i[1]>= newInterval[0] or i[0] <= newInterval[1]:
                newInterval[0]=min(i[0],newInterval[0])
                newInterval[1]= max(i[1],newInterval[1])
        x.append(newInterval)
        return x
        