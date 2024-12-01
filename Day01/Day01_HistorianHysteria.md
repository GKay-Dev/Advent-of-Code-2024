# [Day 1: Historian Hysteria](https://adventofcode.com/2024/day/1)

## Problem-Solving Approach
- **Read the input file**: Parse the provided input and split it into two separate lists based on the two columns.
- **Part One**:  
    - Sort both lists in ascending order.
    - Calculate the difference between each pair of elements at the same indices in the two lists.
    - Compute the total sum of these differences to determine the **total distance** between the lists.
    - Implemented this using **list comprehension** for efficiency and readability.
- **Part Two**:  
    - Multiply each element in the left list by the frequency of the same element in the right list.
    - Sum these products to compute the **similarity score**.
