#Code provided by the lab:
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2

#Question 1
#For Best Case, if li[i] is less or equal to 5 then the inner for loop would not execute.
#This results in a linear time complexity of O(n)
#For Worst Case, li[i] fulfills the if condition of li[i] > 5 so that the inner for loop executes.
#This results in a time complexity of O(n^2) because within the loop
#For Average Case, the time complexity would be O(n^2) since on average the inner for loop would be executed.
                
#Question 2
#The time complexity for average, best, and worst are not the same.
#Here is the modified version of the code:
def processdata_modified(li):
    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= 2
#This code will now have complexity of O(n) for best, worse and average.