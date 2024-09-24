from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals)
    merged_interval = [None, None]
    collection_of_intervals = []
    for i in range(len(intervals)):
        current_interval = intervals[i]
#        print("in loop: ", i, current_interval, merged_interval, collection_of_intervals)
        if merged_interval == [None, None]:
            merged_interval = current_interval

        elif current_interval[0] <= merged_interval[1] < current_interval[1]:
            merged_interval[1] = current_interval[1]
        
        else:
            if not collection_of_intervals:
                collection_of_intervals.append(merged_interval)
            elif merged_interval != collection_of_intervals[-1]:
                collection_of_intervals.append(merged_interval)
            if current_interval[1] > merged_interval[1] and current_interval[0] > merged_interval[0]:
                merged_interval = current_interval
        
#        print("after loop: ", i, current_interval, merged_interval, collection_of_intervals)   
    
    if merged_interval != [None, None] and not collection_of_intervals:
        collection_of_intervals.append(merged_interval)
    elif merged_interval != [None, None] and merged_interval != collection_of_intervals[-1]:
        collection_of_intervals.append(merged_interval)

    return collection_of_intervals


print(merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
print(merge([[1,4],[4,5]]), [[1,5]])
print(merge([[1,4],[0,4]]), [[0,4]])
print(merge([[1,4],[2,3]]), [[1,4]])