vals = input().split()
n = int(vals[0])
k = int(vals[1])

if k > n:
    k = n

payments = [0]*n
deductions = [0]*n
for i in range(n):
    vals = input().split()
    payments[i] = int(vals[0])
    deductions[i] = int(vals[1])
    
# Translate problem to subtract all deductions, then add deductions to each payment
earnings = -1*sum(deductions)
totalPayments = [payments[i] + deductions[i] for i in range(n)]
totalPayments.sort(reverse=True)

for i in range(k):
    earnings += totalPayments[i]
    
if earnings > 0:
    print(earnings)
else:
    print(0)
