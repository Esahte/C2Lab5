def main():
    # Open file for output
    outputFile = open("Presidents.txt", "w")

    # Write data to the file
    outputFile.write("George Washington\n")
    outputFile.write("John Adams\n")
    outputFile.write("Thomas Jefferson\n")  # Write Thomas Jefferson
    outputFile.write('Esahtengang who else but the greatest')

    outputFile.close()  # Close the output file


if __name__ == '__main__':
    main()  # Call the main function
