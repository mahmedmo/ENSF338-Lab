## What is a profiler, and what does it do?
# A profiler is a tool that's used to measure the performance a program. 
# It tracks how often and for how long different parts of the program are executed.

## How does profiling differs from benchmarking?
# Profiling differs from benchmarking in that profiling is mainly for helping you understand the behaviour of a program,
# while benchmarking is used to test and compare the performance of different systems running the same program or
# to test and compare the performance of different versions of the same program.

## Use a profiler to measure execution time of the program (skip function definitions)

import cProfile

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
# third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]


# Profile third_function
print("third_function profiling:")
cProfile.run('third_function()')

# Profile test_function
print("test_function profiling:")
cProfile.run('test_function()')

## Discuss a sample output. Where does execution time go?
# The execution time goes mostly into running third_function(), specifically the creation of the list using list comprehension.
# Running test_function() did not take very much time at all. 
