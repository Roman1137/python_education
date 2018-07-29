print("""Menu
1. File
2. View
3. Exit 
""")

choice = input("Enter your choice: ")
if choice == "1":
    print("You have selectred 'File' menu")
elif choice == "2":
    print("You have selectred 'View' menu")
elif choice == "3":
    print("You have selectred 'Exit' menu")
else:
    print("Incorrect choice")
