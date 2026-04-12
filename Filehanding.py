def file_operations():

    with open("example.txt", "w") as file:

        file.write("This is the first line of the file.\n")

        file.write("This is the second line of the file.\n")

    print("File written successfully.")

    with open("example.txt", "r") as file:

        contents = file.read()

        print("\nContents of the file:")

        print(contents)

    with open("example.txt", "a") as file:

        file.write("This is the appended line.\n")

    print("\nContent appended successfully.")

    with open("example.txt", "r") as file:

        updated_contents = file.read()

        print("\nUpdated contents of the file after appending:")

        print(updated_contents)



if __name__ == "__main__":

    file_operations()
