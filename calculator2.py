def calculate(s: str) -> int:
    def findNums(s: str, ix: int, dir: str) -> (int, int):
        length = len(s)
        if dir == 'r':
            ix += 1
        else:
            ix -= 1
        numStr = ''
        while True:
            c = s[ix]
            if c == ' ':
                pass
            elif c.isnumeric():
                numStr += c
            if (not c.isnumeric() and c != ' ') or ix == 0 or ix == length - 1:
                if dir == 'l':
                    return int(numStr[::-1]), ix
                else:
                    return int(numStr), ix
            if dir == 'r':
                ix += 1
            else:
                ix -= 1
 
    def twoNumProductDivide(s: str, ix: int, op: str) -> (int, int, int):
        if op not in '/*':
            raise Exception
        leftNum, Lix = findNums(s, ix, 'l')
        rightNum, Rix = findNums(s, ix, 'r')
        Lix = 0 if Lix == 0 else Lix + 1
        Rix = len(s) if Rix + 1 == len(s) else Rix 
        
        print(f"twoNum: {s}, {leftNum}, {Lix}, {rightNum}, {Rix}, {ix}")
        if op == '*':
            return (leftNum * rightNum, Lix, Rix)
        else:
            return (leftNum // rightNum, Lix, Rix)

    i = 0          
    while i < len(s):
        c = s[i]
        if c in "*/":
            solution, Lix, Rix = twoNumProductDivide(s, i, c)
            s = f"{s[:Lix]}{solution}{s[Rix:]}"
            i = Lix + len(str(solution))
            print(f"updated s: {s}, {i}")
        else:
            i += 1

    solution = 0
    first = True
    i = 0
    while i < len(s):
        c = s[i]
        if c in "+-":
            if first:
                leftNum, Lix = findNums(s, i, 'l')
                rightNum, Rix = findNums(s, i, 'r')
                if c == '+':
                    solution = leftNum + rightNum
                else:
                    solution = leftNum - rightNum
                first = False
            else:
                rightNum, Rix = findNums(s, i, 'r')
                if c == '+':
                    solution += rightNum
                else:
                    solution -= rightNum
            i = Rix
        else:
            i += 1
    if first:
        return int(float(s))
    return solution

print(calculate(" 3+5 / 2 "), 5)
print(calculate(" 3/2 "), 1)
print(calculate("3+2*2"), 7)
print(calculate("3*2"), 6)
print(calculate("0*0"), 0)
print(calculate("1+1+1"), 3)
print(calculate("2*3+4"), 10)
print(calculate("1+2+3+4+5"), 15)
print(calculate("2*3*4"), 24)
print(calculate("2*3*40*10"), 2400)
print(calculate("4/3+2"), 3)
print(calculate("14/3*2"))