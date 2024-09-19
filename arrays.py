def moveZeros(l: list()):
    for i in range(len(l)):
        if l[i] == 0:
            l = l[0:i] + l[i+1:] + [0]

    num_nonzeros = sum([x != 0 for x in l])
    return l #, num_nonzeros  # Time: O(2N) Memory: O(N)

def sumToZero(l: []):
    for i in range(len(l)):
        for j in range(len(l)):
            for k in range(len(l)):
                if i != j  and j != k and i != k:
                    if (l[i] + l[j] + l[k]) == 0:
                        return True #Time O(N^3) Space O(1)
    return False

def sumToZeroFast(l: []):
    sums = {}
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i]+l[j] not in sums:
                sums[l[i]+l[j]] = None
    for i in range(len(l)):
        if l[i] * -1 in sums.keys():
            print(l[i], sums.keys())
            return True

    return False # Time O(N^2 + N) Space O(N^2)

print(moveZeros([0, 1, 0, 3, 2, 0, 5]))
# print(sumToZero([3, 5, 8, 10, -9, -11, 16, 2]))
# print(sumToZeroFast([3, 5, 8, 10, -9, -11, 16, 2]))
print(moveZeros([0,1,0,3,12]))