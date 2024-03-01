#Code provided by the lab:
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2

# Question 1
# For the Best Case, all elements in li are less or equal to 5 then the inner for loop would not execute, 
# which results in a linear time complexity of O(n).
# For the Worst Case, all elements of li fulfill the if condition of li[i] > 5 so the inner for loop executes each time the outer for loop executes, 
# which results in a time complexity of O(n^2).
# For the Average Case, the time complexity would be half of the Worst Case, which would be O((n^2)/2), which is the same as O(n^2).
                
# Question 2
# The time complexity for average, best, and worst are not the same.
# Here is the modified version of the code:
def processdata_modified(li):
    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= 2**len(li)
# This code will now have complexity of O(n) for best, worse and average.
