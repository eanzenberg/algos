from typing import List
from collections import Counter


def longestPalindrome(words: List[str]) -> int:
    solution = 0
    switched_two_letters = [] # Store the inverse so we don't repeat. Conversely, we can subtract them out later
    has_same_two_letters_odd = False # Track if, for example, 'gg' has an odd count, it can be in the middle of the Palindrome
    word_counts = Counter(words) # We don't just need a dict, we need a dictionairy of counts

    for word in word_counts:
        if word[::-1] in word_counts and word[0] != word[1] and word not in switched_two_letters: # Check if the inverse of the word is in the dictionairy
            switched_two_letters.append(word[::-1])
            print(f"{word}, {switched_two_letters}, {word_counts}")
            solution += 4 * min(word_counts[word], word_counts[word[::-1]])

        elif word[0] == word[1]: # Math to track when the word has the same chars
            counts = word_counts[word]
            if counts % 2 == 0:
                solution += 2 * counts
            else:
                has_same_two_letters_odd = True
                solution += 2 * (counts - 1)

    if has_same_two_letters_odd: # Finally add 2 for the lone 'gg' in the middle
        solution += 2

    return solution


print(longestPalindrome(["lc","cl","gg"]), 6)
print(longestPalindrome(["cc","ll","xx"]), 2)
print(longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]), 22)