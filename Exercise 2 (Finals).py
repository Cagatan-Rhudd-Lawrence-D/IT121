try:
    Short_Note_or_Message = input("Enter a Short Note/Message: ")
    with open("notes.txt", "w") as file:
        file.write(Short_Note_or_Message + "\n" + "\n")

    with open("notes.txt", "r") as file:
        print("\nYour Short Note/Message:")
        print(file.read())

    New_Note_or_Message = input("Enter new Note/Message: ")
    with open("notes.txt", "a") as file:
        file.write(New_Note_or_Message + "\n" + "\n")
    with open("notes.txt", "r") as file:
        print("\nYour Updated Short Note/Message:")
        print(file.read())

except FileNotFoundError:
    print("Error: File Not Found!")

except PermissionError:
    print("Error: Permission Denied! File might be open in another Program or you lack Access!")

except IsADirectoryError:
    print("Error: A file named 'notes.txt' already exists in this folder!")

except KeyboardInterrupt:
    print("You Cancelled the Program!")

except OSError:
    print("Error: System Error Occured!")