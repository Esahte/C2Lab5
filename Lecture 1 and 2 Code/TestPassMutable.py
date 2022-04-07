from Circle import Circle


def main():
    # Create a Circle object with radius 1
    myCircle = Circle()

    # Print areas for radius 1, 2, 3, 4, and 5.
    n = 5
    printAreas(myCircle.radius, n)

    # Display myCircle.radius and times
    print("\nRadius is", myCircle.radius)
    print("n is", n)


# Print a table of areas for radius 
def printAreas(c, times):
    print("Radius \t\tArea")
    while times >= 1:
        print(c.__radius, "\t\t", c.getArea())
        c.__radius = c.__radius + 1  # increase radius by 1
        times -= 1


main()  # Call the main function
