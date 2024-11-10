from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections

# isbn: ABCDEFGHI X
# X = A + B + ... + I
#
# - key = isbn, value = price
# - If ISBN exists, insert updates entry to be the "most recently used" (do NOT change price)
# - Lookup also updates entry to be "most recently used"

# lru_cache = LruCache(10)

# lru_cache.insert(123456789 X, 40)
# lru = 1
# lru_cache.insert(223456799 X, 50)
# lru_cache.insert(123456799 X, 60)

# lru_cache.lookup(123456789 X)
# lru_cache.erase(123456789 X)


class LruCache0:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.cache_map = {}
        self.key_queue = []

    def lookup(self, isbn: int) -> int:
        if isbn in self.cache_map:
            self.key_queue.pop(self.key_queue.index(isbn))
            self.key_queue.append(isbn)
            return self.cache_map[isbn]
        else:
            return -1

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.cache_map:
            self.key_queue.pop(self.key_queue.index(isbn))
            self.key_queue.append(isbn)
            return

        if self.size >= self.capacity:
            lru_key = self.key_queue.pop(0)
            self.cache_map.pop(lru_key)
            self.size -= 1

        self.cache_map[isbn] = price
        self.key_queue.append(isbn)
        self.size += 1

    def erase(self, isbn: int) -> bool:
        if isbn in self.cache_map:
            self.key_queue.pop(self.key_queue.index(isbn))
            self.cache_map.pop(isbn)
            self.size -= 1
            return True
        else:
            return False

    def __str__(self):
        return str(self.key_queue) + '\n' + str(self.cache_map)


class LruCache:
    def __init__(self, capacity: int) -> None:
        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn: int) -> int:
        if isbn not in self._isbn_price_table:
            return -1

        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price

        return price

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif self._capacity <= len(self._isbn_price_table):
            self._isbn_price_table.popitem(last=False)

        self._isbn_price_table[isbn] = price

    def erase(self, isbn: int) -> bool:
        return self._isbn_price_table.pop(isbn, None) is not None

    def __str__(self):
        return str(self._isbn_price_table)


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    #lru_cache = LruCache(3)
    #lru_cache.insert(0, 10)
    #lru_cache.insert(1, 20)
    #lru_cache.insert(2, 30)
    #lru_cache.insert(3, 40)
    #lru_cache.insert(4, 50)
    ## lru_cache.insert(3, 70)
    #lru_cache.lookup(3)
    #lru_cache.lookup(4)
    #lru_cache.lookup(4)
    #lru_cache.lookup(5)
    #lru_cache.erase(3)
    #lru_cache.insert(5, 70)
    #lru_cache.insert(6, 80)
    #print(lru_cache)
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
