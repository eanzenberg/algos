def myPowSlower(x: float, n: int) -> float:
    if n == 0:
        return 1
    
    res = x
    
    for _ in range(abs(n) - 1):
        res *= x

    if n < 0:
        return 1 / res
    else:
        return res
    

def myPow(x: float, n: int) -> float:
    def multiply(x, n):
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        result = multiply(x, n // 2)
        result *= result
        
        print(f"x {x}, n {n}, result {result}")

        if n % 2 == 1:
            return x * result
        else:
            return result
    
    final_answer = multiply(x, abs(n))
    if n >= 0:
        return final_answer
    else:
        return 1 / final_answer


print(myPow(2, 4), 16)
print(myPow(2, 8), 256)
print(myPow(2, 10), 1024)
print(myPow(2.1, 3), 9.26)
print(myPow(2, -2), .25)