## 1. Compare advantages and disadvantages of arrays vs linked list (complexity of task completion) [0.1 pts]

The time complexity for retrievals with a known index is O(1) for Arrays, but is O(n) for Linked Lists. The time complexity for insertion and deletion of an element is O(1) for Linked Lists, but is at worst O(n) for Arrays. Arrays are faster at retrieving, while Linked Lists are faster at inserting and deleting elements.


## 2. For arrays, we are interested in implementing a replace function that acts as a deletion followed by insertion. How can this function be implemented to minimize the impact of each of the standalone tasks? [0.1 pts]

impact?


## 3. Assuming you are tasked to implement a doubly linked list with a sort function, given the list of sort functions below, state the feasibility of using each one of them and elaborate why is it possible or not to use them. [0.4 pts]
  1. Insertion sort
  2. Merge sort

Insertion sort is feasible with doubly linked lists. In doubly linked lists, you can easily move forwards or backwards in the list. When insertion sort needs to move an element, it can do so easily by changing the pointers of a few elements.
Merge sort is feasible with doubly linked lists. Since you can easily move forwards and backwards in the list, merge sort can divide the list into sublists and then merge them, although a temporary list is still required.


## 4. Also show the expected complexity for each and how it differs from applying it to a regular array [0.4 pts]

The time complexity for insertion sort on both doubly linked lists and arrays is O($n^2$). The time complexity for merge sort on both doubly linked lists and arrays is O(nlogn). The sorting algorithms function essentially the same, doing the same comparisons and swaps, so the time complexities for both types are the same.
