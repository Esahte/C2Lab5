def main():
    n = int(input("Enter a non negative integer: "))
    print("Factorial of", n, "is", factorial(n))


# Return the factorial for a specified number
def factorial(n):
    if n == 0:  # Base case
        return 0
    else:
        return n + factorial(n - 1)  # Recursive call


main()  # Call the main function
