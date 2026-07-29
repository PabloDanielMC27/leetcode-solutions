# 621. Task Scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # heap + queue
        # d = Counter(tasks)

        # queue = [(-count, 0, task) for task, count in d.items()]
        # heapify(queue)

        # idle = deque()
        # t = 1

        # while queue or idle:

        #     while idle and idle[0][1] <= t:
        #         count, time, task = idle.popleft()
        #         heapq.heappush(queue, (count, time, task))

        #     if queue:
        #         count, time, task = heapq.heappop(queue)
        #         count += 1

        #         if count < 0:
        #             idle.append((count, t + n + 1, task))
        #     t += 1
        # return t - 1

        # math
        d = Counter(tasks)

        value = (n + 1) * (max(d.values()) - 1)
        for val in d.values():
            if val == max(d.values()):
                value += 1

        return max(value, len(tasks))




        
