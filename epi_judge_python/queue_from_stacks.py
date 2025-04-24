from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self):
        self._input_stack, self._output_stack = [], []

    def enqueue(self, x: int) -> None:
        self._input_stack.append(x)

    def dequeue(self) -> int:
        if not self._output_stack:
            while self._input_stack:
                self._output_stack.append(self._input_stack.pop())

        if not self._output_stack:
            raise IndexError('Dequeue from empty queue')

        return self._output_stack.pop()


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    #q = Queue()
    #q.enqueue(1)
    #q.enqueue(2)
    #q.enqueue(3)

    #r1, r2, r3 = q.dequeue(), q.dequeue(), q.dequeue()
    #print(r1, r2, r3)

    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
