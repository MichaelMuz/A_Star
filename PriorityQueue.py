from typing import TypeVar, Generic

from Node import Node


# Priority Queue using min heap data structure implementation
# Usage:
#    To make a priority queue use `pq = PriorityQueue()`
#    To get the next element use `.get()`
#    To add an element use `.put([value])`

def parent(pos: int) -> int:
    return pos // 2


def left_child(pos: int) -> int:
    return 2 * pos


def right_child(pos: int) -> int:
    return 2 * pos + 1


class PriorityQueue:

    def __init__(self):
        self.size = 0
        # Dummy node value
        self.queue = [Node(0, 0, 0)]

    def qsize(self):
        return self.size

    def is_leaf(self, pos: int) -> int:
        return pos * 2 > self.size

    def swap(self, p1: int, p2: int):
        self.queue[p1], self.queue[p2] = self.queue[p2], self.queue[p1]

    def heapify(self, pos: int):
        if not self.is_leaf(pos):
            if self.queue[left_child(pos)] < self.queue[pos]:
                self.swap(left_child(pos), pos)
                self.heapify(left_child(pos))
            elif self.queue[right_child(pos)] < self.queue[pos]:
                self.swap(right_child(pos), pos)
                self.heapify(right_child(pos))

    def put(self, val: Node):
        self.size += 1
        # Auto resize (append) if needed
        if len(self.queue) <= self.size:
            self.queue.append(val)
        else:
            self.queue[self.size] = val

        cpos = self.size

        while self.queue[cpos] < self.queue[parent(cpos)]:
            self.swap(cpos, parent(cpos))
            cpos = parent(cpos)

    def get(self) -> Node:
        ret = self.queue[1]
        self.queue[1] = self.queue[self.size]
        self.size -= 1
        self.heapify(1)
        return ret

    def print(self):
        for i in self.queue:
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
