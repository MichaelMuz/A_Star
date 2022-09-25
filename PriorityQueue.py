# Priority Queue using min heap data structure implementation
# Usage:
#    To make a priority queue use `pq = PriorityQueue()`
#    To get the next element use `.get()`
#    To add an element use `.put([value])`

class PriorityQueue:

    def __init__(self):
        self.size = 0
        self.heap = [0]

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return 2 * pos + 1

    def isLeafNode(self, pos):
        return pos * 2 > self.size

    def swap(self, p1, p2):
        self.heap[p1], self.heap[p2] = self.heap[p2], self.heap[p1]

    def heapify(self, pos):
        if not self.isLeafNode(pos):
            if self.heap[self.leftChild(pos)] < self.heap[pos]:
                self.swap(self.leftChild(pos), pos)
                self.heapify(self.leftChild(pos))
            elif self.heap[self.rightChild(pos)] < self.heap[pos]:
                self.swap(self.rightChild(pos), pos)
                self.heapify(self.rightChild(pos))

    def put(self, val):
        self.size += 1
        # Auto resize (append) if needed
        if len(self.heap) <= self.size:
            self.heap.append(val)
        else:
            self.heap[self.size] = val

        cpos = self.size

        while self.heap[cpos] < self.heap[self.parent(cpos)]:
            self.swap(cpos, self.parent(cpos))
            cpos = self.parent(cpos)

    def get(self):
        ret = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heapify(1)
        return ret

    def Print(self):
        print(self.heap)

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.Print()
    pq.put(47)
    pq.put(50)
    pq.Print()
    pq.put(49)
    pq.Print()
    pq.put(48)
    pq.Print()
    pq.put(46)
    pq.Print()
    pq.put(45)
    pq.Print()
    pq.put(44)
    pq.Print()
    pq.get()
    pq.Print()
    pq.put(43)
    pq.Print()
    pq.put(42)
    pq.Print()

