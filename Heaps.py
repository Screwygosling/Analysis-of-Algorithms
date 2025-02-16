class MinHeap:
    def __init__(self):
        self.heap = []
        
    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[(i - 1) // 2] > self.heap[i]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def delete(self, value):
        i = -1
        for j in range(len(self.heap)):
            if self.heap[j] == value:
                i = j
                break
        if i == -1:
            return
        self.heap[i] = self.heap[-1]
        self.heap.pop()
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break
    
    def minHeapify(self, i, n):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minHeapify(smallest, n)
    
    def search(self, element):
        for j in self.heap:
            if j == element:
                return True
        return False

    def getMin(self):
        return self.heap[0] if self.heap else None
    
    def printHeap(self):
        print("Min Heap:", self.heap)

if __name__ == "__main__":
    h = MinHeap()
    values = [3, 2, 1, 15, 5, 4, 45]
    for val in values:
        h.insert(val)
    h.printHeap()

    h.delete(5)
    print("After deleting 5:", h.heap)

    print("Searching for 5:", "Found" if h.search(5) else "Not Found")
    print("Minimum element in heap:", h.getMin())
            
    