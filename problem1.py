# Problem 1: Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
s = 0
for n in range(1,1000):
    if n % 3 == 0:
        s = s + n
    elif n % 5 == 0:
        s = s + n
print(s)






