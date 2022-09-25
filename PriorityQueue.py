# Priority Queue using min heap data structure implementation
# Usage:
#    To make a priority queue use `pq = PriorityQueue()`
#    To get the next element use `.get()`
#    To add an element use `.put([value])`

class PriorityQueue:

    def __init__(self):
        self.size = 0
        self.heap = []

    def parent(self, pos: int) -> int:
        return pos // 2

    def left_child(self, pos: int) -> int:
        return 2 * pos

    def right_child(self, pos: int) -> int:
        return 2 * pos + 1

    def is_leaf(self, pos: int) -> int:
        return pos * 2 > self.size

    def swap(self, p1: int, p2: int) -> int:
        self.heap[p1], self.heap[p2] = self.heap[p2], self.heap[p1]

    def heapify(self, pos: int):
        if not self.is_leaf(pos):
            if self.heap[self.left_child(pos)] < self.heap[pos]:
                self.swap(self.left_child(pos), pos)
                self.heapify(self.left_child(pos))
            elif self.heap[self.right_child(pos)] < self.heap[pos]:
                self.swap(self.right_child(pos), pos)
                self.heapify(self.right_child(pos))

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

    def print(self):
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
