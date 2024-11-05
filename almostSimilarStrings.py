def almost_similar_strings(str1: str, str2: str) -> bool:
    
    def is_mostly_similar(str1: str, str2: str) -> bool:
        num_changes = 0
        for i in range(len(str1)):
            if num_changes > 1:
                return False
            if str1[i] != str2[i]:
                if str2 == str1[:i] + str1[i+1:]:
                    return True
                else:
                    num_changes += 1

        return True    
    

    len1, len2 = len(str1), len(str2)

    if len1 > len2:
        result = is_mostly_similar(str1, str2)
    else:
        result = is_mostly_similar(str2, str1)  
    
    return result


print(almost_similar_strings('abcd', 'abxd'), True)
print(almost_similar_strings('aabad', 'aaad'), True)
print(almost_similar_strings('abc', 'ada'), False)
