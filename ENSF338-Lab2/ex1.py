import timeit
#original code
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
#1. What does this code do? [0.1 pts] 
# This code uses a recursive function that will take a number 'n', and will check the number is a 0 or 1.
# If the number doesn't match the if statement then the code will continue to the else statement the function
# This else statement will then go create two more smaller instances of the function while reducing the number by 1 and 2 
# These steps repeat until the number either hits 0 or 1 then it'll add them up starting from the most recent instance created until the func is solved.


#2. Is this an example of a divide-and-conquer algorithm (think carefully about this one)? [0.1 pts]
#Yes this code is an example of a divide and conquer algorithm since the code splits into two smaller problems that eventually merges to solve the overall problem.

#3. Give an expression for the time complexity of the algorithm [0.2 pts]
# O(2^n)

#4. Implement a version of the code which uses memoization to improve performance [0.2 pts]
# Memoization version:
memo = {}

def func(n):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        result = func(n-1) + func(n-2)
        memo[n] = result
        return result


#5. Give an expression for the time complexity of the optimized algorithm [0.2 pts]
# O(n)

#6. Time the original code and your improved version, for all integers between 0 and 35, and plot the results (output plots must be called ex1.6.1.jpg and ex1.6.2.jpg) [0.2 pts]
# sent in dropbox
# the code below was used to get each time value for the graphs
for i in range(0,36):
    elasped_time = timeit.timeit(lambda : func(i), number = 1)
    print(f'The execution time for {i} is: {elasped_time} seconds')
