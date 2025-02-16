from collections import deque

if __name__ == "__main__":
    q = deque()
    q.append('0')
    q.append('1')
    q.append('3')
    q.append('4')

    print("Initial queue")
    print(q)
    
    print("\nElements dequeued from the queue")
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())

    print("\nQueue after removing elements")
    print(q)