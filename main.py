import heapq 

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    for i, duration in enumerate(data):
        finish_time, thread_index = heapq.heappop(threads)
        start_time = max(finish_time, output[i-1][1]) if i > 0 else finish_time
        output.append((thread_index, start_time))
        heapq.heappush(threads, (start_time + duration, thread_index))
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for thread_index, start_time in result:
        print(thread_index, start_time)

if __name__ == "__main__":
    main()
