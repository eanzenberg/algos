from typing import List
from collections import defaultdict, deque


def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    start_queue = deque()
    id_times = defaultdict(int)

    for log in logs:
        id, func, time = log.split(":")
        time = int(time)
        if func == 'start':
            if start_queue:
                last_id, last_timestamp = start_queue[-1]
                id_times[last_id] += time - last_timestamp
            start_queue.append((id, time))
        elif func == 'end':
            _, last_timestamp = start_queue.pop()
            total_time = time - last_timestamp + 1
            id_times[id] += total_time
            print(id_times, last_timestamp, time, start_queue)            
            if start_queue:
                prior_id, _ = start_queue[-1]
                start_queue[-1] = (prior_id, time + 1)
    
    ans = []
    for i in range(n):
        ans.append(id_times[str(i)])
    return ans


print(exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]), [3,4])
print(exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]), [8])