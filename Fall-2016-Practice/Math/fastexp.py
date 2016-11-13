
# computes x^n mod m
def exp(x, n, m):
    result = 1
    currentPower = x
    while n > 0:
        # At any iteration, my final answer is result * (currentPower ** n)
        if n % 2 == 1:
            result = (result * currentPower) % m
        
        currentPower = (currentPower * currentPower) % m
        n /= 2
        
    return result