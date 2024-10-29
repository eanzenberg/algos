from collections import namedtuple


def longestRepeatingSubstring(s: str) -> int:
    largest = 0

    for length in range(1, len(s)):
        words = set()
        words.add(s[:length])

        for i in range(1, len(s) - length + 1):
            word = s[i:i+length]
            print(word, words)
            if word in words:
                print(f"found: {word}, {words}")
                largest = length
                break

            words.add(word)

        if largest < length:
            break

    return largest


test = namedtuple('test', ['input', 'output'])
tests = [test("abcd", 0),
         test("aaaaa", 4),
         test("abbaba", 2),
         test("aabcaabdaab", 3),
         test("zzzaabcaabdaab", 3)]

for t in tests:
    ans = longestRepeatingSubstring(t.input)
    print(t.input, ans, t.output)
    assert ans == t.output