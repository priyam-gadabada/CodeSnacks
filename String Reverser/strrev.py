def reverse_string(text):
    stack = []
    for i in text:
        stack.append(i)
    rev = ''
    while stack:
        rev += stack.pop()
    return rev

s = input("Enter a string: ")
print("Reversed:", reverse_string(s))
