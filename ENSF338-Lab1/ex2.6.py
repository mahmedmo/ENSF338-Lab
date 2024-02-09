import timeit

# fact function
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

elapsed_time = timeit.timeit(lambda : fact(100), number=10000)
print("Average time to run the original factorial function 10000 times:", elapsed_time/10000)

# function that runs fact(n) 1000 times using a for loop
def factfl1000(n):
    if n > 100:
        return 0
    for i in range(1000):
        factorial = fact(n)
    return factorial

# function that runs fact(n) 1000 times using list comprehension
def factlc1000(n):
    if n > 100:
        return 0
    factorial = [fact(n) for x in range(1000)]
    return factorial[0]


elapsed_time = timeit.timeit(lambda : factfl1000(100), number=1)
print("Average time it takes to run fact(n) 1000 times using a for loop:", elapsed_time/1000)

elapsed_time = timeit.timeit(lambda : factlc1000(100), number=1)
print("Average time it takes to run fact(n) 1000 times using list comprehension:", elapsed_time/1000)

