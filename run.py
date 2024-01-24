import time
import argparse, sys

parser=argparse.ArgumentParser()

parser.add_argument("--count", help="How many times to run each solution", type=int, default=100000)

args=parser.parse_args()
print("Number of runs: " + str(args.count) + "\n")

# 2351. First Letter to Appear Twice https://leetcode.com/problems/first-letter-to-appear-twice/description/


def array_search_solution(s):
    seen_letters = []
    for letter in s:
        if letter in seen_letters:
            return letter
        seen_letters.append(letter)

    return None

def hash_set_solution(s):
    seen_letters = set()
    for letter in s:
        if letter in seen_letters:
            return letter
        seen_letters.add(letter)

    return None

def char_code_map_solution(s):
    seen_letters = [0] * 26
    offset = ord('a')
    for letter in s:
        charCode = ord(letter) - offset
        if seen_letters[charCode] == 1:
            return letter
        seen_letters[charCode] = 1

    return None

def bit_mask_solution(s):
    seen_letters = 0
    offset = ord('a')
    for letter in s:
        charCode = ord(letter) - offset
        if seen_letters & (1 << charCode) > 0:
            return letter
        seen_letters |= (1 << charCode)

    return None

def run_benchmark(solution, input, numberOfRuns=args.count):
    print("----------------------------------")
    print("Running benchmark for " + solution.__name__)
    print("Input: " + input)
    runData = []
    for i in range(numberOfRuns):
        startTime = time.perf_counter_ns()
        solution(input)
        elapsedTime = time.perf_counter_ns() - startTime
        runData.append(elapsedTime)

    # print("runData:", runData)
    print("Total time: " + str(sum(runData)))
    averageTime = sum(runData) / len(runData)
    sortedRunData = sorted(runData)
    medianTime = sortedRunData[len(sortedRunData) // 2]
    p75Time = sortedRunData[int(len(sortedRunData) * 0.75)]
    p95Time = sortedRunData[int(len(sortedRunData) * 0.95)]
    p99Time = sortedRunData[int(len(sortedRunData) * 0.99)]

    print("Average time: " + str(averageTime))
    print("Median time: " + str(medianTime))
    print("75th percentile time: " + str(p75Time))
    print("95th percentile time: " + str(p95Time))
    print("99th percentile time: " + str(p99Time))


# normal input
input1 = "abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"

# a bigger input for bigger differences
input2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}[]|:<>?/.,;'`~"

print("Normal input:")
run_benchmark(array_search_solution, input1)
run_benchmark(hash_set_solution, input1)
run_benchmark(char_code_map_solution, input1)
run_benchmark(bit_mask_solution, input1)

print("\n")
print("Bigger input:")
run_benchmark(array_search_solution, input2)
run_benchmark(hash_set_solution, input2)
