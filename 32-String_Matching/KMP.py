# KMP - Truly linear string matching Algorithm
# Compute all π[] values for the pattern p in O(∣p∣) time.
# Use these π[] values in the KMP matching step to find all
#occurrences of p in s in O(∣s∣) time.
#The total running time is O(∣p∣ + ∣s∣): linear time!

# Apart from the strings themselves, the algorithm uses O(∣p∣)
# memory (we assume printing the matches requires O(1) memory)
# We can also do in 0(1) but its in the exercise 32-1

def pi_array(pattern):
    pi = [0] * len(pattern)
    for i in range(1, len(pattern)):
        j = pi[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            pi[i] = j + 1
    return pi

def KMP(text, pattern):
    pi = pi_array(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i - len(pattern) + 1
    return -1

string = "abhcdskhksd"
pattern = "ksd"
print(KMP(string, pattern))