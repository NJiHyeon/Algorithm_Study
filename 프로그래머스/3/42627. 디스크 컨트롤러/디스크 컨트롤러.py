def solution(jobs):
    import heapq
    # start 시간이 짧은순대로 정렬 
    jobs.sort()
    heap = []
    current_time, completed_jobs, total_time = 0, 0, 0
    jobs_idx = 0
    
    while completed_jobs < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업 모두 추가
        while jobs_idx < len(jobs) and jobs[jobs_idx][0] <= current_time:
            start, duration = jobs[jobs_idx]
            heapq.heappush(heap, (duration, start))
            jobs_idx += 1
            
        # 추가된 작업 처리하기 
        if heap:
            duration, start = heapq.heappop(heap)
            total_time += (current_time - start + duration)
            current_time += duration
            completed_jobs += 1
        else:
            current_time = jobs[jobs_idx][0]
            
    return total_time // len(jobs)