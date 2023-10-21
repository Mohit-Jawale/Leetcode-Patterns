from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        
        if len(intervals)==0:
            return True
        intervals.sort(key=lambda x: x.start)    
        curr_start, curr_end = intervals[0].start,intervals[0].end
        for i in intervals[1:]:
            if curr_end<=i.start:
                ans = True
                curr_end = i.end
            else:
                return False 
        return ans     
