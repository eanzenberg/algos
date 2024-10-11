def simplifyPath(path: str) -> str:
    def count_chars(path: str, i: int, target: str) -> int:
        count = 0
        while i < len(path):
            if path[i] == target:
                count += 1
                i += 1
            else:
                break
        return count

    i = 0
    result = ''
    while i < len(path):
        c = path[i]
        if c == '/':
            num_dashes = count_chars(path, i, '/')
            if len(result) != 1:
                result += '/'
            i += num_dashes
        elif c == '.':
            num_periods = count_chars(path, i, '.')
            if (i + num_periods < len(path) and path[i + num_periods] != '/') or path[i - 1] != '/':
                result += '.' * num_periods
                i += num_periods
                continue
            if num_periods == 1:
                if len(result) != 1:
                    result = result[:-1]
                i += 1
            elif num_periods == 2:
                dashes_to_remove = 2
                while dashes_to_remove != 0 and len(result) > 1:
                    popped_char = result[-1]
                    result = result[:-1]
                    if popped_char == '/':
                        dashes_to_remove -= 1  
                i += 2
            else:
                result += '.' * num_periods
                i += num_periods
        else:
            result += c
            i += 1
 #       print(path[:i], result)

    end = result[-1]
    while end == '/' and len(result) > 1:
        end = result[-1]
        if end == '/':
            result = result[:-1]
            end = result[-1]

    return result


print(simplifyPath("/home/"), "/home")
print(simplifyPath("/../"), "/")
print(simplifyPath("/home//foo"), "/home/foo")
print(simplifyPath("/home/user/Documents/../Pictures"), "/home/user/Pictures")
print(simplifyPath("/.../a/../b/c/../d/./"), "/.../b/d")
print(simplifyPath("/a/./b/../../c/"), "/c")
print(simplifyPath("/x/y/z/a/./b/../../c/"), "/x/y/z/c")
print(simplifyPath("/."), "/")
print(simplifyPath("/a//b.."), "/a/b..")
print(simplifyPath("/..hidden"), "/..hidden")
print(simplifyPath("/hello../world"), "/hello../world")