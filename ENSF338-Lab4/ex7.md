## 1. Give an expression for the time complexity of the reverse() implementation. Explain how you reached the conclusion describing your step-by-step reasoning. [0.3 pts]

The time complexity of the reverse() implementation is O($n^2$). The for loop runs $n$ times and in the for loop, get_element_at_pos traverses $n$ times in the worse case and $n/2$ in the average case. So the time complexity for reverse() is O($n$*$n$) = O($n^2$) = O($n$*$n/2$).

## 2. Design an optimized implementation of the same function with better performance. Discuss which changes you made and how they should be expected to result in a better function [0.3 pts]


