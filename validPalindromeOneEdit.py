def validPalindrome(s: str) -> bool:
    def is_palindrome(s: str) -> bool:
        start, end = 0, len(s) - 1
        while start <= end:
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True

    def _is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    start, end = 0, len(s) - 1
    
    while start <= end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            if is_palindrome(s[start:end]) or is_palindrome(s[start + 1:end + 1]):
                return True
            else:
                return False
    
    return True


print(validPalindrome("aba"), True)
print(validPalindrome("abca"), True)
print(validPalindrome("abc"), False)
print(validPalindrome("abcdcxba"), True)
print(validPalindrome("abxcdcba"), True)
print(validPalindrome("abcdcbax"), True)