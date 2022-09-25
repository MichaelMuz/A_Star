from typing import TypeVar, Generic

from Node import Node

# Priority Queue using min heap data structure implementation
# Usage:
#    To make a priority queue use `pq = PriorityQueue()`
#    To get the next element use `.get()`
#    To add an element use `.put([value])`

class PriorityQueue:

    def __init__(self):
        self.size = 0
        # Dummy node value
        self.heap = [Node(0, 0, 0)]

    def parent(self, pos: int) -> int:
        return pos // 2

    def left_child(self, pos: int) -> int:
        return 2 * pos

    def right_child(self, pos: int) -> int:
        return 2 * pos + 1

    def is_leaf(self, pos: int) -> int:
        return pos * 2 > self.size

    def swap(self, p1: int, p2: int):
        self.heap[p1], self.heap[p2] = self.heap[p2], self.heap[p1]

    def heapify(self, pos: int):
        if not self.is_leaf(pos):
            if self.heap[self.left_child(pos)] < self.heap[pos]:
                self.swap(self.left_child(pos), pos)
                self.heapify(self.left_child(pos))
            elif self.heap[self.right_child(pos)] < self.heap[pos]:
                self.swap(self.right_child(pos), pos)
                self.heapify(self.right_child(pos))

    def put(self, val: Node):
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

    def get(self) -> Node:
        ret = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heapify(1)
        return ret

    def print(self):
        for i in self.heap:
            print(i.print())


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.print()
    pq.put(Node(1, 1, 50))
    pq.put(Node(1, 1, 47))
    pq.print()
    pq.put(Node(1, 1, 49))
    pq.print()
    pq.put(Node(1, 1, 48))
    pq.print()
    pq.put(Node(1, 1, 46))
    pq.print()
    pq.put(Node(1, 1, 45))
    pq.print()
    pq.put(Node(1, 1, 44))
    pq.print()
    pq.get()
    pq.print()
    pq.put(Node(1, 1, 43))
    pq.print()
    pq.put(Node(1, 1, 42))
    pq.print()
