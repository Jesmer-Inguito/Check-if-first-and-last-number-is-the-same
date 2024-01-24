# pseudocode

def first_and_last (List):
    # Show the given numbers
    print("The numbers are:", List)

    # Check if first and last numbers are the same
    first_num = List[0]
    last_num = List[-1]

    if first_num == last_num:
        return True
    # Else
    else:
        return False

numbers_1 = [10, 20, 40, 50, 10]
numbers_2 = [20, 40, 60, 80, 45]

# Print results
print("Result is", first_and_last(numbers_1))
print("Result is", first_and_last(numbers_2))