try: a = int(input("Enter a number: "))
except ValueError: print("That's not a valid number!")
else: 
    for i in range(1, 11):
        print(f"{a} x {i} = {a * i}")
