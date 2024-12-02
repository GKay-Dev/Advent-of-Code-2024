# [Day 2: Red-Nosed Reports](https://adventofcode.com/2024/day/2)

## Problem-Solving Approach
- **Read the input file**: Parse the input into a list of lists, where each sublist contains numerical data.
- **Define helper functions**:
    - **Check order**: Verify if the elements in a list are sorted in ascending or descending order.
    - **Check differences**: Ensure the difference between consecutive elements is between 1 and 3 (inclusive).
    - Combine these checks to determine if a list qualifies as a **safe report**.
- **Part One**:
    - Apply the helper functions to each list.
    - Count the number of lists that qualify as safe reports.
- **Part Two**:
    - For each unsafe report, attempt to make it safe by removing a single element.
    - Reapply the helper functions to the modified lists.
    - Count the number of modified lists that qualify as safe reports.
