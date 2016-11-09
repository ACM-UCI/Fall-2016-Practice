# n: A positive integer
# Returns the nth Fibonacci number
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        vals = [0]*(n + 1)
        vals[0] = 1
        vals[1] = 1
        
        for i in range(2, n + 1):
            vals[i] = vals[i - 1] + vals[i - 2]
        return vals[n]
        
def fib_tests():
    print("Testing Fibonacci, should print 1, 5, 89, 573147844013817084101")
    print(fib(1))
    print(fib(4))
    print(fib(10))
    print(fib(100))
    
if __name__ == '__main__':
    fib_tests()