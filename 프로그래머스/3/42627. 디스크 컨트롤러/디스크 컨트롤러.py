def solution(jobs):
    import heapq 
    jobs.sort()
    heap = []
    current_time, completed_jobs, total_response_time = 0, 0, 0
    jobs_idx = 0

    while completed_jobs < len(jobs):
        while jobs_idx < len(jobs) and jobs[jobs_idx][0] <= current_time:
            start, duration = jobs[jobs_idx]
            heapq.heappush(heap, (duration, start))
            jobs_idx += 1

        if heap:
            duration, start = heapq.heappop(heap)
            total_response_time += (current_time - start + duration)
            current_time += duration
            completed_jobs += 1
        else:
            current_time = jobs[jobs_idx][0]
    return total_response_time // completed_jobs
