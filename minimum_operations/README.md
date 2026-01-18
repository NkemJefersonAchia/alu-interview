# Minimum Operations

## Description
This project contains a solution to the "Minimum Operations" problem. Given a text file with a single character 'H', and a text editor that can only perform "Copy All" and "Paste" operations, the goal is to calculate the minimum number of operations needed to achieve exactly n 'H' characters.

## Requirements
- Ubuntu 14.04 LTS
- Python 3.4.3
- PEP 8 style (version 1.7.x)

## Algorithm
The solution is based on prime factorization. To get n H's optimally, we need to find the sum of all prime factors of n. Each prime factor represents a necessary sequence of "Copy All" followed by paste operations.

## Usage
```bash
./0-main.py
```

## File
- `0-minoperations.py`: Contains the `minOperations` function

## Author
Nkem Jeferson Achia
