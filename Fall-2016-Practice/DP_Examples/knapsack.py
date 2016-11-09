# a: A list of (weight, value) pairs for each possible item
# C: The maximum capacity
# Returns the total value of the best set of items we can choose
def knapsack(a, C):
    # With no elements, we can only get value zero
    maxValues = [0]*(C + 1)

    # Loop over each new value
    for item in a:
        newMaxValues = [val for val in maxValues]
        for i in range(item[0], C + 1):
            nextVal = maxValues[i - item[0]] + item[1]
            if nextVal > newMaxValues[i]:
                newMaxValues[i] = nextVal
                
        maxValues = newMaxValues
        # print(maxValues)
    
    return newMaxValues[C]
    
def knapsack_tests():
    print("Knapsack tests, should print 7, 9")
    print(knapsack([(1,1), (2,3), (3,4)], 5)) # Prints 7, which is achieved using the second and third items
    print(knapsack([(1,5), (3,4), (4,8)], 4)) # Print 9, which is achieved using the first and second items
    
if __name__ == '__main__':
    knapsack_tests()