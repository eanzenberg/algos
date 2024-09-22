def pattern_matches(string: str, pattern: str) -> bool:
    def find_number(string: str, ix: int) -> (int, int):
        number = ''
        length = 0
        while string[ix].isnumeric():
            number += string[ix]
            ix += 1
            length += 1

        return (int(number), length)
    
    stringIx = patternIx = 0

    while patternIx < len(pattern):
        if stringIx >= len(string):
            return False
        c = pattern[patternIx]
        if c.isnumeric():
            number, num_length = find_number(pattern, patternIx)
            stringIx += number
            patternIx += num_length
        else:
            if c != string[stringIx]:
                print(stringIx, patternIx)
                return False
            else:
                patternIx += 1
                stringIx += 1

    if patternIx < len(pattern):
        return False
    
    return True


print(pattern_matches('facebook', 'f6k'), True)
print(pattern_matches('face', 'f6k'), False)
print(pattern_matches('internationalization', 'i18n'), True)

# i18n 
# f6k 'facebook'