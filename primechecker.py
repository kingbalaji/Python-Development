def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


def reverse_string(s):
    return s[::-1]
print(reverse_string(input("Enter a string: ")))

def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
number=[10,20,30,99,999]
print(find_largest(number))

def calculate_percentage(part, whole):
    return (part / whole) *100
print(calculate_percentage(100,2000))

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("dad"))