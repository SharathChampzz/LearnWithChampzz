class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        if not intervals:
            return [new_interval]

        merged_intervals = []
        num_intervals = len(intervals)
        index = 0

        while index < num_intervals or new_interval:
            if index >= num_intervals or (new_interval and new_interval[0] < intervals[index][0]):
                current_interval = new_interval
                new_interval = []  # Do not increment index here
            else:
                current_interval = intervals[index]
                index += 1  # Move to the next interval

            if not merged_intervals or merged_intervals[-1][1] < current_interval[0]:
                merged_intervals.append(current_interval)  # No overlap
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], current_interval[1])

        return merged_intervals


    def Oldinsert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        index = 0

        # find insert position and insert it
        for index, interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                intervals.insert(index, newInterval)
                break
        else:
            index += 1
            intervals.append(newInterval)

        print(intervals)

        # handle overlap
        # n = len(intervals)

        def check_overlap(index) -> bool:
            if index >= (len(intervals)-1):
                return False # we are at end

            current_end_interval = intervals[index][1]
            next_start_interval = intervals[index + 1][0]
            
            return current_end_interval >= next_start_interval

        def merge_overlap(index):
            if index >= (len(intervals)-1):
                raise Exception('You incorrectly evaluated the last index as overlapped')

            intervals[index][1] = max(intervals[index][1], intervals[index + 1][1])
            intervals.pop(index + 1) # after merging pop it out

        if index > 0:
            index -= 1 # start looking from overlap from here

        while index < (len(intervals)-1):
            if check_overlap(index):
                merge_overlap(index)
            else:
                index += 1

        return intervals

