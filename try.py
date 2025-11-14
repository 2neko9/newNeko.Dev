numbers = []
for i in range(5):
    num = float(input(f"Enter number: {i + 1}: "))
    numbers.append(num)

    # Menu for options
print("\nChoose between A,B,C,D : ")
print("A - Sum and Round (up to 2 decimal places)\nB - Min\nC - Max\nD - Pow (raised to the power of 3)")


choice = input("\nEnter your choice (A,B,C,D) !!::IN UPPER CASE:!! : ").upper()
if choice == 'A':
    sum = round(sum(numbers), 2)
    print(f"The Sum (rounded) is: {sum}")
elif choice == 'B':
    min = min(numbers)
    print(f"The Minimum is: {min}")
elif choice == 'C':
    max = max(numbers)
    print(f"The Maximum is: {max}")
elif choice == 'D':
    cube = [round(num ** 3, 2) for num in numbers]
    print(f"Numbers raised to 3: {cube}")
else:
    print("INVALID OPTION!!!")