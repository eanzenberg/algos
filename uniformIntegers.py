def getUniformNumber(i, n) -> int:
    return int("".join([str(i)] * n))

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    A_len = len(str(A))
    B_len = len(str(B))
    num = 0

    if A <= getUniformNumber(str(A)[0], A_len):
        num += 1
    if B >= getUniformNumber(str(B)[0], B_len):
        num += 1

    if B_len == A_len:
        num += int(str(B)[0]) - int(str(A)[0]) - 1

    else:
        if B_len - A_len >= 2:
            num += 9 * (B_len - A_len - 1)
        num += 9 - int(str(A)[0])
        num += int(str(B)[0]) - 1
    return num


print(getUniformIntegerCountInInterval(75, 300))
print(getUniformIntegerCountInInterval(1, 9))
print(getUniformIntegerCountInInterval(999999999999, 999999999999))
print(getUniformIntegerCountInInterval(75, 3000))
