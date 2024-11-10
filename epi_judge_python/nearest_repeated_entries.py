from typing import List

from test_framework import generic_test


# s = <"All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]
def find_nearest_repetition0(paragraph: List[str]) -> int:
    closest_distance = float('inf')
    for i in range(len(paragraph)):
        distance = 0
        is_word_found = False
        for j in range(i + 1, len(paragraph)):
            if paragraph[i] == paragraph[j]:
                is_word_found = True
                distance += 1
                break

            distance += 1

        if not is_word_found:
            distance = float('inf')

        if distance < closest_distance:
            closest_distance = distance

    return -1 if closest_distance == float('inf') else closest_distance


# s = <"All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]
def find_nearest_repetition(paragraph: List[str]) -> int:
    word_to_latest_distance = {}
    closest_distance = float('inf')

    for i in range(len(paragraph)):
        word = paragraph[i]
        if word in word_to_latest_distance:
            distance = i - word_to_latest_distance[word]
            # TODO: Add to notes (use min() instead of an if structure)
            closest_distance = min(closest_distance, distance)

        word_to_latest_distance[word] = i

    return -1 if closest_distance == float('inf') else closest_distance


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
