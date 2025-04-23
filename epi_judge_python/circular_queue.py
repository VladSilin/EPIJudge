from test_framework import generic_test
from test_framework.test_failure import TestFailure

# Requirements
# - Constructor w/ init. capacity
# - Enqueue fn.
# - Dequeue fn.
# - Fn. returning the num. elems. stored
# - Dynamic resizing

# Examples:
# [1, 2, 3, 4, 5, 6]
#           h
#                 t
# [4, 5, 6, 1, 2, 3, 4, x, x, x, x, x, x, x, x]
#  h
#  t

class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:
        # TODO: Add to notes (protected vars. w/ _)
        self._q = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x: int) -> None:
        if (self._num_queue_elements == len(self._q)):
            self._q = (self._q[self._head:] + self._q[:self._head])
            self._head, self._tail = 0, self._num_queue_elements
            self._q += [None] * (len(self._q) * Queue.SCALE_FACTOR - len(self._q))


        self._q[self._tail] = x
        # TODO: Add to notes (wraparound logic)
        self._tail = (self._tail + 1) % len(self._q)
        self._num_queue_elements += 1


    def dequeue(self) -> int:
        if not self._num_queue_elements:
            raise IndexError('empty queue')

        self._num_queue_elements -= 1
        ret = self._q[self._head]

        self._head = (self._head + 1) % len(self._q)

        return ret

    def size(self) -> int:
        return self._num_queue_elements


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    #q = Queue(3)

    #q.enqueue(1)
    #q.enqueue(2)
    #q.enqueue(3)

    #q.enqueue(4)

    #d1 = q.dequeue()
    #d2 = q.dequeue()

    #q.enqueue(4)
    #q.enqueue(5)
    #q.enqueue(6)
    #q.enqueue(7)
    #q.enqueue(8)
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
