def longestPalindrome(s: str) -> str:
    def check_left_right(s: str, start: int, end: int):
        result = s[start: end + 1]
        while start > 0 and end < (len(s) - 1):
            start -= 1
            end += 1
            if s[start] == s[end]:
                result = s[start] + result + s[end]
            else:
                return result
        return result


    def find_similar_chars_forward(s: str, c: str, i: int) -> int:
        end = i
        ix = i + 1
        while ix < len(s):
            if s[ix] !=  c:
                return ix - 1
            ix += 1
        return ix


    if len(s) == 1:
        return s

    max_pali = ''
    i = 0
    while i < len(s) - 1:
        c = s[i]
        end = find_similar_chars_forward(s, c, i)
        pali = check_left_right(s, i, end)
        if len(pali) > len(max_pali):
            max_pali = pali
        if end > i:
            i = end
        else:
            i += 1

    return max_pali


print(longestPalindrome("babad"), "bab")
print(longestPalindrome("cbbd"), "bb")
print(longestPalindrome("a"), "a")
print(longestPalindrome("ccc"), "ccc")
print(longestPalindrome("cccc"), "cccc")