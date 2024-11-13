from typing import Set

import string
from test_framework import generic_test
from collections import defaultdict, deque, namedtuple

# Given:
# s: str
# t: str
# D: Set[str]

# Sequence of strings P, [p[0] == s, p[1], ... , p[n - 1] == t]:
#   - Starting with s, ending with t
#     - len(p[i - 1]) == len(p[i])
#     - char_diff(p[i - 1], p[i]) == 1
#   - s produces t if there exists a sequence P

# - Assume lowercase alphabetic

# Return:
# len(P) of shortest P if s produces t
# -1 if s does not produce t

# Notes:
# - Relationship between p[i - 1], p[i] potentially implies a graph
#   - Shortest P implies BFS

# Example:
# s = cat
# t = dog
# D = { bat, cot, dog, dag, dot, cat }

# Approach:
# - Build a graph with set of vertices D
# - An edge b/w D[i], D[j] => len(s) == len(t) == len(D[i - 1]) == len(D[i]) and distance(D[i], D[j]) == 1
def transform_string0(D: Set[str], s: str, t: str) -> int:
    if len(s) != len(t):
        return -1

    word_length = len(s)

    def word_distance(w1: str, w2: str) -> int:
        count_diff_chars = 0
        for corresponding_chars in zip(w1, w2):
            if corresponding_chars[0] != corresponding_chars[1]:
                count_diff_chars += 1

        return count_diff_chars

    reachable_words_graph = defaultdict(set)
    # D_filtered = set(filter(lambda w: len(w) == word_length, D))
    for word in D:
        for other_word in D:
            if word_distance(word, other_word) == 1:
                reachable_words_graph[word].add(other_word)

    #print('reachable_words_graph', reachable_words_graph)
    search_queue = [s]
    visited = []
    node_to_parent = {}
    while search_queue:
        cur_node = search_queue.pop(0)
        visited.append(cur_node)

        if cur_node == t:
            break

        # {'dot': {'dog', 'cot'}, 'cot': {'dot', 'cat'}, 'cat': {'cot', 'bat'}, 'bat': {'cat'}, 'dog': {'dot', 'dag'}, 'dag': {'dog'}}
        for node in reachable_words_graph[cur_node]:
            if node not in visited:
                node_to_parent[node] = cur_node
                search_queue.append(node)

    print('parent_path', node_to_parent)

    path_trace_node = t
    path_length = 0
    while path_trace_node is not None:
        print('trace node {trace}, parent {parent}'.format(trace=path_trace_node, parent=node_to_parent[path_trace_node]))
        path_length += 1
        path_trace_node = node_to_parent[path_trace_node] if path_trace_node in node_to_parent else None


    return path_length


def transform_string(D: Set[str], s: str, t: str) -> int:
    WordToPathDistance = namedtuple('StringDistance', ('word', 'distance'))
    search_queue = deque([WordToPathDistance(s, 0)])
    # Mark s as visited
    D.remove(s)

    while search_queue:
        cur_word, distance = search_queue.popleft()

        # NOTE: Could also put this here instead of the check in the loops
        #if cur_word == t:
        #    return distance + 1

        for i in range(len(cur_word)):
            for c in string.ascii_lowercase:
                word_variation = cur_word[:i] + c + cur_word[i + 1:]

                if word_variation == t:
                    return distance + 1

                if word_variation in D:
                    D.remove(word_variation)
                    search_queue.append(WordToPathDistance(word_variation, distance + 1))

    return -1

if __name__ == '__main__':
    #s_test = 'cat'
    #t_test = 'dog'
    #D_test = {'bat', 'cot', 'dog', 'dag', 'dot', 'cat'}

    #result = transform_string(D_test, s_test, t_test)
    #print(result)

    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
