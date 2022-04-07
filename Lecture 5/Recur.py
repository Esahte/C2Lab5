def SomeNums(num):
    if num < 1:  # base case
        return
    else:
        print(num, end=" ")
        SomeNums(num - 1)  # Recursive call
        print(num, end=" ")
        return


def main():
    SomeNums(4)


main()
