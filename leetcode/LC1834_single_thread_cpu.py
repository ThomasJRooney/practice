class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        next_task, task_processing_order = [], []
        sorted_tasks = [(enqueue, process, idx) for idx, (enqueue, process) in enumerate(tasks)]
        sorted_tasks.sort()
        time, task_index = 0, 0
        while task_index < len(tasks) or next_task:
            if not next_task and time < sorted_tasks[task_index][0]:
                time = sorted_tasks[task_index][0]
            while task_index < len(sorted_tasks) and time >= sorted_tasks[task_index][0]:
                _, process_time, original_index = sorted_tasks[task_index]
                heapq.heappush(next_task, (process_time, original_index))
                task_index += 1
            process_time, index = heapq.heappop(next_task)
            time += process_time
            task_processing_order.append(index)
        return task_processing_order