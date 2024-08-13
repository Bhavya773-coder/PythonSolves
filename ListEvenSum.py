def sum_of_even_numbers(numbers):
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers)
print("Sum of even numbers:",result)