# Timeit Analysis

## Question 1

### Factors to Consider
- **CPU**: The efficiency of the CPU in handling tasks.
- **Garbage Collection**: Management of no longer needed data.
- **Disk I/O (overall resource usage)**: How resources are allocated and managed, affecting performance during computation or file access.
- **JIT Compilation**: The impact of Just-in-Time compilation, where the first execution of a function may be slower than subsequent executions.

### Appropriate Use Cases

#### `timeit.timeit`
- Ideal for basic timing needs for a function over a specified number of iterations.
- Helps average out random fluctuations through the `number=` parameter, reducing variance.

#### `timeit.repeat`
- Useful for executing the timing multiple times to identify and analyze fluctuations more accurately.
- Mitigates the initial overhead of JIT compilation by allowing multiple executions.
- Best suited for more thorough and extensive benchmarking needs.

## Question 2

### Statistics for Analysis

#### `timeit.timeit`
- **Average** is the key statistic, as it provides a total time that, when divided by the number of iterations (`number=`), yields an effective average time per iteration. This is crucial for understanding the average case performance.

#### `timeit.repeat`
- **Min and Max** are significant statistics, offering insight into the best and worst case scenarios by identifying the shortest and longest times across multiple executions. This helps in understanding the range of execution times and potential variability.
- While the average is also useful here, it requires aggregating and dividing the total of all times by the total number of executions, a step more involved compared to using `timeit.timeit` for average time calculation.
