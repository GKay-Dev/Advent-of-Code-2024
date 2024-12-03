# [Day 3: Mull It Over](https://adventofcode.com/2024/day/3)

## Problem-Solving Approach

- **Input Parsing**: Read the input file and parse it into a list of strings, where each string represents corrupted memory data.

- **Part One**:
    - **Regex Matching**:
        - Use a regex pattern to find all `mul(X,Y)` instructions, where `X` and `Y` are integers with 1-3 digits.
        - Extract all matches into a list.
    - **Processing**:
        - Extract the numbers `X` and `Y` from each `mul(X,Y)` instruction.
        - Multiply `X` and `Y` for each match and calculate the total sum of all results.

- **Part Two**:
    - **Regex Matching**:
        - Extend the regex to match:
            - `mul(X,Y)` instructions (same as in Part One).
            - `do()` to enable processing.
            - `don't()` to disable processing.
    - **Processing**:
        - Use a `flag` to track whether `mul` instructions are enabled:
            - Set the `flag` to `True` when encountering `do()`.
            - Set the `flag` to `False` when encountering `don't()`.
        - While the `flag` is `True`:
            - Extract numbers `X` and `Y` from `mul(X,Y)`.
            - Multiply `X` and `Y` and add the result to the total sum.
        - Skip processing `mul` instructions when the `flag` is `False`.
    - **Output**: Compute and return the total sum of results from enabled `mul` instructions.
