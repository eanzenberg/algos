from typing import List

def palindromePairs(words: List[str]) -> List[List[int]]:
    def isPalindrome(string: str) -> bool:
        return string == string[::-1]

    words_map = {word: i for i, word in enumerate(words)}
    solution = []

    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix, suffix = word[:j], word[j:]
            
            if isPalindrome(prefix):
                suffix_rev = suffix[::-1]
            
                if suffix_rev != word and suffix_rev in words_map:
                    solution.append([words_map[suffix_rev], i])
            
            if j != len(word) and isPalindrome(suffix):
                prefix_rev = prefix[::-1]

                if prefix_rev != word and prefix_rev in words_map:
                    solution.append([i, words_map[prefix_rev]])
    
    return solution


print(palindromePairs(["abcd","dcba","lls","s","sssll"]))
print(palindromePairs(["bat","tab","cat"]))
print(palindromePairs(["a",""]))