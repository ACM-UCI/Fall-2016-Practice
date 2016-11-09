# a: A list of positive integers
# n: A positive integer
# Returns true iff there is a subset of a that sums to n
def subset_sum(a, n):
    # The empty subset has a sum of zero
    sumCheck = [False]*(n + 1)
    sumCheck[0] = True
    
    # Loop over each value
    for val in a:
        newSumCheck = [False]*(n + 1)
        for i in range(n + 1):
            if sumCheck[i]:
                # Keep a previous subset
                newSumCheck[i] = True
                
                # Add the current value to that previous subset
                if(i + val <= n):
                    newSumCheck[i + val] = True

        sumCheck = newSumCheck
        # print(sumCheck)

    return sumCheck[n]
    
def subset_sum_tests():
    print("Subset sum tests, should print True, False")
    print(subset_sum([1, 2, 3], 5)) # Prints True, since 2 + 3 = 5
    print(subset_sum([1, 3, 4], 6)) # Print False, since there is no subset that sums to 6
    
if __name__ == '__main__':
    subset_sum_tests()