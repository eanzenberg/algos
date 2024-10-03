def longestValidParentheses(s: str) -> int:
    def get_item(l: list, i: int) -> int:  #return item in list, or 0 if the list is empty
        if l:
            return l[i]
        else:
            return 0
        
    left_paren = []
    right_paren = []
    max_len = 0
    current_len = 0
    for i, c in enumerate(s):
        if c == '(':
            left_paren.append(i)
        elif c == ')':
            if left_paren and not right_paren:
                left_paren.pop()
                current_len = i - get_item(left_paren, -1)
                if not left_paren:
                    current_len += 1
                if current_len > max_len:
                    max_len = current_len
                print(s, 'a', i, left_paren, right_paren, current_len)

            elif left_paren and right_paren:
                left_paren.pop()
                if get_item(left_paren, -1) > right_paren[-1]:
                    current_len = i - get_item(left_paren, -1)
                else:
                    current_len = i - get_item(left_paren, -1) - right_paren[-1]
                if current_len > max_len:
                    max_len = current_len
                print(s, 'b', i, left_paren, right_paren, current_len)

            elif not left_paren:
                right_paren.append(i)
    return max_len


print(longestValidParentheses("))(()"), 2, "\n")
print(longestValidParentheses("))))((()(("), 2, "\n")
print(longestValidParentheses("(()"), 2, "\n")
print(longestValidParentheses("(()()((()"), 4, "\n")
print(longestValidParentheses(")(()"), 2, "\n")
print(longestValidParentheses("((()"), 2, "\n")
print(longestValidParentheses("()"), 2, "\n")
print(longestValidParentheses("()()()()"), 8, "\n")
print(longestValidParentheses(")()())"), 4, "\n")
print(longestValidParentheses("()(()"), 2, "\n")
print(longestValidParentheses("()((())()"), 6, "\n")
print(longestValidParentheses(""), 0, "\n")
print(longestValidParentheses(")((())("), 4, "\n")
print(longestValidParentheses(")(((((()())()()))()(()))("), 22, "\n")