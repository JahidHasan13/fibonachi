# Program to display the Fibonacci sequence up to n-th term

nterm = int(input("please enter the nth number "))

# the 1st two numbers of the sequence

n1, n2 = 0, 1
count = 0
if nterm <= 0:
    print("Please enter a valid Number!! the number is invalid ")
elif nterm == 0:
    print(n1)
    print("the sequence is ", nterm, "!")
else:
    print("the fibonacci series is ")
    while count < nterm:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
