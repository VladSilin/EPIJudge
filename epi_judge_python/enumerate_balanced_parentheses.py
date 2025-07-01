from typing import List

from test_framework import generic_test, test_utils

# Input:
# num_pairs: int, the number of matched pairs of parens

# Output:
# all_possible_strings_with_num_pairs: List[str], all possible strings with the given number of matched pairs of parens

# Notes / Assumptions:
# - Can add a pair of parens by:
#   - Adding a leading left and trailing right
#   - Appending

# Examples:

# Outline:


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    def directed_generate_balanced_parentheses(
        num_left_parens_needed, num_right_parens_needed, valid_prefix, result=[]
    ):
        # Able to insert '('
        if num_left_parens_needed > 0:
            directed_generate_balanced_parentheses(
                num_left_parens_needed - 1, num_right_parens_needed, valid_prefix + "("
            )

        # Able to insert ')'
        if num_left_parens_needed < num_right_parens_needed:
            directed_generate_balanced_parentheses(
                num_left_parens_needed, num_right_parens_needed - 1, valid_prefix + ")"
            )

        if not num_right_parens_needed:
            result.append(valid_prefix)

        return result

    return directed_generate_balanced_parentheses(num_pairs, num_pairs, "")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "enumerate_balanced_parentheses.py",
            "enumerate_balanced_parentheses.tsv",
            generate_balanced_parentheses,
            test_utils.unordered_compare,
        )
    )
