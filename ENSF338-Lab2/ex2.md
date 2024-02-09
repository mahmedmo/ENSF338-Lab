# Exercise 2
## Mention at least two aspects that make interpolation search better than binary search.
- it starts dividing closer to the target value, so it should need less divisions to reach the target value
- with larger datasets, it would likely skip over more data since it starts dividing closer to the target value, further reducing the comparisons needed

## Interpolation search assumes that data is uniformly distributed. What happens this data follows a different distribution? Will the performance be affected? Why?
Yes, the performance of interpolation search would be affected negatively. Interpolation search would lose its advantage of starting division closer to the target value because the target value would not be where interpolation search assumes it would be. For example, if the data was sorted in reverse order, it would on average be slower than binary search.

## If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected? 
The line 'pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))' would be affected.

## When is linear search your only option for searching data as binary and interpolation search may fail?
Linear search is your only option when the data is unsorted, because then binary and interpolation search cannot make any assumptions to find the target value more quickly.

## In which case will linear search outperform both binary and interpolation search, and why?
In the case that the target value is at the beginning of the data, linear search can find it in one step, while binary and interpolation search would need to make multiple divisions and comparisons to find it.

## Is there a way to improve binary and interpolation search to solve this issue?
You could make binary and interpolation search check the first value every time before running normally. This would make the adjusted binary and interpolation search find the target value in one step if the target value was at the beginning of the data, but having the target value be at the start is a rare case. More commonly, the target value is not at the start, so this adjustment would add an unnecessary step extra step for most cases. Because of this, I would say that there is no way to improve binary and interpolation search to solve this issue.
