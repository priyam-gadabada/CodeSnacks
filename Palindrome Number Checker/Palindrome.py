# Palindrome Number Checker

def palindrome(num):
    if num < 0:
        return False
    return str(num) == str(num)[::-1]

num = int(input("Enter a number: "))

if palindrome(num):
    print(f"{num} is a palindrome!")
else:
    print(f"{num} is not a palindrome.")
