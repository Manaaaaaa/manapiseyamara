def reverse_ascending(numbers):
    result = []
    subsequence = []
    for num in numbers:
        if not subsequence or num > subsequence[-1]:
            subsequence.append(num)
        else:
            result.extend(reversed(subsequence))
            subsequence = [num]
    result.extend(reversed(subsequence))
    
    return result
print(f"\n{'~' * 60}\n")
print("\n")
original_list = input("Enter list of numbers separated by spaces or commas: ")
original_list = [int(x) for x in original_list.replace(',', ' ').split()] 
modified_iterable = reverse_ascending(original_list)
print("\n")
print(f"\n{'~' * 60}\n")
print("\n")
print(" Ascending Numbers 👇")
print("\n", modified_iterable)
print("\n")
print(f"\n{'~' * 60}\n")
