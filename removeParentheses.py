def minRemoveToMakeValid(s: str) -> str:
    left_paren = []
    right_paren = []

    result = ''

    for i, c in enumerate(s):
        if c == '(':
            left_paren.append(i)
        elif c == ')':
            if left_paren:
                left_paren.pop()
            elif not left_paren:
                right_paren.append(i)
    
    print(s, left_paren, right_paren)

    for i in range(len(s)):
        if not i in left_paren + right_paren:
            result += s[i]

    return result


print(minRemoveToMakeValid("lee(t(c)o)de)"), "lee(t(c)o)de")
print(minRemoveToMakeValid("a)b(c)d"), "ab(c)d")
print(minRemoveToMakeValid("))(("), "")