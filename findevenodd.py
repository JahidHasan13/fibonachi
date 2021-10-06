# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

user_input = int(input("> "))
if (user_input % 2) == 1:
    print("odd")
else:
    print("even")
print(f'the number is {user_input} ')