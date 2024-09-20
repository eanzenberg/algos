def shortestPalindrome(s: str) -> str:
    def isPalindrome(string: str) -> bool:
        return string == string[::-1]
    
    length_of_string = len(s)
    
    if length_of_string in [0, 1] or isPalindrome(s):
        return s
    
    for i in range(1, len(s)):
        if isPalindrome(s[:-i]):
            return s[length_of_string - i:][::-1] + s
        

print(shortestPalindrome("aacecaaa"))
print(shortestPalindrome("abcd"))
print(shortestPalindrome(""))
print(shortestPalindrome("a"))
print(shortestPalindrome("aba"))