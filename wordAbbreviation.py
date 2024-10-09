def pattern_matches(word: str, abbr: str) -> bool:
    def find_number(string: str, ix: int) -> (int, int):  # type: ignore
        number = ''
        length = 0
        while ix < len(string):
            if string[ix].isnumeric():
                number += string[ix]
                length += 1
            else:
                break
            ix += 1            

        if number[0] == '0':
            return (0, 0)

        return (int(number), length)
    
    stringIx = patternIx = 0

    while patternIx < len(abbr):
        if stringIx >= len(word):
            return False
        c = abbr[patternIx]
        if c.isnumeric():
            number, num_length = find_number(abbr, patternIx)
            if num_length == 0:
                 return False
            stringIx += number
            patternIx += num_length
        else:
            if c != word[stringIx]:
                return False
            else:
                patternIx += 1
                stringIx += 1

    if patternIx != len(abbr):
        return False
    
    if stringIx != len(word):
        return False
    
    return True


print(pattern_matches('alkiopub', 'a6b'), True)
print(pattern_matches('abcd', 'a6d'), False)
print(pattern_matches('internationalization', 'i18n'), True)
print(pattern_matches('internationalization', "i5a11o1"), True)
print(pattern_matches('internationalization', "i12iz4n"), True)
print(pattern_matches('abbde', "a1b01e"), False)
print(pattern_matches('a', '2'), False)
print(pattern_matches('hi', '1'), False)
