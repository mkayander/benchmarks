# README

## Overview

This Python script `run.py` is a benchmarking tool for different solutions to the problem of finding the first letter to appear twice in a string. The script includes several different solutions to the problem and a function to run benchmarks on these solutions.

## Solutions

1. `array_search_solution(s)`: This function uses an array to keep track of the letters that have been seen. When a letter is encountered that is already in the array, it is returned.

2. `hash_set_solution(s)`: This function uses a set to keep track of the letters that have been seen. When a letter is encountered that is already in the set, it is returned.

3. `char_code_map_solution(s)`: This function uses an array of size 26 (for each letter of the alphabet) to keep track of the letters that have been seen. When a letter is encountered that is already marked in the array, it is returned.

4. `bit_mask_solution(s)`: This function uses a bit mask to keep track of the letters that have been seen. When a letter is encountered that is already marked in the bit mask, it is returned.

## Benchmarking

The `run_benchmark(solution, input)` function is used to run benchmarks on the solutions. It takes a solution function and an input string as arguments. The function measures the time taken by the solution function to solve the problem for the given input and repeats this for a specified number of runs. It then calculates and prints the total, average, median, 75th percentile, 95th percentile, and 99th percentile times.

## Usage

The script can be run from the command line with no arguments. It will run each solution with two different inputs and print the benchmarking results.

Example:

```bash
python run.py
```

This will run each solution with a normal input and a bigger input, and print the benchmarking results.

# Conclusions
### HashSet solution WINS!
Take a look at the results:

```
Number of runs: 100000

Normal input:
----------------------------------
Running benchmark for array_search_solution
Input: abcdefghijklmnopqrstuvwxyziflskecznslkjfabe
Total time: 490901300
Average time: 4909.013
Median time: 4700
75th percentile time: 4700
95th percentile time: 4900
99th percentile time: 13900
----------------------------------
Running benchmark for hash_set_solution
Input: abcdefghijklmnopqrstuvwxyziflskecznslkjfabe
Total time: 186413000
Average time: 1864.13
Median time: 1800
75th percentile time: 1800
95th percentile time: 1900
99th percentile time: 2400
----------------------------------
Running benchmark for char_code_map_solution
Input: abcdefghijklmnopqrstuvwxyziflskecznslkjfabe
Total time: 251516000
Average time: 2515.16
Median time: 2400
75th percentile time: 2400
95th percentile time: 2500
99th percentile time: 3300
----------------------------------
Running benchmark for bit_mask_solution
Input: abcdefghijklmnopqrstuvwxyziflskecznslkjfabe
Total time: 423600000
Average time: 4236.0
Median time: 4000
75th percentile time: 4000
95th percentile time: 4300
99th percentile time: 14600


Bigger input:
----------------------------------
Running benchmark for array_search_solution
Input: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}[]|:<>?/.,;'`~
Total time: 4318789500
Average time: 43187.895
Median time: 40900
75th percentile time: 41500
95th percentile time: 55000
99th percentile time: 79200
----------------------------------
Running benchmark for hash_set_solution
Input: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}[]|:<>?/.,;'`~
Total time: 610226600
Average time: 6102.266
Median time: 5500
75th percentile time: 5700
95th percentile time: 6300
99th percentile time: 21200
```