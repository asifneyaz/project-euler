# sum of Fibonacci numbers


# Computes value of first
# fibonacci numbers
def calculate_sum(n):
    if n <= 0:
        return 0

    fibo = [0] * (n + 1)
    print(fibo)
    fibo[1] = 1

    # Initialize result
    sm = fibo[0] + fibo[1]

    # Add remaining terms
    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
        sm = sm + fibo[i]
    print(fibo)
    return sm


# Driver program to test
# above function
n = 4
print("Sum of Fibonacci numbers is : ", calculate_sum(n))
