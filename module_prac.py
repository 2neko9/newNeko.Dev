for num in range(10, 20):     # Iterate between 10 and 20
    for i in range(2, num):  # Iterate on the factors of the number
        if num % i == 0:     # Determine if i is a factor of num
            j = num / i    # Calculate the second factor (using integer division)
            print('%d equals %d * %d' % (num, i, j))
            break           # Move to the next number
    else:
        # This else is associated with the for-loop, not the if-statement
        print(num, 'is a prime number')
