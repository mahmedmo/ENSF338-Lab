import numpy as np

def count_consonants(word):
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ" ### doesn't count 'y' as a consonant
    count = 0
    for letter in word:
        if letter in consonants:
            count += 1
    return count

def count_words(line):
    words = 0
    words = line.count(' ') + 1 #counts number of words. +1 to count the first word that is not separated by a space
    return words

def main():

    try:
        with open('pg2701.txt', 'r', encoding='latin-1') as file:
            lines = [line.strip() for line in file.readlines()] #reads lines without newline character '\n'
            array = np.array(lines) #puts lines into an array

        total_consonants = sum(count_consonants(line) for line in array)
        total_words = sum(count_words(line) for line in array)

        if total_words > 0:
            average_consonants = total_consonants / total_words
            print("Average number of consonants per word within the text file is:", average_consonants)
        else:
            print("No words found in the text file.")

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
