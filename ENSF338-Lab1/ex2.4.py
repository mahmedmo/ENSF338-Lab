import numpy as np
import timeit

def count_vowels(word):
    vowels = "aeiouyAEIOUY" ### counts 'y' as a vowel
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

def count_words(line):
    words = 0
    words = line.count(' ') + 1 #counts number of words. +1 to count the first word that is not separated by a space
    return words

def avg_vowels(arr): # made to allow for timing
    total_vowels = sum(count_vowels(line) for line in arr)
    total_words = sum(count_words(line) for line in arr)
    average_vowels = total_vowels/total_words
    return total_vowels, total_words, average_vowels


def main():

    try:
        with open('pg2701.txt', 'r', encoding='latin-1') as file:
            lines = [line.strip() for line in file.readlines()] #reads lines without newline character '\n'
            array = np.array(lines) #puts lines into an array

        elapsed_time = timeit.timeit(lambda : avg_vowels(array), number = 100)

        total_vowels, total_words, average_vowels = avg_vowels(array) # added so that total_vowels, total_words, average_vowels have values to allow for printing (not counted in timing so it's still only timing 100 repetitions)
        if total_words > 0:
            average_vowels = total_vowels / total_words
            print("Average number of vowels per word within the text file is:", average_vowels)
        else:
            print("No words found in the text file.")
        
        print("Average time it took to compute the average number of vowels: ", elapsed_time/100)

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
