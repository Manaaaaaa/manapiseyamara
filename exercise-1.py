def replace_last(numbers):
    if  len(numbers) <= 1:
      return numbers
    else:
      return [numbers[-1]] + numbers[:-1]

numbers_input = input("Enter numbers separated by commas: ").strip()
numbers_list = [int(num) for num in numbers_input.split(',')]
print(replace_last(numbers_list))
