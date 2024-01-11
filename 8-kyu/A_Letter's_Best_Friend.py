def best_friend(txt, a, b):
    occurrences = [i for i in range(len(txt) - 1) if txt[i] == a and txt[i + 1] == b]
    return len(occurrences) == txt.count(a)

# Example usage:
result = best_friend("we found your dynamite", "d", "y")

print(result)






# "he headed to the store", "h", "e") ➞ True

# All occurences of "h": ["he", "headed", "the"]
# All occurences of "h" have an "e" after it.
# Return True

# ('abcdee', 'e', 'e') ➞ False

# For first "e" we can get "ee"
# For second "e" we cannot have "ee"
# Return False